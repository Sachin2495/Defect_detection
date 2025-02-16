import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torchvision import models

class DefectDetectionModel(nn.Module):
    def __init__(self):
        super(DefectDetectionModel, self).__init__()
        self.model = models.resnet50(pretrained=True)
        num_ftrs = self.model.fc.in_features
        self.model.fc = nn.Linear(num_ftrs, 2)  # Binary classification (defect or no defect)

    def forward(self, x):
        return self.model(x)

def load_model(model_path):
    model = DefectDetectionModel()
    model.load_state_dict(torch.load(model_path))
    model.eval()
    return model

def predict(model, image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
    image = transform(image).unsqueeze(0)
    outputs = model(image)
    _, predicted = torch.max(outputs, 1)
    return "Defect" if predicted.item() == 1 else "No Defect"
