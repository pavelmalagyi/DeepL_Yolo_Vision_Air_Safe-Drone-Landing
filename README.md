# DeepL_Yolo_Vision_Air_Safe-Drone-Landing
Projet de détection de zone d'atterrissage pour drone avec YOLO

Ce dépôt contient le code source de notre projet de détection de zone d'atterrissage pour drone, réalisé par Pavel MALAGYI et Antoine MAMETZ.

## 📊 Processus de collecte des données (Data Collection)
Pour ce projet, nous avons conçu deux cibles personnalisées asymétriques basées sur des marqueurs fiduciels (ArUco / AprilTag) afin de maximiser l'extraction de caractéristiques par le modèle.
* **Captation :** Ces cibles ont été imprimées sur des papiers de différentes couleurs et photographiées sous de multiples angles, distances et conditions lumineuses (intérieur et extérieur).
* **Negative Samples :** Des scènes vierges (sans cibles) et des leurres ont été intégrés pour apprendre au modèle à ne rien détecter et réduire les faux positifs.
* **Prétraitement & Annotation :** Les images ont été redimensionnées/compressées via un script (Pillow/HEIF) puis annotées manuellement au format YOLO (*tight bounding boxes*) à l'aide de Label Studio.

## 📂 Contenu du dépôt et Livrables
* 📜 **Code d'entraînement :** `Training_Notebook.ipynb` (Script Colab pour le Transfer Learning, la comparaison des modèles YOLOv8n, YOLO11s, YOLO26n, et le calcul des seuils de sécurité).
* 💻 **Code de démo en direct :** `yolo_detect.py` (Script Python pour l'inférence en temps réel à la webcam, intégrant la politique de décision SAFE/NOT SAFE).
* 📦 **Dataset :** [Lien Google Drive du Dataset](https://drive.google.com/drive/folders/1Zd7nkHyQ1AbAWaJiwanathCMI0R0talLy9hk6W?usp=sharing) (Dossier contenant notre dataset annoté au format YOLO).
* 🎬 **Modèles & Vidéos :** [Lien Google Drive des Poids et Démo](https://drive.google.com/drive/folders/1oXfyNY9P7-ScRctgHGVJr6dCyWaKWoEc?usp=sharing) (Fichier `best.pt` final et vidéos d'inférence live validant les scénarios imposés).

---

## ⚙️ Installation "From Scratch" (Environnement Local)
Pour exécuter ce projet en local avec accélération GPU, suivez ces instructions. Nous recommandons l'utilisation d'Anaconda ou Miniconda.

**1. Création et activation de l'environnement virtuel :**
```bash
conda create --name VisionAir-env python=3.11 -y
conda activate VisionAir-env
```

**2. Installation des dépendances (PyTorch avec CUDA & Ultralytics) :**
Assurez-vous d'avoir installé les drivers NVIDIA à jour.
```bash
# Installation de PyTorch optimisé pour CUDA (ex: version 11.8)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
# Installation de YOLO et des outils annexes via le fichier requirements.txt
pip install -r requirements.txt
```

## 🚀 Reproductibilité : Entraînement et Inférence
** Reproduire l'entraînement (Training Pipeline) **
Vous pouvez reproduire notre entraînement de deux manières :

**Via Google Colab : Importez le fichier Training_Notebook.ipynb dans Colab, modifiez le chemin vers le fichier data.yaml de notre dataset, et exécutez les cellules.**
** Via le terminal en local (CLI) : Une fois l'environnement installé et le dataset téléchargé, lancez la commande suivante : **
```bash
yolo task=detect mode=train model=yolov8n.pt data=chemin/vers/data.yaml epochs=50 imgsz=640 batch=16
```

** Utilisation de la démo en direct (Live Inference) **

Pour lancer la détection en temps réel avec le modèle entraîné dans la console Anaconda Prompt ou PowerShell (nécessite d'avoir placé le fichier `best.pt` dans le même dossier de ce code) :
```bash
python yolo_detect.py --model best.pt --source usb0 --resolution 1280x720
```
(Note : pour utiliser un flux vidéo YouTube en direct comme source, utilisez yt-dlp : yt-dlp -g <lien_youtube> et placez l'URL générée dans l'argument --source).
