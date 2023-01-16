from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_code():

    if os.path.isfile("prog.txt"):
        os.remove("prog.txt")
    file = request.files['file']
    file.save("prog.txt")
    try:
        output = subprocess.check_output(["g++", "converter.cpp","-o","converter"])
        output = subprocess.check_output(["./converter"])
    except subprocess.CalledProcessError as e:
        output = e.output
    # read the contents of the output.txt file
    with open("output.txt", "r") as f:
        pseudocode = f.read()
    
    
    return render_template('index.html', pseudocode=pseudocode)


if __name__ == '__main__':
    app.run(debug=True)
