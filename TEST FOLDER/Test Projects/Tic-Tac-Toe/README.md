# Modern Tic-Tac-Toe

A modern, web-based version of Tic-Tac-Toe built with Flask.

## Prerequisites

You need Python 3 and `flask` installed.

Since `pip` seems to be missing from your environment, you might need to install it first:

```bash
sudo apt install python3-pip
```

Then install dependencies:

```bash
pip3 install -r requirements.txt
```

## Running the Game

We've created a helper script to set everything up for you (including the virtual environment).

1.  Run the startup script:
    ```bash
    ./start_game.sh
    ```
2.  Open your web browser and go to:
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Features

- Modern, responsive UI with glassmorphism design.
- Interactive game board.
- Win/loss/draw detection.
- Reset game functionality.

## Original CLI Version

You can still play the terminal version by running:

```bash
python3 TicTacToe.py
```
