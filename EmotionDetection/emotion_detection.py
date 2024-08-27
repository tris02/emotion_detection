"""
Module for detecting emotions in text using an external sentiment analysis service.
"""

import json  # Import the json library
import requests  # Import the requests library to handle HTTP requests


def emotion_detector(text_to_analyze):
    """
    Analyze the emotions in the provided text using an external API.

    Args:
        text_to_analyze (str): The text to analyze for emotions.

    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion.
        int: The HTTP status code indicating success (200) or bad request (400).
    """

    # Check if the input text is blank or None
    if not text_to_analyze or text_to_analyze.strip() == "":
        # Return a response with all values set to None and status_code 400 for blank input
        response = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return response, 400

    # URL of the sentiment analysis service
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )

    # Create a dictionary with the text to be analyzed
    input_json = {"raw_document": {"text": text_to_analyze}}

    # Set the headers required for the API request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json=input_json, headers=headers, timeout=10)

    # Convert the response text into a dictionary
    response_dict = json.loads(response.text)

    # Access the first element in the 'emotionPredictions' list and then the 'emotion' dictionary
    emotions = response_dict['emotionPredictions'][0]['emotion']

    # Extract the required set of emotions
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    # Find the dominant emotion
    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return the required output format
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
    