# 🫀 CardioPulse AI - Heart Disease Risk Level Predictor

CardioPulse AI is a Deep Learning-based web application designed to predict a patient's heart disease risk level using clinical health parameters. Built with TensorFlow/Keras and Flask, this tool offers an intuitive interface for real-time risk assessment.

---

## 📸 User Interface Preview

#### Input Form
![Patient Details Form](./webapp/images/patient_details.png)

---

#### Prediction Results
![Results View](./webapp/images/patient_results.png)

---

## ✨ Features

- **Deep Learning Model**: Uses a Feedforward Neural Network (FFNN) built with Keras & TensorFlow for regression predictions.
- **Model Checkpointing**: Automatically saves the best-performing model based on validation loss (`val_loss`).
- **Feature Preprocessing**: Scales input features and target values using Scikit-Learn's `MinMaxScaler`.
- **Modern Web Interface**: Clean Glassmorphism UI built with HTML5, CSS3, and Flask.

---

## 📊 Clinical Input Features

The model uses 7 key clinical features to estimate heart disease risk:
1. **Gender**
2. **Age**
3. **Total Cholesterol (TC)**
4. **HDL Cholesterol**
5. **Smoking Status**
6. **Blood Pressure Medication**
7. **Diabetes Status**

---

## 🛠 Tech Stack

- **Machine Learning / Deep Learning**: Python, TensorFlow / Keras, Scikit-Learn, Pandas, NumPy
- **Backend Framework**: Flask
- **Frontend**: HTML5, CSS3 (Glassmorphism UI)
- **Tools**: Jupyter Notebook, VS Code

---

