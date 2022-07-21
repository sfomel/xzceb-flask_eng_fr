import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(englishToFrench(None),None)
        self.assertEqual(englishToFrench('Hello'),'Bonjour')

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(frenchToEnglish(None),None)
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
 
unittest.main()