# ♻️ EcoSort - Smart Waste Classification using Deep Learning

**EcoSort** is a web-based deep learning app that classifies waste images into **material-based categories** like plastic, paper, metal, etc.  
It intelligently maps each to **Biodegradable** or **Non-Biodegradable**, and offers useful **recycling tips** to promote sustainability.  
Powered by a **MobileNetV2** model with **~94%** validation accuracy, EcoSort helps users make informed, eco-friendly decisions in real time.

---

## 🔗 Live Demo

👉 [Try EcoSort Now (Deployed on Render)](https://ecosort-1dzm.onrender.com)  
_🚀 Hosted live with integrated Flask backend and trained model_

---

## 🧠 Model Overview

- **Accuracy**: ~94% on validation data
- **Architecture**: MobileNetV2 (Transfer Learning)
- **Input Shape**: 224×224 RGB
- **Framework**: TensorFlow / Keras
- **Loss Function**: Categorical Crossentropy
- **Optimizer**: Adam
- **Dataset Used**: [Garbage Classification - Kaggle](https://www.kaggle.com/datasets/mostafaabla/garbage-classification/data)

---

## Classes & Categories

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

