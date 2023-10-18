import os

file_path = "C:/Users/ASUS/OneDrive/Desktop/VehicleDSTest/"

files = os.listdir(file_path)
counter = 1
format = ".jpg"
for file in files:
    file_name = str(counter) + format
    os.rename((os.path.join(file_path,file)), (os.path.join(file_path, file_name)))
    counter = counter + 1