#!flask/bin/python
import os
from flask import Flask, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from solver import theGrid

UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/static/<path:path>', methods=['GET', 'POST'])
def send_js(path):
    if request.method=='POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('static/index.html')
    return send_from_directory('static', path)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
   if request.method == 'POST':
       file = request.files['file']
       extension = os.path.splitext(file.filename)[1]
       f_name = str(uuid.uuid4()) + extension
       file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
       return json.dumps({'filename':f_name})




@app.route('/sudoku/getSolved', methods=['GET'])
def get_tasks():
    return jsonify({'solved': theGrid})


if __name__ == '__main__':
    app.run(debug=True)
