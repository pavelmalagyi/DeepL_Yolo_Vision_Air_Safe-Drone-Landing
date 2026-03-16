import os
from PIL import Image
import pillow_heif

# Ça permet à Python de comprendre le format HEIC d'Apple
pillow_heif.register_heif_opener()

# --- CONFIGURATION ---
dossier_source = r"E:\user\source" # Mets ici le chemin de ton dossier source avec les images HEIC
dossier_destination = r"E:\user\destination" # Mets ici le chemin de ton dossier de destination pour les JPG redimensionnés
taille_max = (1000, 1000)

# Liste des extensions que tu veux traiter
extensions_valides = (".jpg", ".jpeg", ".png", ".webp", ".heic")

# Créer le dossier de destination s'il n'existe pas!
os.makedirs(dossier_destination, exist_ok=True)

compteur = 0

print(f" Début de la conversion pour l'équipe VisionAir...")

for fichier in os.listdir(dossier_source):
    if fichier.lower().endswith(extensions_valides):
        chemin_complet = os.path.join(dossier_source, fichier)
        
        try:
            # 1. Ouvrir l'image HEIC
            img = Image.open(chemin_complet)

            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            elif img.mode == "RGBA":
                # Optionnel : mettre un fond blanc au lieu de noir pour la transparence
                background = Image.new("RGB", img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[3])
                img = background
            else:
                img = img.convert("RGB")
            # 2. Réduire la taille en gardant les proportions (aspect ratio)
            img.thumbnail(taille_max)
            
            # 3. Préparer le nouveau nom de fichier (.jpg au lieu de .heic)
            nom_sans_extension = os.path.splitext(fichier)[0]
            nouveau_nom = f"{nom_sans_extension}.jpg"
            chemin_sauvegarde = os.path.join(dossier_destination, nouveau_nom)
            
            # 4. Sauvegarder en JPG avec une bonne qualité
            img.save(chemin_sauvegarde, format="JPEG", quality=85)
            compteur += 1
            print(f"✅ {fichier} -> {nouveau_nom} (réduite)")
            
        except Exception as e:
            print(f" Erreur avec {fichier} : {e}")

print(f"\nTerminé ! {compteur} images ont été redimensionnées et converties en JPG dans le dossier '{dossier_destination}'.")