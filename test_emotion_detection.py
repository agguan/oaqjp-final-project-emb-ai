# test_emotion_detection.py

import unittest
from EmotionDetection.emotion_detection import emotion_detector 

class TestEmotionDetection(unittest.TestCase):
    def test_emotions(self):
        # Test case 1: Joy
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy', "Expected 'joy' for the statement: 'I am glad this happened'")

        # Test case 2: Anger
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger', "Expected 'anger' for the statement: 'I am really mad about this'")

        # Test case 3: Disgust
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust', "Expected 'disgust' for the statement: 'I feel disgusted just hearing about this'")

        # Test case 4: Sadness
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness', "Expected 'sadness' for the statement: 'I am so sad about this'")

        # Test case 5: Fear
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear', "Expected 'fear' for the statement: 'I am really afraid that this will happen'")

if __name__ == '__main__':
    unittest.main()
