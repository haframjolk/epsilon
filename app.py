#!/usr/bin/env python3
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", candidates=["Sóla", "Vallý"])


@app.route("/vote", methods=["POST"])
def vote():
    data = request.form
    if not data["password"]:
        return render_template("error.html")
    return render_template("success.html")
