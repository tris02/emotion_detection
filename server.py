"""
Flask application for detecting emotions in text.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Route to analyze emotions in the provided text.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Check if text_to_analyze is provided
    if not text_to_analyze:
        return "Invalid input! Please provide text to analyze."

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Handle the case where dominant_emotion is None
    if response['dominant_emotion'] is None:
        return jsonify({
            "error": "Invalid text! Please try again!"
        }), 400

    # Extract the individual emotion scores and dominant emotion from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Format the output string
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    # Return the formatted response
    return formatted_response


@app.route("/")
def render_index_page():
    """
    Renders the main application page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    # Executes the Flask app and deploys it on localhost:5000.
    app.run(host="0.0.0.0", port=5000)
