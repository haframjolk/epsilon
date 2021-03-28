#!/usr/bin/env python3
from flask import Flask, render_template, request
import json


def init():
    """Initializes required data"""
    global config
    global votes

    config = {}
    with open("config.json") as f:
        config = json.load(f)

    votes = {candidate: 0 for candidate in config["candidates"]}
    votes["empty"] = 0


# Initialize data
init()
# Initialize app
app = Flask(__name__)


def write_json():
    """Writes current vote tally to JSON file"""
    with open("votes.json", "w") as f:
        json.dump(votes, f)


def vote_for(candidate: str):
    """Vote for a single candidate"""
    votes[candidate] += 1


def candidate_exists(candidate: str):
    """Returns True if candidate exists, False otherwise"""
    return candidate in votes


def vote_for_candidates(candidates: list[str]):
    """Vote for multiple candidates. Returns True if successful, False otherwise"""
    # If candidates are not selected, register empty vote
    if not candidates:
        empty_vote()
        return True
    # If all candidates exist, vote for every one
    if all(candidate_exists(candidate) for candidate in candidates):
        for candidate in candidates:
            vote_for(candidate)
        return True
    return False


def remove_password(password: str):
    config["passwords"].remove(password)


def empty_vote():
    votes["empty"] += 1


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
    if password in config["passwords"]:
        candidates = [data.get("candidate")]
        # Only get the form list if the election allows multiple choice, to prevent voters from voting multiple times
        if config["multiple"]:
            candidates = data.getlist("candidate")
        # Try to vote for the candidates
        success = vote_for_candidates(candidates)
    if success:
        # If voting was successful, disable the password and write the new results
        remove_password(password)
        write_json()
        return render_template("success.html")
    else:
        return render_template("error.html")
