import argparse
import json
import os

import tqdm
from doccano_api_client import DoccanoClient
from admin_config import ADMIN_CONFIG


def create_project(client: DoccanoClient,
                   project_name: str,
                   description: str,
                   project_type: str,
                   resource_type: str):
    result = client.create_project(name=project_name,
                                   description=description,
                                   project_type=project_type,
                                   resourcetype=resource_type)
    return result['id']


def add_image(client: DoccanoClient,
              project_id: int,
              image_path: str):
    upload_ids = []
    try:
        image = open(image_path, 'rb')
        fp_resp = client.post("v1/fp/process/", files={"filepond": image}, as_json=False)
        fp_resp.raise_for_status()
        upload_ids.append(fp_resp.text)
    except Exception as e:
        # revert previous uploads if we have a problem
        for upload_id in upload_ids:
            client.delete(
                "v1/fp/revert/", data=upload_id, headers={"Content-Type": "text/plain"}
            )
        raise e
    upload_data = {
        "uploadIds": upload_ids,
        "format": "ImageFile",
        'task': "IMAGE_CAPTIONING"
    }
    try:
        client.post(f"v1/projects/{project_id}/upload", json=upload_data)
        return upload_ids[0]
    except Exception as e:
        print(e)


def do_create(host_name: str,
              admin_username: str,
              admin_password: str,
              project_name: str,
              description: str,
              project_type: str,
              resource_type: str,
              root: str,
              images: list):
    client = DoccanoClient(host_name, admin_username, admin_password)
    project_id = create_project(client,
                                project_name,
                                description,
                                project_type,
                                resource_type)
    for image in tqdm.tqdm(images):
        image_id = add_image(client,
                             int(project_id),
                             os.path.join(root, image['path']))
        for text in image['text']:
            url = f'v1/projects/{project_id}/examples/{image_id}/texts'
            client.post(url, json={"text": text})


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="creating project")
    parser.add_argument("-pn", "--project_name", type=str, help="name of project")
    parser.add_argument("-de", "--description", type=str, default="", help="description of project")
    parser.add_argument("-pt", "--project_type", type=str, default="ImageCaptioning", help="type of project")
    parser.add_argument("-rt", "--resource_type", type=str, default="ImageCaptioningProject", help="type of resource")
    parser.add_argument("--r", "--image_root", type=str, default="", help="image_root")
    parser.add_argument("-dp", "--data_path", type=str, default="", help="path of json data")
    arg = parser.parse_args()
    images = json.loads(open(arg.data_path, 'r', encoding='utf-8').read())
    do_create(**ADMIN_CONFIG,
              project_name=arg.project_name,
              description=arg.description,
              project_type=arg.project_type,
              resource_type=arg.resource_type,
              root=arg.image_root,
              images=images)
