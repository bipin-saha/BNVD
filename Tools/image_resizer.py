import cv2
import time
import os
import imutils

original_img_path = "C:/Users/ASUS/OneDrive/Desktop/Vehicle DS/SemiSuper/296"
save_path = "C:/Users/ASUS/OneDrive/Desktop/OurDS/Phase5/images/"

img_list = os.listdir(original_img_path)
save_path_img_list = os.listdir(save_path)

counter = 13776
#counter = int((save_path_img_list[-1]).replace(".jpg","")) + 1
for img in os.listdir(original_img_path):
    frame = cv2.imread(os.path.join(original_img_path, img))
    resized = imutils.resize(frame, width=1280)

    file_name = str(counter) + ".jpg"    
    cv2.imwrite(os.path.join(save_path,file_name), resized)
    print("Saved : ", str(file_name))
    counter = counter + 1