# Python standard libraries
import json
import os

# Third party libraries
from flask import Flask, render_template, redirect, url_for
import requests


# Flask app setup
app = Flask(__name__)




@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dataset")
def dataset():
    return render_template("dataset.html")

@app.route("/visualizacion")
def visualizacion():
    return render_template("visualization.html")

@app.route("/eda")
def eda():
    return render_template("eda.html")

@app.route("/machineLearning")
def machineLearning():
    return render_template("machine-learning.html")

@app.route("/resultados")
def resultados():
    return render_template("results.html")

@app.route("/sobre-nosotros")
def sobre_nosotros():
    return render_template("about-us.html")



if __name__ == "__main__":
    app.run(ssl_context="adhoc")
