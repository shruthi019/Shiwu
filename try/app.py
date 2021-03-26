
# A very simple Flask Hello World app for you to get started with...

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello from Flask!'

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

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/crop")
def crop_suggestion():
    return render_template("afterUpload.html")
#app.run()