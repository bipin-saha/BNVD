import os
import shutil

image_files = os.listdir("G:/Research/Vehicle DS/5_VeRi/VeRi.coco/images/train/")
label_files = os.listdir("G:/Research/Vehicle DS/5_VeRi/VeRi.coco/labels/train/")

image_original_path = "G:/Research/Vehicle DS/5_VeRi/VeRi.coco/images/train/"
image_moved_file_path = "G:/Research/Vehicle DS/5_VeRi/VeRi.coco/images/"

label_original_path = "G:/Research/Vehicle DS/5_VeRi/VeRi.coco/labels/train"
label_moved_file_path = "G:/Research/Vehicle DS/5_VeRi/VeRi.coco/labels/"

folder = "train1"


for x in range(5000):
    shutil.move(os.path.join(image_original_path,image_files[x]), os.path.join(image_moved_file_path, folder, image_files[x]))
    shutil.move(os.path.join(label_original_path,label_files[x]), os.path.join(label_moved_file_path, folder, label_files[x]))
    print("Moved", image_files[x])