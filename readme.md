# Trigger Bot

This project is a Python-based trigger bot that detects changes in the color of the center pixel on the screen and triggers an action (e.g., shooting).

## Features

- Monitors the center pixel of the screen for color changes.
- Triggers a predefined action when a color change is detected.
- Configurable settings for sensitivity and action.

## Requirements

- Python 3.x
- `quartz` To get keyboard signals for MacOs
- `PIL` To view the screen for MacOs

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Bokkieboy/Python-triggerbot.git
    cd triggerbot
    ```

2. Install the required libraries:
    ```bash
    pip install pillow pyautogui
    ```

## Usage

1. Run the script:
    ```bash
    python triggerbot.py
    ```

2. The bot will start monitoring the center pixel for color changes and trigger the action when a change is detected.

## Configuration

You can configure the bot by modifying the `config.json` file:

- `sensitivity`: Adjust the sensitivity of color change detection.
- `action`: Define the action to be triggered (e.g., mouse click, keyboard press).

## Disclaimer

This project is for educational purposes only. Use it responsibly and do not use it for any malicious activities.

