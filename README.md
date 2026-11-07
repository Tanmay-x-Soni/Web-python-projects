# Hangman Web Game

A browser-based Hangman game built with Python and Flask. Guess the hidden word one letter at a time before the hangman is fully drawn. You get 6 lives.

I first made this as a terminal game and then turned it into a web app so it can be played in the browser and deployed online.

**Live demo:** _add your Render link here_

## Features

- Play with the on-screen keyboard or your physical keyboard
- Gallows drawn stroke by stroke with every wrong guess (SVG, no images needed)
- Word shown as letter tiles, with a small animation when you reveal a letter
- Keys turn green for correct guesses and red for wrong ones
- Lives shown as hearts, with a win / game-over screen that reveals the word
- Over 600 words, with a new random word each game
- Works on desktop and mobile screens

## How to play

1. A random word is chosen and shown as empty tiles.
2. Click a letter (or press it on your keyboard) to guess.
3. A correct letter is revealed everywhere it appears. A wrong letter costs one life and draws a part of the hangman.
4. Reveal the whole word to win. Run out of the 6 lives and you lose.
5. Press **New word** or **Play again** to start another round.

## Tech stack

- **Python 3** with **Flask** for the game logic and a small JSON API
- **HTML, CSS and JavaScript** for the interface (single template, no frameworks)
- **Gunicorn** as the production server
- Deployed on **Render**

## Project structure

```
Hangman_game/
├── app.py                # Flask app: game logic and API routes
├── templates/
│   └── index.html        # Game interface (HTML, CSS, JS)
├── Words.py              # Word list
├── Hangman_art.py        # ASCII art used by the terminal version
├── Hangman_terminal.py   # Original command-line version of the game
├── requirements.txt      # Python dependencies
└── README.md
```

## Run it locally

You need Python 3 installed.

```bash
# 1. Get the code
git clone <your-repo-url>
cd WEB_PROJECTS_PY/Hangman_game

# 2. (Optional) create a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the server
python app.py
```

Then open **http://localhost:5000** in your browser.

> Don't open `index.html` directly from your folder. The game needs the Flask server running to work.

### Play the terminal version

```bash
python Hangman_terminal.py
```

## Deploy on Render

1. Push this project to GitHub.
2. On [render.com](https://render.com), choose **New → Web Service** and connect the repository.
3. Use these settings:

   | Setting | Value |
   |---|---|
   | Root Directory | `WEB_PROJECTS_PY/Hangman_game` |
   | Runtime | Python 3 |
   | Build Command | `pip install -r requirements.txt` |
   | Start Command | `gunicorn app:app` |

4. Under **Environment**, add a variable named `SECRET_KEY` with a long random value.
5. Click **Create Web Service**. Render gives you a public URL when the build finishes.

Note: on Render's free plan the app goes to sleep when idle, so the first visit after a while can be slow to load.

## API routes

| Method | Route | What it does |
|---|---|---|
| GET | `/` | Serves the game page |
| GET | `/api/state` | Returns the current game state |
| POST | `/api/guess` | Takes `{"letter": "a"}` and returns the updated state |
| POST | `/api/new` | Starts a new game |

The game state is kept in a signed Flask session cookie, so each player has their own game.

## What I learned

- Turning a command-line program into a web app
- Building a small JSON API with Flask and calling it with `fetch`
- Keeping game state per user with sessions
- Deploying a Python app with Gunicorn on Render, from a subfolder of a larger repository

## Possible improvements

- Word categories and difficulty levels
- Hints and a score or streak counter
- Sound effects
- Keeping the game state on the server instead of in the cookie

## Author

**Tanmay Soni** - BCA student, Indore
GitHub: [@Tanmay-x-Soni](https://github.com/Tanmay-x-Soni)