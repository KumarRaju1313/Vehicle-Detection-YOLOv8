import cv2
import time
import csv
from ultralytics import YOLO

model = YOLO('ObjDect/TrainedModels/yolov8_train/weights/best_openvino_model/')

input_video_path = 'Videos Downloaded/sample1.mp4'
output_video_path = 'Videos Downloaded/ovsample.mp4'

cap = cv2.VideoCapture(input_video_path)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

start = time.time()

accuracy_scores = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    results = model.predict(frame)
    
    confidences = [box.conf for box in results[0].boxes]  
    accuracy = sum(confidences) / len(confidences) if confidences else 0
    accuracy_scores.append(accuracy)
  
    annotated_frame = results[0].plot()
    
    out.write(annotated_frame)

cap.release()
out.release()

end = time.time()
timetaken = end - start

print(f"Time taken: {timetaken} seconds")

results_list = [timetaken, accuracy_scores]

csv_file_path = 'ovsample.csv'
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Time Taken (seconds)', 'Frame Accuracies'])
    writer.writerow(results_list)

print(f"Results saved to {csv_file_path}")
