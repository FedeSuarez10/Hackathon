import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
# Charger un modèle pré-entraîné
model = models.resnet50(pretrained=True)
model.eval()  # Mode évaluation
# Transformations d'image
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
def predict(image_path):
    image = Image.open(image_path)
    image_tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        outputs = model(image_tensor)
        _, predicted = outputs.max(1)
        return predicted.item()  # Retourner l'index de la classe prédite