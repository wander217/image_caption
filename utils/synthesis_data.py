import json
import os

root = r'C:\Users\admin\Downloads\results (1)'
save_path = r'F:\project\python\image_caption\utils\convert_data\trans.json'
data = json.loads(open(save_path, 'r', encoding='utf-8').read())
for file in os.listdir(root):
    file_path = os.path.join(root, file)
    item_data = json.loads(open(file_path, 'r', encoding='utf-8').read())
    for k, v in item_data.items():
        if v is not None:
            data[k] = v

new_data = {}
for k, v in data.items():
    if k != v:
        new_data[k.capitalize()] = v.capitalize()
save_path = r'F:\project\python\image_caption\utils\convert_data\trans.json'
with open(save_path, 'w', encoding='utf-8') as f:
    print(len(new_data))
    f.write(json.dumps(new_data, indent=4))
