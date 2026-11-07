import os
import random

from flask import Flask, jsonify, render_template, request, session

import Words

app = Flask(__name__)
# On Render, set SECRET_KEY as an environment variable. The fallback is for local use only.
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-change-me")

MAX_LIVES = 6

# Lowercase, dedupe, and keep real words only (the original list had "I", "Android", etc.)
WORDS = sorted({w.lower() for w in Words.words if w.isalpha() and len(w) >= 3})


def new_game():
    session["word"] = random.choice(WORDS)
    session["guessed"] = []
    session["lives"] = MAX_LIVES
    session["message"] = "Pick a letter to start."


def status_of(word, guessed, lives):
    if all(ch in guessed for ch in word):
        return "won"
    return "lost" if lives <= 0 else "playing"


def payload():
    if "word" not in session:
        new_game()
    word, guessed, lives = session["word"], session["guessed"], session["lives"]
    status = status_of(word, guessed, lives)
    return {
        "letters": [ch if ch in guessed else "" for ch in word],
        "wrong": [g for g in guessed if g not in word],
        "guessed": guessed,
        "lives": lives,
        "maxLives": MAX_LIVES,
        "status": status,
        "word": word if status != "playing" else None,
        "message": session.get("message", ""),
    }


@app.after_request
def no_cache_api(resp):
    if request.path.startswith("/api/"):
        resp.headers["Cache-Control"] = "no-store"
    return resp


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/state")
def api_state():
    return jsonify(payload())


@app.post("/api/guess")
def api_guess():
    data = payload()  # makes sure a game exists
    if data["status"] == "playing":
        letter = str((request.get_json(silent=True) or {}).get("letter", "")).strip().lower()
        word, guessed, lives = session["word"], list(session["guessed"]), session["lives"]
        if len(letter) != 1 or not letter.isalpha():
            msg = "Type a single letter from A to Z."
        elif letter in guessed:
            msg = f"You already tried {letter.upper()}."
        else:
            guessed.append(letter)
            if letter in word:
                msg = f"Nice! {letter.upper()} is in the word."
            else:
                lives -= 1
                msg = f"No {letter.upper()} here."
        session["guessed"], session["lives"], session["message"] = guessed, lives, msg
    return jsonify(payload())


@app.post("/api/new")
def api_new():
    new_game()
    return jsonify(payload())


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
