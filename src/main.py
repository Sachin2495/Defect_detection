import os
import torch
from PIL import Image
from detection.defect_detection import load_model, predict

# Paths
model_path = '../models/defect_detection_model.pth'
image_path = '../data/notebooks/train_images/sample.jpg'

# Load model
model = load_model(model_path)

# Predict
if os.path.exists(image_path):
    image = Image.open(image_path)
    result = predict(model, image)
    print(f"Prediction: {result}")
else:
    print(f"Image not found: {image_path}")
