from __future__ import annotations
import os

annotations_path = "C:/Users/ASUS/Downloads/Compressed/Object-Detection-20221024T082730Z-001/Object-Detection/Yolo-Labels/val/"
image_path = "C:/Users/ASUS/Downloads/Compressed/Object-Detection-20221024T082730Z-001/Object-Detection/Images/val/"

all_annotations = os.listdir(annotations_path)
all_annotations.sort()
all_images = os.listdir(image_path)
all_images.sort()
#print(all_annotations)
#print(all_images)

index = 0

for x in all_annotations:
    annotation_name = x.replace(".txt", "")
    try:
        image_name = all_images[index].replace(".jpg","")
    except Exception as e:
        print(index)

    if annotation_name == image_name:
        pass
    else:
        print(annotation_name)
        print(image_name)

"""
print(all_annotations[1499])
print(all_annotations[1500])
print(all_annotations[1501])
print(all_annotations[1502])
print(all_annotations[1503])
print(all_annotations[1504])
print(all_annotations[1505])
print(all_annotations[1506])
print(all_annotations[1507])
print(all_annotations[1508])
"""