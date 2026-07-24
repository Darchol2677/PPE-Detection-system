from ultralytics import YOLO

# Load  trained model
model = YOLO("models/best.pt")   

# Detect objects in an image
results = model("test.jpg")

# Show result
results[0].show()

# Save result
results[0].save(filename="output/result.jpg")



#acurrany or model marirx

model = YOLO("models/best.pt")

metrics = model.val(
    data="Dataset/data.yaml"   # <-- Path to your data.yaml
)

print("mAP50:", metrics.box.map50)
print("mAP50-95:", metrics.box.map)
print("Precision:", metrics.box.mp)
print("Recall:", metrics.box.mr)