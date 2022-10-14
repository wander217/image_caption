import json

text_path = r'./convert_data/rm_text.json'
raw_data = json.loads(open(text_path, 'r', encoding='utf-8').read())
trans_path = r'./convert_data/trans.json'
trans_data = json.loads(open(trans_path, 'r', encoding='utf-8').read())

new_data = []
for item in raw_data:
    if item.capitalize() not in trans_data:
        new_data.append(item)

part_num = 1
data_len = len(new_data)
part_len = data_len // part_num
split_data = []
for i in range(part_num):
    split_data.append(new_data[i * part_len:min([(i + 1) * part_len, data_len])])
for i in range(part_num):
    save_path = r'./convert_data/un_trans_{}.json'.format(i)
    with open(save_path, 'w', encoding='utf-8') as f:
        print(len(split_data[i]))
        f.write(json.dumps(split_data[i], indent=4))
