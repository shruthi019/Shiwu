#from flask_ngrok import run_with_ngrok
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
#run_with_ngrok(app)   #starts ngrok when the app is run

model_path = "soilClassify.h5"
SoilNet = load_model(model_path)

def predict_model(img_path, model):
    img = load_img(img_path, target_size=(224, 224))
    img = img_to_array(img)
    img = img / 255
    img = np.expand_dims(img, axis = 0)

    result = np.argmax(model.predict(img))
#    prediction = classes[result]
    return result
    if (result == 0):
        return render_template("alluvialSoil.html")
    elif (result == 1):
        return render_template("blackSoil.html")
    elif result == 2:
        return render_template("claySoil.html")
    elif result == 3:
        return render_template("redSoil.html")
    else:
        return "An error occurred"

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        uploadedImg = request.files["image"]
        nameUploadedImg = uploadedImg.filename
        print("You have uploaded ", nameUploadedImg)

        uploadedImg_path = os.path.join('static/uploaded_by_user', nameUploadedImg)
        uploadedImg.save(uploadedImg_path)

        print("Predicting.....")
        result = predict_model(uploadedImg_path, SoilNet)
        
        if (result == 0):
            return render_template("alluvialSoil.html")
        elif (result == 1):
            return render_template("blackSoil.html")
        elif result == 2:
            return render_template("claySoil.html")
        elif result == 3:
            return render_template("redSoil.html")
        else:
            return "An error occurred"

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/intuition")
def intuition():
    return render_template("intuition.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/uploadCrop")
def uploadCrop():
    return render_template("uploadCrop.html")

@app.route("/uploadSoil")
def uploadSoil():
    return render_template("uploadSoil.html")

@app.route("/crop")
def crop_suggestion():
    return render_template("afterUploadCrop.html")

@app.route("/soil")
def soil_suggestion():
    return render_template("afterUploadSoil.html")
#app.run()
