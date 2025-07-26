import os
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from tensorflow.keras.models import load_model
import tensorflow as tf
from werkzeug.utils import secure_filename

Model = load_model("model/garbageClassification_model.keras")
class_labels = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

recycling_tips = {
    "cardboard": "Flatten boxes before recycling. Keep it dry and clean.",
    "glass": "Rinse bottles and jars. Remove caps and lids.",
    "metal": "Clean food containers. Aluminum cans are 100% recyclable.",
    "paper": "Avoid shredded paper. Don't recycle greasy food wrappers.",
    "plastic": "Recycle bottles and containers. Avoid soft plastics.",
    "trash": "This item goes in general waste. Try to reduce usage."
}

@app.route("/")
def home():
    return render_template("home.html",request=request)

@app.route("/about")
def about():
    return render_template("about.html",request=request)

@app.route("/detect", methods=["GET"])
def detect():
    return render_template("detect.html",request=request)

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return redirect(url_for("detect"))

    file = request.files["file"]
    if file.filename == "":
        return redirect(url_for("detect"))

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Preprocess and predict
    img = tf.keras.utils.load_img(filepath, target_size=(224, 224))
    img_array = tf.keras.utils.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = Model.predict(img_array)[0]

    predicted_class = class_labels[np.argmax(prediction)]
    confidence = round(float(np.max(prediction)) * 100, 2)
    category = "Biodegradable" if predicted_class in ['paper', 'cardboard'] else "Non-Biodegradable"
    tip = recycling_tips.get(predicted_class, "No tips available.")

    return render_template("detect.html",
                           label=predicted_class,
                           confidence=confidence,
                           category=category,
                           image_path=filename,
                           tip=tip,
                           probabilities=prediction.tolist(),
                           labels=class_labels)

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
