from ultralytics import YOLO
import argparse
import os
import cv2

def model_defn(act_model_path):
    act_model = YOLO(act_model_path)
    print("Model loaded successfully")
    return act_model

def detect_video(act_model, video_src, dest_path):
    cap = cv2.VideoCapture(video_src)
    
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_src}")
        return
    
    process_output_dir = os.path.join(dest_path, "motorcycle") # Class name
    os.makedirs(process_output_dir, exist_ok=True)

    fr_cnt = 0
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * 1) 

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if fr_cnt % frame_interval == 0:
            results = act_model.predict(frame, conf=0.40, save_crop=False)
            save_frame_and_labels(results, frame, fr_cnt, process_output_dir)

        fr_cnt += 1

    cap.release()
    print("Video processing completed.")

def save_frame_and_labels(results, frame, frame_number, save_dir):
    boxes_info = [] 

    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls.item()) 
            
            if cls_id == 3: # Class ID
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist()) 
                
                img_h, img_w, _ = frame.shape
                x_center = (x1 + x2) / 2 / img_w
                y_center = (y1 + y2) / 2 / img_h
                w_norm = (x2 - x1) / img_w
                h_norm = (y2 - y1) / img_h
                box_info = f"{cls_id} {x_center:.6f} {y_center:.6f} {w_norm:.6f} {h_norm:.6f}"
                boxes_info.append(box_info)

    if boxes_info:  
        frame_filename = os.path.join(save_dir, "bike1_"f"{frame_number}.jpg")
        cv2.imwrite(frame_filename, frame)

        label_filename = os.path.join(save_dir, "bike1_"+f"{frame_number}.txt")
        with open(label_filename, 'w') as f:
            f.write("\n".join(boxes_info))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--source_paths', nargs='+', type=str, required=False) 
    parser.add_argument('--dest_path', type=str, required=True)
    parser.add_argument('--act_model_path', type=str, default="yolov8n.pt", required=False)

    args = parser.parse_args()

    if not os.path.exists(args.dest_path):
        os.makedirs(args.dest_path)

    act_model = model_defn(args.act_model_path)
    detect_video(act_model, "bike_vid2.mkv", args.dest_path)
