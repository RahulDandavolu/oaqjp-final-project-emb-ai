import requests
import json
def emotion_detector(text_to_analyze):
    website = ("https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict")
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(website, json=input_json, headers=headers)
    res_dict = json.loads(response.text)
    emotions = res_dict["Predictons"][0]["emotion"]
    anger = emotions["anger"]
    disguist = emotions["disguist"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]
    scores = {
        "anger": anger,
        "disguist": disguist,
        "fear": fear,
        "joy": joy,
        "sadness": sadness
    }
    dominant = max(scores, key = scores.get)
    return {
        "anger": anger,
        "disguist": disguist,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant
    }