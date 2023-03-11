import unittest
from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') # Test for the translation of the world ‘Hello’ and ‘Bonjour’.
        self.assertEqual(englishToFrench('Hello, how are you today?'), 'Bonjour, comment vous êtes aujourd\'hui?') # Test a full sentence with punctuation
        self.assertEqual(englishToFrench('Bonjour'), 'Hello') # 
        self.assertEqual(englishToFrench(''), 'You must supply some input') # null input

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # Test for the translation of the world ‘Bonjour’ and ‘Hello’.
        self.assertEqual(frenchToEnglish('Bonjour, comment vous êtes aujourd\'hui?'), 'Hello, how are you today?') # Test a full sentence with punctuation
        self.assertEqual(frenchToEnglish(''), 'You must supply some input') # null input

unittest.main()