# Python standard libraries
import json
import os

# Third party libraries
from flask import Flask, render_template, redirect, request, url_for
import requests


# Flask app setup
app = Flask(__name__)




@app.route("/")
def index():
    return render_template("sample-page.html")

@app.route("/presentacion")
def presentacion():
    return render_template("index.html")




if __name__ == "__main__":
    app.run(ssl_context="adhoc")
