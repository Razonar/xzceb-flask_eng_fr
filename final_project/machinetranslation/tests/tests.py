from translator import englishToFrench, frenchToEnglish
import unittest

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self):
        self.assertEqual(frenchToEnglish(''), '')
    def test2(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(''), '')
    def test2(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

unittest.main()
