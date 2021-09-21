from flask import render_template, request, url_for,flash, redirect
import os
from app import app
from werkzeug.utils import secure_filename
import cv2


ALLOWED_EXTENSIONS = ['jpg','png', 'jpeg']

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/upload_image', methods=['POST','GET'])
def upload_image():
    if request.method=='POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
            img = cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
            blurImg = cv2.blur(img,(10,10))
            cv2.imwrite((os.path.join(app.config['BLUR_FOLDER'], secure_filename(file.filename))),blurImg)
            return render_template("display.html", filename=file.filename)
        else:
            flash("Check your file extension. Allowed extensions are {jpg,png,jpeg}")
            return render_template('upload.html')


if __name__=='__main__':
    app.run(debug=True,host='localhost',port='5000')
