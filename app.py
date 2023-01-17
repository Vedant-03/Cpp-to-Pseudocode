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
        result = subprocess.run(['python', 'convrt.py', 'prog.txt'], capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        return "Error: {}\n{}".format(e.returncode, e.output)
    # read the contents of the output.txt file
    try:
        with open("/home/agrawalvedant03/mysite/output.txt", "r") as f:
            pseudocode = f.read()
    except IOError as e:
        return "Error: {}".format(e)
    return render_template('index.html', pseudocode=pseudocode)


if __name__ == '__main__':
    app.run(debug=True)
