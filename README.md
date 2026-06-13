# Cats vs Dogs Classification using SVM

## 📌 Overview

This project is part of my Machine Learning Internship at Prodigy Infotech.

The objective of this project is to build a machine learning model that can classify images of cats and dogs using the Support Vector Machine (SVM) algorithm.

The model uses image processing techniques to convert images into numerical features and then applies SVM for classification.

---

## 🎯 Objective

To implement a supervised machine learning model that classifies images into two categories:

- Cat 🐱
- Dog 🐶

The model is trained using labeled image data and evaluated using accuracy metrics.

---

## 📂 Dataset

Dataset Used: Custom Cats vs Dogs Image Dataset

Dataset Structure:
Cat/
Dog/

Dataset Details:

- Total Images Used: ~600 (limited for system performance)
- Image Size: Resized to 64 × 64 pixels
- Color Mode: RGB → Flattened / Feature Extracted

The dataset consists of cat and dog images organized into separate folders (Cat/ and Dog/). Due to dataset size limitations, the image dataset is not included in this repository.

---

## 🛠️ Technologies Used

- Python
- OpenCV
- NumPy
- Scikit-Learn
- Matplotlib (optional for visualization)
- Joblib (for model saving)

---

## ⚙️ Workflow

The project follows these steps:

1. Load image dataset from Cat and Dog folders
2. Resize images to a fixed size (64×64)
3. Convert images into numerical feature vectors
4. Split dataset into training and testing sets
5. Train Support Vector Machine (SVM) model
6. Evaluate model performance using accuracy score
7. Save trained model using Joblib
8. Test model on new images

---

## 🤖 Model Used

### Support Vector Machine (SVM)

SVM is a supervised machine learning algorithm used for classification tasks.

In this project:

- Kernel Used: Linear / RBF (based on implementation)
- Input: Image feature vectors
- Output: Binary classification (Cat or Dog)

---

## 📊 Results

The trained model successfully classifies images into Cat and Dog categories.

### Model Performance:

- Accuracy: ~50%–60% (depends on dataset and system constraints)

### Note:

The accuracy is limited due to:

- Small dataset size
- Use of basic feature extraction (flattened pixel values)
- Hardware constraints (4GB RAM system optimization)

---

## 💾 Model Saving

The trained model is saved using Joblib:
svm_model.pkl

This allows reuse of the trained model without retraining.

---

## 🧪 How to Run

### 1. Install Dependencies

```bash
pip install numpy opencv-python scikit-learn matplotlib joblib
```

### 2. Run the Project

```bash
python cats_dogs_svm.py
```

### 3. Predict on New Image

```bash
predict_image("image_location.jpg")
```

## 🏆 Internship Information

Task: Cats vs Dogs Image Classification using SVM
Internship: Prodigy Infotech Machine Learning Internship
Task Code: PRODIGY_ML_03

## 🚀 Key Learnings

Image preprocessing using OpenCV
Feature extraction from images
Supervised learning using SVM
Model evaluation techniques
Saving and loading ML models

## 👨‍💻 Author

Ashutosh Agrawal
B.Tech CSE Student
Government College of Engineering, Kalahandi

Machine Learning Enthusiast | Aspiring Software Engineer
