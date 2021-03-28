#!/usr/bin/env python3
from flask import Flask, render_template, request
import json

app = Flask(__name__)

config = {}
with open("config.json") as f:
    config = json.load(f)

votes = {candidate: 0 for candidate in config["candidates"]}
votes["empty"] = 0


def write_json():
    with open("votes.json", "w") as f:
        json.dump(votes, f)


def vote_for(candidate):
    if candidate not in votes:
        return False
    else:
        votes[candidate] += 1
        write_json()
        return True


def empty_vote():
    votes["empty"] += 1

    write_json()


@app.route("/")
def index():
    return render_template("index.html", candidates=config["candidates"])


@app.route("/vote", methods=["POST"])
def vote():
    data = request.form
    password = data.get("password")
    success = False
    # Check password validity
    if password in config["passwords"]:
        candidate = data.get("candidate")

        # If no candidate was selected, register an empty vote
        if candidate is None:
            empty_vote()
            success = True
        # Else, try to vote for candidate
        elif vote_for(candidate):
            # If successful, remove password
            config["passwords"].remove(password)
            success = True
        else:
            # invalid candidate selected, return error
            pass
    if success:
        return render_template("success.html")
    else:
        return render_template("error.html")
