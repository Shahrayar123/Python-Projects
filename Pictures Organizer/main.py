""" Symple code for organizing pictures based on the number of faces"""
import argparse
import glob
import os

import cv2

parser = argparse.ArgumentParser()
parser.add_argument("path", help="Folder with images")
parser.add_argument("extension", help="Valid image extension (.png, .jpg, .jpeg)")
args = parser.parse_args()

current_path = os.getcwd()

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

imagens = glob.glob(f"{args.path}*.{args.extension}")
n_folders = 0
total_images = len(imagens)

for j, img_path in enumerate(imagens):
    img = cv2.imread(img_path)
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    n_faces = len(faces)
    if n_faces>0:
        folder = f"{n_faces}_face"
        dest_path = os.path.join(args.path,folder)
        try:
            os.mkdir(dest_path)
            n_folders+=1
        except:
            pass
        os.system(f"mv {img_path} {dest_path}")
    print (f"Done: {j}/{total_images}", end='\r')

print (f"Nº of folders created: {n_folders}")