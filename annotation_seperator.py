import os
import random
import shutil


annotation_path = "C:/Users/ASUS/OneDrive/Desktop/Sample/somapo"
annotation_file_list = os.listdir(annotation_path)
print(len(annotation_file_list))

classes = ["Bicycle", "Bus", "Bhotbhoti", "Car", "CNG", "Easybike", "Leguna", "Motorbike", "MPV", "Pedestrian", "Pickup", "PowerTiller", "Rickshaw", "ShoppingVan", "Truck", "Van", "Wheelbarrow"]

bicycle, bus, bhotbhoti, car, cng, easybike, leguna, motorbike, mpv, pedestrian, pickup, powertiller, rickshaw, shoppingvan, truck, van, wheelbarrow = ([] for i in range(17))

for x in annotation_file_list:
    with open(os.path.join(annotation_path,x)) as file:
        file_information = str(file.read())
        file_annotation_details = file_information.split("\n")
        for element in file_annotation_details:
            class_element = element.split(" ")
            class_element = int(class_element[0])
            if class_element == 0:
                bicycle.append(x)
            elif class_element == 1:
                bus.append(x)
            elif class_element == 2:
                bhotbhoti.append(x)
            elif class_element == 3:
                car.append(x)
            elif class_element == 4:
                cng.append(x)
            elif class_element == 5:
                easybike.append(x)
            elif class_element == 6:
                leguna.append(x)
            elif class_element == 7:
                motorbike.append(x)
            elif class_element == 8:
                mpv.append(x)
            elif class_element == 9:
                pedestrian.append(x)
            elif class_element == 10:
                pickup.append(x)
            elif class_element == 11:
                powertiller.append(x)
            elif class_element == 12:
                rickshaw.append(x)
            elif class_element == 13:
                shoppingvan.append(x)
            elif class_element == 14:
                truck.append(x)
            elif class_element == 15:
                van.append(x)
            elif class_element == 16:
                wheelbarrow.append(x)
            
        pass
    pass

train_list = []
valid_list = []

isinstance_class_list_of_list = []
isinstance_class_list_of_list.extend([bicycle, bus, bhotbhoti, car, cng, easybike, leguna, motorbike, mpv, pedestrian, pickup, powertiller, rickshaw, shoppingvan, truck, van, wheelbarrow])

count_percentage = 0.07

valid_bicycle = random.sample(bicycle, int(len(bicycle)*count_percentage))
valid_bus = random.sample(bus, int(len(bus)*count_percentage))
valid_bhotbhoti = random.sample(bhotbhoti, int(len(bhotbhoti)*count_percentage))
valid_car = random.sample(car, int(len(car)*count_percentage))
valid_cng = random.sample(cng, int(len(cng)*count_percentage))
valid_easybike = random.sample(easybike, int(len(easybike)*count_percentage))
valid_leguna = random.sample(leguna, int(len(leguna)*count_percentage))
valid_motorbike = random.sample(motorbike, int(len(motorbike)*count_percentage))
valid_mpv = random.sample(mpv, int(len(mpv)*count_percentage))
valid_pedestrian = random.sample(pedestrian, int(len(pedestrian)*count_percentage))
valid_pickup = random.sample(pickup, int(len(pickup)*count_percentage))                
valid_powertiller = random.sample(powertiller, int(len(powertiller)*count_percentage))
valid_rickshaw = random.sample(rickshaw, int(len(rickshaw)*count_percentage))
valid_shoppingvan = random.sample(shoppingvan, int(len(shoppingvan)*count_percentage))
valid_truck = random.sample(truck, int(len(truck)*count_percentage))
valid_van = random.sample(van, int(len(van)*count_percentage))
valid_wheelbarrow = random.sample(wheelbarrow, int(len(wheelbarrow)*count_percentage))

valid_list = valid_bicycle + valid_bus + valid_bhotbhoti + valid_car + valid_cng + valid_easybike + valid_leguna + valid_motorbike + valid_mpv + valid_pedestrian + valid_pickup + valid_powertiller + valid_rickshaw + valid_shoppingvan + valid_truck + valid_van + valid_wheelbarrow
valid_list = list(dict.fromkeys(valid_list))
#print(valid_list)

# Validation Annotation Map

class_instance = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for filex in valid_list:
    with open(os.path.join(annotation_path,filex)) as file:
        file_information = str(file.read())
        file_annotation_details = file_information.split("\n")
        for element in file_annotation_details:
            class_element = element.split(" ")
            class_element = int(class_element[0])
            class_instance[class_element] = class_instance[class_element] + 1


print("Bicyle: ",(class_instance[0]/len(bicycle))*100)
print("Bus: ",(class_instance[1]/len(bus))*100)
print("Bhotbhoti: ",(class_instance[2]/len(bhotbhoti))*100)
print("Car: ",(class_instance[3]/len(car))*100)
print("CNG: ",(class_instance[4]/len(cng))*100)
print("Easybike: ",(class_instance[5]/len(easybike))*100)
print("Leguna: ",(class_instance[6]/len(leguna))*100)
print("Motorbike: ",(class_instance[7]/len(motorbike))*100)
print("MPV: ",(class_instance[8]/len(mpv))*100)
print("Pedestrian: ",(class_instance[9]/len(pedestrian))*100)
print("Pickup: ",(class_instance[10]/len(pickup))*100)
print("PowerTiller: ",(class_instance[11]/len(powertiller))*100)
print("Rickshaw: ",(class_instance[12]/len(rickshaw))*100)
print("ShoppingVan: ",(class_instance[13]/len(shoppingvan))*100)
print("Truck: ",(class_instance[14]/len(truck))*100)
print("Van: ",(class_instance[15]/len(van))*100)
print("Wheelbarrow: ",(class_instance[16]/len(wheelbarrow))*100)


image_original_path = "C:/Users/ASUS/OneDrive/Desktop/Sample/image2"
image_moved_file_path = "C:/Users/ASUS/OneDrive/Desktop/Sample/SemiSupervision/images"

label_original_path = "C:/Users/ASUS/OneDrive/Desktop/Sample/somapo"
label_moved_file_path = "C:/Users/ASUS/OneDrive/Desktop/Sample/SemiSupervision/labels"

folder = "train1"


for x in valid_list:
    shutil.move(os.path.join(label_original_path,x), os.path.join(label_moved_file_path, x))
    x = x.replace(".txt", ".jpg")
    shutil.move(os.path.join(image_original_path,x), os.path.join(image_moved_file_path, x))
    print("Moved", x)