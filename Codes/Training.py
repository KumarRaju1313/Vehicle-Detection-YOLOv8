import os
from ultralytics import YOLO

save_path = 'C:/Users/Lenovo/Desktop/Project/TrainedModels'
os.makedirs(save_path, exist_ok=True)

model = YOLO('yolov8n.pt')

results = model.train(
    data='C:/Users/Lenovo/Desktop/Project/data.yaml',
    epochs=25,
    imgsz=640,
    project=save_path,
    name='yolov8_training'
)

print("Training complete. Ssaved models at:", save_path)