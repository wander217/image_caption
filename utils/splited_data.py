import os
import cv2 as cv

root = r'F:\project\data\image_caption\coco\images\VG_100K'
part_num = 6
image_path = os.listdir(root)
data_len = len(image_path)
part_len = data_len // part_num
split_data = []
for i in range(part_num):
    split_data.append(image_path[i * part_len:min([(i + 1) * part_len, data_len])])

save_path = r'F:\project\data\image_caption\image'
for i in range(part_num):
    part_path = os.path.join(save_path, "part_{}".format(i))
    if not os.path.isdir(part_path):
        os.mkdir(part_path)
    for item in split_data[i]:
        try:
            image = cv.imread(os.path.join(root, item))
            cv.imwrite(os.path.join(part_path, item), image)
        except Exception as e:
            print(item)
