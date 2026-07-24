# 🦺 PPE Detection System using YOLO

An AI-powered Personal Protective Equipment (PPE) Detection System built using the YOLO object detection model. The system detects whether workers are wearing the required safety equipment in real time from images, videos, or a webcam.

---

## 📌 Features

- Real-time PPE detection
- Detects multiple people in a frame
- Supports image, video, and webcam input
- Fast object detection using YOLO
- Bounding boxes with confidence scores
- Easy to extend with additional PPE classes

---

## 🛠️ Tech Stack

- Python
- YOLO (Ultralytics)
- OpenCV
- NumPy
- PyTorch

---

## 📂 Dataset

Dataset Source:

https://universe.roboflow.com/sphar/ppe-detection-p2kug/dataset/4

Classes:

- Helmet
- No Helmet
- Vest
- No Vest
- Safety Shoe
- Person

---

## 📁 Project Structure

PPE-Detection-System/
│
├── detect.py
├── train.py
├── predict.py
├── data.yaml
├── requirements.txt
├── README.md
├── screenshots/
└── outputs/

---

## 📦 Pre-trained Model

This repository includes a pre-trained YOLO model (`best.pt`) located in the `models/` directory.

The model has already been trained on the PPE Detection dataset.

If you only want to perform detection, **you do not need to train the model again**.

Simply run one of the following:

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/ppe-detection-system.git
```

Move into the project folder:

```bash
cd ppe-detection-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

```bash
python train.py
```

---

## ▶️ Run Detection

Image:

```bash
python detect.py
```

Video:

```bash
python detect.py --source video.mp4
```

Webcam:

```bash
python detect.py --source 0
```

---

## 📊 Model Performance

| Metric | Value |
|---------|-------|
| mAP@0.5 | 87.48372%|
| Precision | 90.66115% |
| Recall | 81.1415% |



---

## 📷 Results

Add screenshots inside the `screenshots/` folder and display them here using Markdown image links after uploading them to GitHub.

---

## 🔮 Future Improvements

- PPE violation alerts
- Email notifications
- Web dashboard
- Attendance integration
- Cloud deployment
- Multi-camera support

---

## 👨‍💻 Author

**Yash Satyawan Pawar**

Diploma in Computer Engineering

Interested in:

- Artificial Intelligence
- Computer Vision
- Deep Learning
- Python Development

---

## ⭐ If you found this project useful, consider giving it a star.