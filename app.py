#!flask/bin/python
import os
from flask import Flask, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from solver import theGrid

UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

solved = [
    {
        "0": {
            "1": "3",
            "2": "1",
            "3": "6",
            "4": "5",
            "5": "7",
            "6": "8",
            "7": "4",
            "8": "9",
            "9": "2"
        },
        "1": {
            "1": "5",
            "2": "2",
            "3": "9",
            "4": "1",
            "5": "3",
            "6": "4",
            "7": "7",
            "8": "6",
            "9": "8"
        }
    }
]


@app.route('/doris')
def doris():
    return '''
    <!doctype html>
    <div id='root'></div>
    <script src="./main.js"></script>
    '''


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
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
            return redirect(url_for('upload_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


@app.route('/sudoku/getSolved', methods=['GET'])
def get_tasks():
    return jsonify({'solved': theGrid})


if __name__ == '__main__':
    app.run(debug=True)
