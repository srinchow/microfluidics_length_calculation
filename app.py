from flask import Flask, render_template, redirect, url_for, request
import os
from Microfluidics_Length import *

UPLOAD_FOLDER = "./images"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def hello():
    return "hello"


@app.route("/upload", methods=["POST"])
def upload_file():
    file1 = request.files["file"]
    path = os.path.join(app.config["UPLOAD_FOLDER"], file1.filename)
    print(path)
    file1.save(path)
    result = action(file1.filename)
    print(result)
    return str(result)


if __name__ == "__main__":
    app.run(debug=True)
