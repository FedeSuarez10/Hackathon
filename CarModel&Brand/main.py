import os
import cv2
import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
# Charger un modèle pré-entraîné (par exemple, ResNet)
model = models.resnet50(pretrained=True)
model.eval()  # Mettre le modèle en mode évaluation
# Transformations pour les images
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Redimensionner à 224x224
    transforms.ToTensor(),  # Convertir en tensor
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normalisation
])
# Chemin de la vidéo
video_path = os.path.join('..', 'Backend', 'uploads', '2-Jeu_Test_J2-10h30_P5.mp4')
def predict_brand_and_model(frame):
    # Convertir le frame (image) OpenCV en image PIL
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    # Appliquer les transformations
    image_tensor = transform(image).unsqueeze(0)  # Ajouter une dimension pour le batch
    # Effectuer une prédiction
    with torch.no_grad():
        outputs = model(image_tensor)
        _, predicted = outputs.max(1)  # Obtenir l'index de la classe prédite
        return predicted.item()  # Retourner l'index de la classe prédite
def process_video():
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Erreur lors de l'ouverture de la vidéo")
        return
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Prédire la marque et le modèle de la voiture
        prediction = predict_brand_and_model(frame)
        print(f"Prédiction : {prediction}")
        # Afficher chaque frame avec la prédiction
        cv2.putText(frame, f"Prediction: {prediction}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('Frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    process_video()