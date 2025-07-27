# 🌿 EcoSort - Smart Waste Classification using Deep Learning

**EcoSort** is a deep learning–powered web application that classifies waste into specific **material types** (like plastic, paper, metal, etc.) and further maps them into **Biodegradable** or **Non-Biodegradable** categories. Built with **Flask** and **Bootstrap**, it provides a simple and intuitive interface to promote responsible waste disposal and sustainability.

![EcoSort Demo](https://via.placeholder.com/1000x300?text=EcoSort+Waste+Classifier)

---

## 🔗 Live Demo

👉 [Click here to try EcoSort live](https://ecosort.onrender.com)  
_🚀 Hosted on Render_

---

## 🧠 Model Overview

- ✅ **Accuracy**: ~94% on test data
- 🧱 **Architecture**: MobileNetV2 (Transfer Learning)
- 📐 **Input Size**: 224x224 RGB
- ⚙️ **Framework**: TensorFlow / Keras
- 📊 **Loss Function**: Categorical Crossentropy
- 🧪 **Optimizer**: Adam
- 📁 **Dataset**: [Garbage Classification Dataset on Kaggle](https://www.kaggle.com/datasets/mostafaabla/garbage-classification/data)

---

## 🗂 Waste Classes

The model is trained on the following 6 classes:

- **Plastic**
- **Glass**
- **Metal**
- **Paper**
- **Organic**
- **Other**

These are then mapped to the **eco-category**:

| Waste Type | Category             |
|------------|----------------------|
| Plastic    | Non-Biodegradable    |
| Glass      | Non-Biodegradable    |
| Metal      | Non-Biodegradable    |
| Paper      | Biodegradable        |
| Organic    | Biodegradable        |
| Other      | Unknown / Mixed      |

---

## 🚀 Features

- 🧠 Predicts the waste material type from images
- 🌱 Indicates if the item is biodegradable or not
- 🖼️ Simple image upload interface
- 📊 Displays confidence score of prediction
- 📱 Mobile responsive layout (Bootstrap 5)
- 🔥 Live Deployment on Render

---

## 💻 Tech Stack

| Layer       | Technology                  |
|-------------|------------------------------|
| Frontend    | HTML, CSS, Bootstrap 5       |
| Backend     | Python, Flask                |
| Model       | MobileNetV2 (Keras, TensorFlow) |
| Deployment  | Render.com                   |

---

## 📁 Project Structure

