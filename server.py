from flask import Flask, render_template, request
from EmotionDetection import emotion_detector
application = Flask(__name__)
@application.route("/")
def renderer():
    return render_template("index.html")
@application.route("/emotionDetector")
def analyze():
    statement = request.args.get("textToAnalyze")
    response = emotion_detector(statement)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    formatted = (f"For the given statement, the system response is "
    f"'anger': {response['anger']}, "
    f"'disgust': {response['disgust']}, "
    f"'fear': {response['fear']}, "
    f"'joy': {response['joy']}, and "
    f"'sadness': {response['sadness']}. "
    f"The dominant emotion is {response['dominant_emotion']}.")
    return formatted
if __name__ == "__main__":
    application.run(host="0.0.0.0", port = 5000)