import os
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from collections import defaultdict

annotation_path = "E:/RS/BNVD/Dataset/ODS_New/labels"
file_list = os.listdir(annotation_path)
class_list = ["Bicycle", "Bus", "Bhotbhoti", "Car", "CNG", "Easybike", "Leguna", "Motorbike", "MPV", "Pedestrian", "Pickup", "PowerTiller", "Rickshaw", "ShoppingVan", "Truck", "Van", "Wheelbarrow"]

class_instance = defaultdict(int)

def annotation_counter(file):
    with open(file, 'r') as f:
        file_annotation_details = f.readlines()
        for line in file_annotation_details:
            class_element = int(line.split()[0])
            class_instance[class_element] += 1

for file_name in file_list:
    annotation_counter(os.path.join(annotation_path, file_name))

print(sum(class_instance.values()))
for class_index, class_name in enumerate(class_list):
    print(f"{class_name}: {class_instance[class_index]}")

figi = px.pie(values=list(class_instance.values()), names=class_list, title='Dataset Class Distribution')
figi.show()
