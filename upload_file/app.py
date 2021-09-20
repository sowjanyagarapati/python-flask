from flask import Flask, render_template, request, url_for
import os
# from werkzeug import secure_filename


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'BlurImage\\uploads'
app.config['MAX_CONTENT_PATH'] = 5000
ALLOWED_EXTENSIONS = ['jpg','png']

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods=['POST','GET'])
def upload_file_():
    if request.method=='POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            file.save(file.filename)
            return "file uploaded"
        else:
            return "Check your file extension. Allowed extensions are {jpg,png}"

if __name__=='__main__':
    app.run(debug=True,host='localhost',port='5000')