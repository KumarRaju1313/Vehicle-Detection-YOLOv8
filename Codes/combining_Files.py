import os
from shutil import copy2
from glob import glob

base_path = r'C:\Users\Lenovo\Desktop\Project\output'
categories = ['car', 'motorcycle', 'person', 'truck']

combined_img_dir = os.path.join(base_path, 'images')
combined_lbl_dir = os.path.join(base_path, 'labels')
os.makedirs(combined_img_dir, exist_ok=True)
os.makedirs(combined_lbl_dir, exist_ok=True)

def combine_files(category):
    img_folder = os.path.join(base_path, category, 'images')
    lbl_folder = os.path.join(base_path, category, 'labels')

    img_paths = glob(os.path.join(img_folder, '*.jpg'))  

    for img_path in img_paths:
        img_name = os.path.basename(img_path)
        lbl_name = img_name.replace('.jpg', '.txt')  

        copy2(img_path, os.path.join(combined_img_dir, img_name))

        lbl_path = os.path.join(lbl_folder, lbl_name)
        if os.path.exists(lbl_path):
            copy2(lbl_path, os.path.join(combined_lbl_dir, lbl_name))

if __name__ == "__main__":

    for category in categories:
        combine_files(category)

    print("Files combined successfully!")
