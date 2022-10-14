import argparse
from doccano_api_client import DoccanoClient
from admin_config import ADMIN_CONFIG


def create_project(host_name: str,
                   admin_username: str,
                   admin_password: str,
                   project_name: str,
                   description: str,
                   project_type: str,
                   resource_type: str):
    client = DoccanoClient(host_name, admin_username, admin_password)
    result = client.create_project(name=project_name,
                                   description=description,
                                   project_type=project_type,
                                   resourcetype=resource_type)
    print("-" * 100)
    print("Project id:", result['id'])
    print("Project name:", result['name'])
    print("-" * 100)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="creating project")
    parser.add_argument("-pn", "--project_name", type=str, help="name of project")
    parser.add_argument("-de", "--description", type=str, default="", help="description of project")
    parser.add_argument("-pt", "--project_type", type=str, default="ImageCaptioning", help="type of project")
    parser.add_argument("-rt", "--resource_type", type=str, default="ImageCaptioningProject", help="type of resource")
    arg = parser.parse_args()
    create_project(**ADMIN_CONFIG,
                   project_name=arg.project_name,
                   description=arg.description,
                   project_type=arg.project_type,
                   resource_type=arg.resource_type)
