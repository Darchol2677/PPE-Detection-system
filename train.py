from ultralytics import YOLO

# Load the pretrained YOLOv11 Nano model
model = YOLO("yolo11n.pt")

# Train the model
results = model.train(
    data="Dataset/data.yaml",      # Path to dataset configuration
    epochs=50,                     # Number of complete passes through the dataset
    imgsz=640,                     # Resize images to 640x640
    batch=16,                      # Number of images processed at a time
    project="runs",                # Folder to save results
    name="ppe_detection",          # Name of this training run
    device="cpu"                   # Change to 0 if you have an NVIDIA GPU
)