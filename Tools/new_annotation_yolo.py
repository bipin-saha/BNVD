from __future__ import annotations
import os
import cv2
from decimal import Decimal, Context

annotation_path = "G:/Research/Vehicle DS/KITTI/training/label_2/"
images_path = "G:/Research/Vehicle DS/KITTI/training/image_2/"
new_annotation_path = "G:/Research/Vehicle DS/KITTI/training/NewAnnotations/"
annotations_list = os.listdir(annotation_path)
image_list = os.listdir(images_path)
x = annotations_list[0]
y = image_list[0]
#print(x)

float_point = Context(prec=10)

"""
img = cv2.imread(os.path.join(images_path,y))
dim = img.shape
print(dim[0], dim[1])
"""
"""
def yolo_annotator(annotation_name):
    with open(os.path.join(annotation_path, x), 'r') as file:
        stack_info = file.read()
        info = stack_info.split("\n")
        info.pop()
        for label in info:
            new_label = label.split()
            x_min = float_point.create_decimal(int(new_label[0])/1280)
            y_min = float_point.create_decimal(int(new_label[1])/720)
            x_max = float_point.create_decimal(int(new_label[2])/1280)
            y_max = float_point.create_decimal(int(new_label[3])/720)
            
            if x_min < 0:
                x_min = 0
            if x_max > 1:
                x_max = 1
            if y_min < 0:
                y_min = 0
            if y_max > 1:
                y_max = 1
            
            mid_x = (x_min + x_max)/2
            mid_y = (y_min + y_max)/2
            width_x = x_max - x_min
            width_y = y_max - y_min

            with open(os.path.join(new_annotation_path,x), 'a') as fox:
                var =str(new_label[4]) + " " + str(mid_x) + " " + str(mid_y) + " " + str(width_x) + " " + str(width_y)
                fox.write(var)
                fox.write("\n")
            print("YOLO Annotation Created", x)
"""
"""
for x in annotations_list:
    yolo_annotator(x)
"""

class_list = ['DontCare', 'Van', 'Tram', 'Cyclist', 'Person_sitting', 'Car', 'Pedestrian', 'Truck', 'Misc']
#yolo_annotator(x)

def kitti_annotator(annotation):
    with open(os.path.join(annotation_path, x), 'r') as file:
        stack_info = file.read()
        info = stack_info.split("\n")
        #print(info)
        info.pop()
        for label in info:
            new_label = label.split()
            #print(type(new_label[4]))
                
            x_min = float_point.create_decimal(float(new_label[4])/1242)
            y_min = float_point.create_decimal(float(new_label[5])/375)
            x_max = float_point.create_decimal(float(new_label[6])/1242)
            y_max = float_point.create_decimal(float(new_label[7])/375)
            
            if x_min < 0:
                x_min = 0
            if x_max > 1:
                x_max = 1
            if y_min < 0:
                y_min = 0
            if y_max > 1:
                y_max = 1
            
            mid_x = (x_min + x_max)/2
            mid_y = (y_min + y_max)/2
            width_x = x_max - x_min
            width_y = y_max - y_min

            if new_label[0] == "DontCare":
                class_id = "0"
            if new_label[0] == "Van":
                class_id = "1"
            if new_label[0] == "Tram":
                class_id = "2"
            if new_label[0] == "Cyclist":
                class_id = "3"
            if new_label[0] == "Person_sitting":
                class_id = "4"
            if new_label[0] == "Car":
                class_id = "5"
            if new_label[0] == "Pedestrian":
                class_id = "6"
            if new_label[0] == "Truck":
                class_id = "7"
            if new_label[0] == "Misc":
                class_id = "8"

            with open(os.path.join(new_annotation_path,x), 'a') as fox:
                var = class_id + " " + str(mid_x) + " " + str(mid_y) + " " + str(width_x) + " " + str(width_y)
                fox.write(var)
                fox.write("\n")
            print("YOLO Annotation Created", x)

for x in annotations_list:
    kitti_annotator(x)
