from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")
@app.route("/emotionDetector")

def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    label = response['label']
    score = response['score']
    if label is None:
        return "Invalid input! Try again."
    return "Text has been identified as {} with a score of {}.".format(label.split('_')[1], score)

@app.route("/")

def render_index_page():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
