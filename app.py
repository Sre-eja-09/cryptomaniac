from flask import Flask, request, render_template, jsonify
import pickle
import requests
import pandas as pd
from patsy import dmatrices
from chat import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/predictions")
def prediction():
    return render_template('prediction.html')

@app.route("/blogs")
def blogs():
    return render_template('blogs.html')

@app.get("/support")
def index_get():
    return render_template("support2.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: CHECK IF TEXT IS VALID
    response = get_response(text)
    message = {"answer":response}
    return jsonify(message)

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)