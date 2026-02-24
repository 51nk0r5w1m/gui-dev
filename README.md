# Assignment 4 – tkinter GUI: Food Viewer

A Python desktop GUI application built with tkinter that displays food images based on the user's radio button selection.

## Description

The Food Viewer app presents a window with a food image and four radio buttons (Chicken, Pie, Pizza, Steak). When the user selects a radio button, the displayed image updates to match the selection. The app defaults to Chicken on startup.

## Requirements

- Python 3
- Pillow library

## Setup

1. Clone or download this repository
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install pillow
   ```

## How to Run

Run from the project root directory:

```bash
python asn4.py
```

## Project Structure

```
gui-dev/
├── asn4.py               # Main application
├── images/
│   ├── chicken.jpg
│   ├── pie.jpg
│   ├── pizza.jpg
│   └── steak.jpg
└── codeExamplesASN4/     # Reference examples provided with assignment
    ├── showInfoDemo.py
    ├── labelImage.py
    └── radiobutton.py
```

## Features

- Displays a food image in a tkinter Label widget
- Four radio buttons dynamically swap the displayed image
- Images are resized to fit the window using the Pillow library
- Built using object-oriented design with a single `FoodViewer` class
