import os
from glob import glob

old_class_to_new = {
    0: 0,  # person
    3: 1,  # motorcycle
    2: 2,  # car
    7: 3   # truck
}

base_path = 'C:\\Users\\Lenovo\\Desktop\\Project\\output'
label_path = os.path.join(base_path, 'train/labels')
val_label_path = os.path.join(base_path, 'val/labels')

def remap_labels(label_folder):
    label_files = glob(os.path.join(label_folder, '*.txt'))
    for lbl_file in label_files:
        with open(lbl_file, 'r') as file:
            lines = file.readlines()
        
        with open(lbl_file, 'w') as file:
            for line in lines:
                parts = line.split()
                old_class = int(parts[0])
                new_class = old_class_to_new.get(old_class, old_class)
                file.write(f"{new_class} {' '.join(parts[1:])}\n")

remap_labels(label_path)
remap_labels(val_label_path)

print("Class indices remapped successfully!")
