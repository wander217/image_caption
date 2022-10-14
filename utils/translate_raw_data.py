import json

data_path = r'./raw_data/region_descriptions.json'
raw_data = json.loads(open(data_path, 'r', encoding='utf-8').read())
trans_path = r'./convert_data/trans.json'
trans_data = json.loads(open(trans_path, 'r', encoding='utf-8').read())
for item in raw_data:
    for region in item['regions']:
        txt = region['phrase']
        trans = trans_data.get(txt.capitalize(), '')
        region['phrase'] = trans

for item in raw_data:
    with open("./splited_data/{}.json".format(item['id']), 'w') as f:
        f.write(json.dumps(item, indent=4))
