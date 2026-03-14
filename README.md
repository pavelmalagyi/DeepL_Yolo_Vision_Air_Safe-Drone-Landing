# DeepL_Yolo_Vision_Air_Safe-Drone-Landing
Projet de détection de zone d'atterrissage pour drone avec YOLO

# 🚁 Safe Drone Landing with YOLO

Ce dépôt contient le code source de notre projet de détection de zone d'atterrissage pour drone, réalisé par Pavel MALAGYI et Antoine MAMETZ.

## 📂 Contenu du dépôt et Livrables
* 📜 **Code d'entraînement :** `Training_Notebook.ipynb` (Script Google Colab utilisé pour le Transfer Learning, la comparaison des modèles YOLOv8n, YOLO11s, YOLO26n, et l'algorithme de calcul de nos seuils de sécurité).
* 💻 **Code de démo en direct :** `yolo_detect.py` (Script Python pour l'inférence en temps réel à la webcam, intégrant notre politique de décision Safe/Not Safe) basée sur les seuils calculés.
* 📦 **Dataset :** (https://drive.google.com/drive/folders/1Zd7nkHyQ1AbAWaJiCMI0R0talLy9hk6W?usp=sharing) (Dossier contenant notre dataset annoté au format YOLO).
* 🎬 **Modèle (Poids) et Vidéo de Démonstration :** (https://drive.google.com/drive/folders/1oXfyNY9P7-ScRctgHGVJr6dCyWaKWoEc?usp=sharing) (Notre fichier de poids final `best.pt` de tous les modèles entrainés et démo live de 2-3 minutes validant notre politique de décision sur les 8 scénarios imposés).

## 🚀 Utilisation de la démo en direct
Pour lancer la détection en temps réel avec le modèle entraîné dans la console Anaconda Prompt ou PowerShell (nécessite d'avoir placé le fichier `best.pt` dans le même dossier de ce code) :
```bash
python yolo_detect.py --model best.pt --source usb0 --resolution 1280x720
