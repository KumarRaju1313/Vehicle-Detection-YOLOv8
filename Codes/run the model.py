# from ultralytics import YOLO

# model = YOLO('C:/Users/Lenovo/Desktop/Project/ObjDect/TrainedModels/yolov8_train/weights/last.pt')

# results = model.train(
#     data='C:/Users/Lenovo/Desktop/Project/ObjDect/data.yaml',
#     epochs=25,           
#     imgsz=640,          
#     batch=32,            
#     project='C:/Users/Lenovo/Desktop/Project/ObjDect/TrainedModels',
#     name='yolov8_train', 
#     resume=True      
# )



import cv2
import time
from ultralytics import YOLO

model = YOLO('ObjDect/TrainedModels/yolov8_train/weights/best.pt')

input_video_path = r'C:\Users\Lenovo\Desktop\Project\Videos Downloaded\output_video5.mp4'
output_video_path = 'Videos Downloaded/ptsam01.mp4'

cap = cv2.VideoCapture(input_video_path)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

start = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model.predict(frame)
    annotated_frame = results[0].plot()
    out.write(annotated_frame)

end = time.time()

timetaken = end-start
print(f"Time taken: {timetaken / 60:.2f} minutes ")

cap.release()
out.release()
cv2.destroyAllWindows()


