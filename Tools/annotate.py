from cProfile import label
import cv2
import os

on_action = 3
face_list = ["bus","car","pickup","truck"]

images = "images"
labels = "labels"
new_ds_dir_img = "C:/Users/ASUS/OneDrive/Desktop/5_VeRi/VeRi/image_val/"
new_ds_dir_label = "C:/Users/ASUS/OneDrive/Desktop/5_VeRi/VeRi/labels"
print(face_list[on_action])

x = os.listdir(os.path.join(new_ds_dir_img,face_list[on_action]))
#print(x)
annotation = str(on_action) + " 0.5" + " 0.5" + " 1.0" +" 1.0"
#print(annotation)
z=0

for i in x:
    img_path = os.path.join(new_ds_dir_img,face_list[on_action],i)
    txt = str(i).replace(".jpg",".txt")
    label_path = os.path.join(new_ds_dir_label,face_list[on_action],txt) 
    with open(label_path,'w+') as f:
        f.write(annotation)

    z=z+1

print(z)