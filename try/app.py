
#from flask_ngrok import run_with_ngrok
from flask import Flask, render_template
#from tensorflow.keras.models import load_model
#from tensorflow.keras.preprocessing.image import load_img, img_to_array
#import numpy as np
#from werkzeug.utils import secure_filename

app = Flask(__name__)
#run_with_ngrok(app)   #starts ngrok when the app is run

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