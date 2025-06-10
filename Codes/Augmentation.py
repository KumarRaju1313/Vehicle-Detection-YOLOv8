import os
import cv2
import albumentations as A
from glob import glob
from tqdm import tqdm

base_path = r'C:\Users\Lenovo\Desktop\Project\output'

augmentations = {
    "gray": A.Compose([A.ToGray(p=1.0)]),          
    "blur": A.Compose([A.Blur(blur_limit=7, p=1.0)])  
}

def augment_images(folder, category):
    image_paths = glob(os.path.join(folder, 'images', '*.jpg')) 
    label_paths = glob(os.path.join(folder, 'labels', '*.txt'))  

    for aug_type, aug_pipeline in augmentations.items():
        aug_img_dir = os.path.join(folder, f'{aug_type}_images')
        aug_lbl_dir = os.path.join(folder, f'{aug_type}_labels')
        os.makedirs(aug_img_dir, exist_ok=True)
        os.makedirs(aug_lbl_dir, exist_ok=True)

        for idx, img_path in enumerate(tqdm(image_paths, desc=f'Augmenting {category} with {aug_type}')):
            img = cv2.imread(img_path)
            img_name = os.path.basename(img_path)
            lbl_name = img_name.replace('.jpg', '.txt')

            lbl_path = os.path.join(folder, 'labels', lbl_name)
            if not os.path.exists(lbl_path):
                continue  

            augmented = aug_pipeline(image=img)
            aug_img = augmented['image']

            new_img_name = f"{img_name.replace('.jpg', '')}_{aug_type}_{idx}.jpg"
            new_lbl_name = new_img_name.replace('.jpg', '.txt')

            cv2.imwrite(os.path.join(aug_img_dir, new_img_name), aug_img)
            os.system(f'copy "{lbl_path}" "{os.path.join(aug_lbl_dir, new_lbl_name)}"')

if __name__ == "__main__":
    categories = ['car', 'motorcycle', 'truck', 'person']
    for category in categories:
        folder = os.path.join(base_path, category)
        augment_images(folder, category)
