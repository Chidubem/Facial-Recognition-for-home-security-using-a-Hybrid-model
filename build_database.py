import face_recognition
import os
import pickle

DATABASE_PATH = "model/database.pkl"
IMAGE_DIR = "dataset"

known_faces = []

# for file in os.listdir(IMAGE_DIR):
#     path = os.path.join(IMAGE_DIR, file)
#     img = face_recognition.load_image_file(path)
#     encodings = face_recognition.face_encodings(img)

#     if encodings:
#         name = os.path.splitext(file)[0]
#         known_faces.append({
#             "name": name,
#             "encoding": encodings[0]
#         })
for file in os.listdir(IMAGE_DIR):
    if not file.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue  # Skip non-image files like .DS_Store

    path = os.path.join(IMAGE_DIR, file)
    img = face_recognition.load_image_file(path)
    encodings = face_recognition.face_encodings(img)

    if encodings:
        name = os.path.splitext(file)[0]
        known_faces.append({
            "name": name,
            "encoding": encodings[0]
        })

os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)

with open(DATABASE_PATH, "wb") as f:
    pickle.dump(known_faces, f)

print(f"Saved {len(known_faces)} face encodings to {DATABASE_PATH}")
