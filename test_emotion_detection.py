from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector(self):
        test_statements_emotion = {
            "I am glad this happened": "joy", 
            "I am really mad about this": "anger", 
            "I feel disgusted just hearing about this": "disgust", 
            "I am so sad about this": "sadness", 
            "I am really afraid that this will happen": "fear"
        }

        for test_statement in test_statements_emotion:
            self.assertEqual(
                emotion_detector(test_statement)['dominant_emotion'],
                test_statements_emotion[test_statement]
            )

unittest.main()
