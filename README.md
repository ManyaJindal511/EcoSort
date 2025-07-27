# 🌿 EcoSort - Smart Waste Classification using Deep Learning

**EcoSort** is a web-based deep learning app that classifies waste images into **material-based classes** like plastic, paper, metal, etc. It also provides eco-awareness by labeling waste as **Biodegradable** or **Non-Biodegradable** and offers **recycling tips** to help users make environmentally responsible decisions.

![EcoSort Banner](https://via.placeholder.com/1000x300?text=EcoSort+Waste+Classifier)

---

## 🔗 Live Demo

👉 [Click to Try EcoSort]([https://ecosort.onrender.com](https://ecosort-1dzm.onrender.com/))  
_🚀 Hosted on Render_

---

## 🧠 Model Overview

- ✅ **Accuracy**: ~94% on validation data
- 🧱 **Architecture**: MobileNetV2 (Transfer Learning)
- 📐 **Input Shape**: 224×224 RGB
- ⚙️ **Framework**: TensorFlow / Keras
- 📊 **Loss Function**: Categorical Crossentropy
- 🧪 **Optimizer**: Adam
- 📁 **Dataset Used**: [Garbage Classification - Kaggle](https://www.kaggle.com/datasets/mostafaabla/garbage-classification/data)

---

## ♻️ Classes & Categories

The model is trained to classify into the following **6 material-based classes**:

| Predicted Class | Eco Category         | Recycling Tip |
|-----------------|----------------------|---------------|
| `cardboard`     | Biodegradable        | Flatten boxes before recycling. Keep it dry and clean. |
| `glass`         | Non-Biodegradable    | Rinse bottles and jars. Remove caps and lids. |
| `metal`         | Non-Biodegradable    | Clean food containers. Aluminum cans are 100% recyclable. |
| `paper`         | Biodegradable        | Avoid shredded paper. Don't recycle greasy food wrappers. |
| `plastic`       | Non-Biodegradable    | Recycle bottles and containers. Avoid soft plastics. |
| `trash`         | Non-Biodegradable    | This item goes in general waste. Try to reduce usage. |

---

## 🖥️ Tech Stack

| Layer       | Technology                  |
|-------------|------------------------------|
| Frontend    | HTML, CSS, Bootstrap 5       |
| Backend     | Python, Flask                |
| Model       | MobileNetV2 (Keras + TensorFlow) |
| Deployment  | Render.com                   |

---

## 📁 Project Structure

