import os
import time
from PIL import Image

image_path = "C:/Users/ASUS/OneDrive/Desktop/ShopRobot/Phase 2/images/Superstar"
image_list = os.listdir(image_path)
cropped_path = "C:/Users/ASUS/OneDrive/Desktop/ShopRobot/Phase 2/images/Superstar/Cropped"
#print(image_list)

def image_cropper(img):
    img = Image.open(img)
    box = (200,200,1800,1180)
    img = img.crop(box)
    return img

for x in image_list:
    image = image_cropper(os.path.join(image_path,x))
    image.save(os.path.join(cropped_path,x))
    print(x)
    #time.sleep(5)
