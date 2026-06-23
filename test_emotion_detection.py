from EmotionDetection import emotion_detector
def test_detector():
    test_cases = {
        "I am glad this happened":	"joy",
        "I am really mad about this":	"anger",
        "I feel disgusted just hearing about this":	"disgust",
        "I am so sad about this":	"sadness",
        "I am really afraid that this will happen":	"fear"
    }
    count = 0
    for statement, dominant_emotion in test_cases.items():
        count = count + 1
        result = emotion_detector(statement)
        if result["dominant_emotion"] == dominant_emotion:
            print("Passed statement: " + count + "with dominant_emotion " + dominant_emotion)
        else:
            print("Failed statement: " + count + "with dominant_emotion " + dominant_emotion)
test_detector()