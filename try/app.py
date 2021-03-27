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

alluvialsoil_desc = """Alluvial soils support more than 40% of India's population by providing the most productive agricultural lands. The soil is porous because of its loamy nature. The proportion of potash, phosphoric acid and alkalies are adequate in alluvial soils. 
Crops: rice, wheat, sugarcane, tobacco, cotton, jute, maize, oilseeds, vegetables and fruits"""

blacksoil_desc = """Black soils when seen in uplands are considered to be present with low fertility while those in the valleys are very fertile. The black colour arises due to the presence of a small proportion of titaniferous magnetite or iron and black constituents of the parent rock. 
Crops: cotton (best suited), wheat, jowar, linseed, Virginia, tobacco, castor, sunflower, millets"""

claysoil_desc = """Clay soil has a smooth texture because of its small particle size. It feels sticky and rolls like plasticine when wet. The clay soil swells when wetted and shrink when dried, so a certain amount of restructuring can take place in these soils depending on weather conditions. Because of its density, the clay soil retains moisture well. 
Crops: paddy (best), vegetables, fruits"""

redsoil_desc = """Red soils originate from parent rocks which are crystalline and metamorphic in nature like acid granites, gneisses and quartzites. On the uplands, the red soils are poor, gravelly and porous but in the lower areas, they are rich, deep dark and fertile. The red color is due to the presence of iron oxide. 
Crops: cotton, wheat, rice, pulses, millets, tobacco, oil seeds, potatoes and fruits"""


def predict_model(img_path, model):
    img = load_img(img_path, target_size=(224, 224))
    img = img_to_array(img)
    img = img / 255
    img = np.expand_dims(img, axis = 0)

    result = np.argmax(model.predict(img))
    return result

@app.route("/predictSoil", methods=["GET", "POST"])
def predictSoil():
    if request.method == "POST":
        uploadedImg = request.files["image"]
        nameUploadedImg = uploadedImg.filename
        print("You have uploaded ", nameUploadedImg)

        uploadedImg_path = os.path.join('static/uploaded_by_user', nameUploadedImg)
        uploadedImg.save(uploadedImg_path)

        print("Predicting soil.....")
        result = predict_model(uploadedImg_path, SoilNet)
        
        if (result == 0):
            return render_template("afterUploadSoil.html", soil_type='Alluvial', user_image_path=uploadedImg_path, desc=alluvialsoil_desc)
        elif (result == 1):
            return render_template("afterUploadSoil.html", soil_type='Black', user_image_path=uploadedImg_path, desc=blacksoil_desc)
        elif result == 2:
            return render_template("afterUploadSoil.html", soil_type='Clay', user_image_path=uploadedImg_path, desc=claysoil_desc)
        elif result == 3:
            return render_template("afterUploadSoil.html", soil_type='Red', user_image_path=uploadedImg_path, desc=redsoil_desc)
        return "An error occurred"
    return render_template("uploadSoil.html")

@app.route("/predictCrop", methods=["GET", "POST"])
def predictCrop():
    if request.method == "POST":
        uploadedImg = request.files["image"]
        nameUploadedImg = uploadedImg.filename
        print("You have uploaded ", nameUploadedImg)

        uploadedImg_path = os.path.join('static/uploaded_by_user', nameUploadedImg)
        uploadedImg.save(uploadedImg_path)

        print("Predicting crop.....")
        result = predict_model(uploadedImg_path, SoilNet)
        
        if (result == 0):
            return render_template("alluvialCrop.html")
        elif (result == 1):
            return render_template("blackCrop.html")
        elif result == 2:
            return render_template("clayCrop.html")
        elif result == 3:
            return render_template("redCrop.html")
        return "An error occurred"
    return render_template("uploadCrop.html")

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

#@app.route("/crop")
#def crop_suggestion():
#    return render_template("afterUploadCrop.html")

#@app.route("/soil")
#def soil_suggestion():
#   return render_template("afterUploadSoil.html")
#app.run()
