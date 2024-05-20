import os
from natsort import natsorted

def get_filenames_without_extension(folder):
    filenames = []
    for filename in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, filename)):
            filenames.append(os.path.splitext(filename)[0])
    return filenames

def find_unpaired_files(image_folder, text_folder):
    image_filenames = natsorted(get_filenames_without_extension(image_folder))
    text_filenames = natsorted(get_filenames_without_extension(text_folder))

    unpaired_images = [filename for filename in image_filenames if filename not in text_filenames]
    unpaired_texts = [filename for filename in text_filenames if filename not in image_filenames]

    empty_text_files = []
    for filename in text_filenames:
        file_path = os.path.join(text_folder, filename + ".txt")
        if os.path.getsize(file_path) == 0:
            empty_text_files.append(filename)

    return unpaired_images, unpaired_texts, empty_text_files

if __name__ == "__main__":
    image_folder = "E:/RS/BNVD/ExtractedImageFiles/RAINY/images"
    text_folder = "E:/RS/BNVD/ExtractedImageFiles/RAINY/labels"

    unpaired_images, unpaired_texts, empty_text_files = find_unpaired_files(image_folder, text_folder)

    print("Unpaired image files:")
    print(unpaired_images)

    print("\nUnpaired text files:")
    print(unpaired_texts)

    print("\nEmpty text files:")
    print(empty_text_files)
