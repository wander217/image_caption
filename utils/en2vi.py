import json
import os
from googletrans import Translator
from threading import Thread


def do_translate(data: list, idx: int):
    save_path = r'./convert_data'
    save_path = os.path.join(save_path, "trans_{}.json".format(idx))
    translator = Translator()

    new_data = {}
    count = 0
    while True:
        try:
            trans = translator.translate(data[count], src="en", dest='vi')
            new_data[data[count]] = trans.text
            count += 1
            if count % 100 == 0:
                print(idx, len(new_data))
                print(trans.text)
                open(save_path, 'w', encoding='utf-8').write(json.dumps(new_data, indent=4))
        except Exception as e:
            print(e)
        finally:
            if count > len(data):
                break


if __name__ == "__main__":
    data_path = r'./convert_data/un_trans_0.json'
    raw_data = json.loads(open(data_path, 'r', encoding='utf-8').read())
    thread_num = 1
    tag = {}
    for i, item in enumerate(raw_data):
        if item not in tag:
            tag[item] = [i]
        else:
            tag[item].append(i)
    data_len = len(tag.keys())
    part_len = data_len // thread_num
    split_data = []
    tag_key = list(tag.keys())
    for i in range(thread_num):
        split_data.append(tag_key[i * part_len:min([(i + 1) * part_len, data_len])])

    threads = []
    for i in range(thread_num):
        tmp = Thread(target=do_translate, args=[split_data[i], i])
        threads.append(tmp)

    for i in range(thread_num):
        threads[i].start()

    for i in range(thread_num):
        threads[i].join()
