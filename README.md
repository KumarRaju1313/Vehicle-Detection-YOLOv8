# 🚗 Vehicle Detection using YOLOv8

A machine learning project to detect and classify vehicles in video streams using **YOLOv8**, including dataset preprocessing, model training, ONNX/OpenVINO exports, and real-time inference.

## 🧠 Key Features

✅ Full YOLOv8 training and inference pipeline  
✅ Dataset preparation, augmentation, and class correction  
✅ Real-time object detection in videos with annotation  
✅ Frame-level confidence scoring and CSV logging  
✅ Exports to ONNX and OpenVINO for efficient deployment

## 📁 Project Structure

```
.
├── Code/
│   ├── Augmentation.py              # Image augmentation functions
│   ├── Download_youtube_video.py    # Download video data
│   ├── Inference_for_class.py       # Run inference by class
│   ├── Splitting.py                 # Split data into train/val
│   ├── Training.py                  # YOLOv8 model training script
│   ├── changing_class_nos.py        # Remap class numbers
│   ├── combining_Files.py           # Merge files for dataset
│   └── run_the_model.py             # Main runner for YOLOv8 pipeline
├── CNN Object Detection.ipynb       # Colab-compatible training + inference notebook
├── data.yaml                        # YOLOv8 data config (paths + class info)
├── onnx_export.py                   # Export model to ONNX
├── openvino_export.py               # Export model to OpenVINO format
├── run1.py                          # Run inference and save annotated video
└── README.md                        # Project documentation
```

## 🗂 Dataset Structure

```
dataset/
├── images/
│   ├── train/
│   └── val/
├── labels/
│   ├── train/
│   └── val/
└── data.yaml
```

### Example `data.yaml`:

```yaml
train: C:/path/to/train/images
val: C:/path/to/val/images
nc: 4
names: ['person', 'motorcycle', 'car', 'truck']
```

## 🚀 How to Run

### 1️⃣ Install Requirements

```bash
pip install ultralytics opencv-python tqdm pillow numpy
```

Or install via requirements.txt:

```bash
pip install -r requirements.txt
```

### 2️⃣ Train the Model

```python
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
model.train(data='path/to/data.yaml', epochs=50, imgsz=640)
```

### 3️⃣ Validate the Model

```python
model.val(data='path/to/data.yaml', model='path/to/best.pt')
```

### 4️⃣ Export the Model

```python
# Export to ONNX
model.export(format="onnx")

# Export to OpenVINO
model.export(format="openvino")
```

### 5️⃣ Run Inference on Video

```bash
python run1.py
```

- Annotated video will be saved (e.g., `output_video.mp4`)
- Frame-wise accuracy (confidence) will be logged into `results.csv`

## 🎯 Model Evaluation

- **mAP50-95**: Evaluated using YOLOv8 `.val()` method
- **Precision / Recall**: Tracked during training
- **Accuracy Logging**: CSV output via OpenVINO inference

## 🧪 Sample Outputs

⚠️ **Note**: Outputs are not included in this repo.

Running the pipeline will generate:
- Annotated video (e.g., `output_video.mp4`)
- Frame-wise accuracy report (`results.csv`)

## 📊 Results Example

| Model Format | Speed (FPS) | Accuracy (avg) |
|--------------|-------------|----------------|
| YOLOv8n      | 35 FPS      | ~82%          |
| OpenVINO     | 50 FPS      | ~80–85%       |

*Note: Results may vary depending on system specs and dataset.*

## 📦 Dependencies

- `ultralytics`
- `opencv-python`
- `tqdm`
- `pillow`
- `numpy`

Install all with:

```bash
pip install -r requirements.txt
```

## 📌 Notes

- Works in both local and Google Colab environments
- Ensure correct paths in your `data.yaml` file
- You can export and deploy the best model in multiple formats

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) for the amazing YOLO implementation
- OpenVINO toolkit for model optimization
- The open-source community for various tools and libraries used
