#!/usr/bin/env python3
from flask import Flask, render_template, request
from election import Election
import json


def init():
    """Initializes required data"""
    global config
    global election

    config = {}
    with open("config.json") as f:
        config = json.load(f)

    election = Election(config["candidates"], config["multiple"])


# Initialize data
init()
# Initialize app
app = Flask(__name__)


def password_is_valid(password: str):
    return password in config["passwords"]


def remove_password(password: str):
    config["passwords"].remove(password)


@app.route("/")
def index():
    return render_template("index.html", candidates=config["candidates"], multiple=config["multiple"])


@app.route("/vote", methods=["POST"])
def vote():
    data = request.form
    password = data.get("password")

    # Was the vote successful?
    success = False
    # Check password validity
    if password_is_valid(password):
        candidates = data.getlist("candidate")
        # Try to vote for the selected candidates
        success = election.vote(candidates)

    if success:
        # If voting was successful, disable the password and write the new results
        remove_password(password)
        election.write_json("votes.json")
        return render_template("success.html")
    else:
        return render_template("error.html")
