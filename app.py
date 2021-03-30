#!/usr/bin/env python3

from flask import Flask, render_template, request
from election import Election
import json
import atexit


def init():
    """Initializes required data"""
    global config
    global election

    # Read config from file
    with open("config.json") as f:
        config = json.load(f)

    # Create Election object from config
    election = Election(config["candidates"], config["out_filename"], config["max_candidates"])


# Initialize data
init()
# Initialize app
app = Flask(__name__)


def password_is_valid(password: str):
    """Returns True if password is valid, False otherwise"""
    return password in config["passwords"]


def remove_password(password: str):
    """Removes password from the list of allowed passwords"""
    config["passwords"].remove(password)


@app.route("/")
def ballot():
    return render_template("ballot.html", title=config["title"], candidates=config["candidates"], max_candidates=config["max_candidates"])


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
        print("Vote received")
        # If voting was successful, disable the password and write the new results
        remove_password(password)
        return render_template("success.html")
    else:
        print("Voting attempt failed")
        return render_template("error.html")


def on_exit():
    """Exit handler"""
    print("Exit requested")
    print("Saving votes...")
    election.write_json()
    print(f"Votes saved to {config['out_filename']}")


# Save election results on exit
atexit.register(on_exit)
