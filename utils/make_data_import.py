import json
import os

data = []
root = r'F:\project\data\image_caption\image\part_0'
for file in os.listdir(root):
    item_data = json.loads(open(os.path.join(root, file), 'r', encoding='utf-16').read())
    text = []
    for region in item_data['regions']:
        text.append(region['phrase'])
    data.append({
        "image_path": item_data['id'],
        "texts": text
    })
save_path = r"F:\project\data\image_caption\texts\part_0.json"
with open(save_path, 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, indent=4))
