import os
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
annotation_path = "C:/Users/ASUS/OneDrive/Desktop/Sample/somapo/"
file_list = os.listdir(annotation_path)

class_list = ["Bicycle", "Bus", "Bhotbhoti", "Car", "CNG", "Easybike", "Leguna", "Motorbike", "MPV", "Pedestrian", "Pickup", "PowerTiller", "Rickshaw", "ShoppingVan", "Truck", "Van", "Wheelbarrow"]
class_instance = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]




def annotation_counter(filename):
    with open(file_name,'r') as f:
        file_information = str(f.read())
        file_annotation_details = file_information.split("\n")
        for element in file_annotation_details:
            class_element = element.split(" ")
            class_element = int(class_element[0])
            class_instance[class_element] = class_instance[class_element] + 1
        
    return class_instance

for x in file_list:
    file_name = os.path.join(annotation_path, x)
    informations = annotation_counter(file_name)
    
for class_name in range(0, len(class_list)):
    print(str(class_list[class_name]), ": ",str(informations[class_name]))


print(sum(informations))
"""
colors = ['red', 'darkorange', 'lime', 'royalblue', 'plum', 'tomato',
            'greenyellow', 'teal', 'indigo', 'peru', 'aqua', 'springgreen',
            'crimson', 'lightcoral', 'gold', 'palegreen', 'moccasin']


fig = plt.figure(figsize = (15, 5))
plt.pie(informations, labels= class_list, colors=colors, 
        radius=1.2, center=(4,4), startangle=90)
plt.legend()
plt.show()
"""
figi = px.pie(values=informations, names = class_list, title='Dataset Class Distribution')
figi.show()