import json
import os

root = r'F:\project\data\image_caption\image'
json_root = r'F:\project\python\image_caption\utils\splited_data'
save_path = r'F:\project\data\image_caption\target'

for folder in os.listdir(root):
    folder_path = os.path.join(root, folder)
    new_data  = []
    for item in os.listdir(folder_path):
        item_name = item.split(".")[0]
        try:
            data = json.loads(open(os.path.join(json_root, "{}.json".format(item_name)), 'r', encoding='utf-8').read())
            text = []
            for region in data['regions']:
                text.append(region['raw'])
                text.append(region['trans'])
            new_data.append({
                "name": item_name,
                "texts": text
            })
        except Exception as e:
            print(e)
    save_path = r'F:\project\data\image_caption\texts'
    with open(os.path.join(save_path, "{}.json".format(folder)), 'w', encoding='utf-8') as f:
        f.write(json.dumps(new_data, indent=4))
