from flask import Flask
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "u dont know"
UPLOAD_FOLDER = 'static\\uploads'
BLUR_FOLDER = 'static\\blurred_images'
app.config['UPLOAD_FOLDER'] = os.path.join(UPLOAD_FOLDER)
app.config['BLUR_FOLDER'] = os.path.join(BLUR_FOLDER)