from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model = YOLO("ObjDect/TrainedModels/yolov8_train/weights/best.pt")

model.export(format="onnx")