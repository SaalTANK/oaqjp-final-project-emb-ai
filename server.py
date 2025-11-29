"""
This will run a Flask server for emotion detection
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_prediction():
    """
    This route will return the detected emotions in a string if valid
    """
    text_to_analyze = request.args.get("textToAnalyze")
    emotion_detection = emotion_detector(text_to_analyze)

    dominant_emotion = emotion_detection['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is"
        f"'anger': {emotion_detection['anger']}, "
        f"'disgust': {emotion_detection['disgust']}, "
        f"'fear': {emotion_detection['fear']}, "
        f"'joy': {emotion_detection['joy']} and "
        f"'sadness': {emotion_detection['sadness']}."
        f" The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    This route will render the index page under templates/index.html
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run("localhost", 5000)
