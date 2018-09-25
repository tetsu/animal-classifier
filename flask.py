import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from keras.models import load_model
from PIL import Image
import sys
import numpy as np
from config import env

classes = env.CLASSES
image_size = env.IMAGE_SIZE

UPLOAD_FOLDER = './images'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            model = load_model('./image_cnn.h5')
            image = Image.open(filepath)
            image = image.convert('RGB')
            image = image.resize((image_size, image_size))
            data = np.asarray(image)
            x = []
            x.append(data)
            x = np.array(x)
            result = model.predict([x])[0]
            predicted = result.argmax()
            percentage = int(result[predicted] * 100)
            return "Label: " + classes[predicted] + ", Percentage: " + str(percentage) + "%"

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
