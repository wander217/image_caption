import json

data_path = r'./convert_data/text.json'
raw_data = json.loads(open(data_path, 'r', encoding='utf-8').read())
tag = {}
for i, item in enumerate(raw_data):
    if item not in tag:
        tag[item.capitalize()] = [i]
    else:
        tag[item.capitalize()].append(i)

save_path = r'./convert_data/rm_text.json'
with open(save_path, 'w', encoding='utf-8') as f:
    f.write(json.dumps(list(tag.keys()), indent=4))
