"""This module sets up a Flask web application for emotion detection
using the emotion_detector function from the EmotionDetection package."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotion_detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """Receives the text from the HTML interface and runs analysis over it
    using emotion_detector() function, returnining the output."""

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the dominant emotion is None
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # Format the response if it is valid
    formatted_response = (
        f"anger: {response['anger']}, "
        f"disgust: {response['disgust']}, "
        f"fear: {response['fear']}, "
        f"joy: {response['joy']}, "
        f"sadness: {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}.")

    # Return output
    return f"For the given statement, the system response is {formatted_response}"

@app.route("/")
def render_index_page():
    """Initiates the rendering of the main application page over the Flask channel."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
