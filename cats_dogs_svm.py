import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

#settings for small ram
IMG_SIZE = 64
MAX_IMAGES = 300

#Load Dataset Function
def load_data(data_dir):
    X = []
    y = []

    categories = ["Cat", "Dog"]

    for category in categories:
        path = os.path.join(data_dir, category)
        label = categories.index(category)

        count = 0

        for img in os.listdir(path):
            if count >= MAX_IMAGES:
                break

            try:
                img_path = os.path.join(path, img)
                image = cv2.imread(img_path)

                if image is None:
                    continue

                image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
                image = image.flatten() / 255.0

                X.append(image)
                y.append(label)

                count += 1

            except:
                pass

    return np.array(X), np.array(y)

#load data
print("Loading dataset...")

X, y = load_data(".")
print("Dataset shape:", X.shape)

#split data
print("Splitting data...")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#train model
print("Training SVM model...")

model = SVC(kernel="rbf", C=10, gamma='scale')
model.fit(X_train, y_train)

#test model
print("Testing model...")

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy * 100, "%")

#save model
print("Saving model...")
joblib.dump(model, "svm_model.pkl")
print("Model saved as svm_model.pkl")

#prediction
def predict_image(img_path):
    img = cv2.imread(img_path)

    if img is None:
        print("Invalid image")
        return

    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img.flatten().reshape(1, -1)

    prediction = model.predict(img)

    if prediction[0] == 0:
        print("Prediction: CAT 🐱")
    else:
        print("Prediction: DOG 🐶")

#testing prediction
predict_image("Cat/20.jpg")