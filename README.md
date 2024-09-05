# Emotion Detection

## Overview

Emotion Detection is a Python package that leverages an external sentiment analysis service to analyze the emotions within a given text. The package offers both a Flask-based web interface and a command-line tool for seamless interaction with the service.

## Features

- Detects key emotions such as anger, disgust, fear, joy, and sadness.
- Identifies and provides the dominant emotion in any given text.
- Includes a simple Flask web server for emotion analysis through a web interface.
- Offers a command-line interface for easy integration into scripts and automation tasks.

## Installation

To install the package locally using `pip`, navigate to the project directory and run in bash: 
'''pip install
'''

## Web Interface

To start the Flask server, run (python3.11 is used in development version): 
'''python server.py
'''        
Then navigate to http://localhost:5000/ in your web browser to access the web interface.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
