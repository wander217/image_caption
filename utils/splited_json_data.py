import json
import os

root = r'F:\project\data\image_caption\image'
json_root = r'F:\project\python\image_caption\utils\splited_data'
save_path = r'F:\project\data\image_caption\target'

for folder in os.listdir(root):
    folder_path = os.path.join(root, folder)
    save_folder_path = os.path.join(save_path, folder)

    if not os.path.isdir(save_folder_path):
        os.mkdir(save_folder_path)
    for item in os.listdir(folder_path):
        item_name = item.split(".")[0]
        try:
            data = json.loads(open(os.path.join(json_root, "{}.json".format(item_name)), 'r', encoding='utf-8').read())

            with open(os.path.join(save_folder_path, "{}.json".format(item_name)), 'w', encoding='utf-8') as f:
                f.write(json.dumps(data, indent=4))
        except Exception as e:
            print(e)

# with open("./file.json", 'w', encoding='utf-8') as f:
#     f.write(json.dumps(file_name, indent=4))
