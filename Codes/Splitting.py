import os
import random
from shutil import copy2
from glob import glob
from collections import defaultdict

base_path = r'C:\Users\Lenovo\Desktop\Project\output'
combined_img_dir = os.path.join(base_path, 'images')
combined_lbl_dir = os.path.join(base_path, 'labels')

train_img_dir = os.path.join(base_path, 'train', 'images')
train_lbl_dir = os.path.join(base_path, 'train', 'labels')
val_img_dir = os.path.join(base_path, 'val', 'images')
val_lbl_dir = os.path.join(base_path, 'val', 'labels')


os.makedirs(train_img_dir, exist_ok=True)
os.makedirs(train_lbl_dir, exist_ok=True)
os.makedirs(val_img_dir, exist_ok=True)
os.makedirs(val_lbl_dir, exist_ok=True)

val_split = 0.2  

def get_class_from_label(label_file):
    with open(label_file, 'r') as f:
        classes = set([line.split()[0] for line in f.readlines()])
    return classes

class_to_images = defaultdict(list)
image_paths = glob(os.path.join(combined_img_dir, '*.jpg'))

for img_path in image_paths:
    img_name = os.path.basename(img_path)
    lbl_path = os.path.join(combined_lbl_dir, img_name.replace('.jpg', '.txt'))
    if os.path.exists(lbl_path):
        classes = get_class_from_label(lbl_path)
        for cls in classes:
            class_to_images[cls].append((img_path, lbl_path))

train_images = []
val_images = []

for cls, images in class_to_images.items():
    random.shuffle(images)
    split_idx = int(len(images) * val_split)
    val_images.extend(images[:split_idx])
    train_images.extend(images[split_idx:])

def move_files(image_label_pairs, dest_img_dir, dest_lbl_dir):
    for img_path, lbl_path in image_label_pairs:
        img_name = os.path.basename(img_path)
        lbl_name = os.path.basename(lbl_path)
        
        copy2(img_path, os.path.join(dest_img_dir, img_name))

        copy2(lbl_path, os.path.join(dest_lbl_dir, lbl_name))

move_files(train_images, train_img_dir, train_lbl_dir)
move_files(val_images, val_img_dir, val_lbl_dir)

print("Stratified dataset split completed!")
