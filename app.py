from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
from pathlib import Path

from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

def model_predict(img_path):
    """
       model_predict will return the preprocessed image
    """
   
    img = open_image(img_path)
    pred_class,pred_idx,outputs = learn.predict(img)
    return pred_class

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('uploadCrop.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path)
        return preds
    return None

if __name__ == '__main__':
    
    app.run()
    