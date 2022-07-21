import unittest

from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase): 
    def test_englishToFrench(self): 
        self.assertNotEqual(englishToFrench(None),None)
        self.assertEqual(englishToFrench('Hello'),'Bonjour')

    def test_frenchToEnglish(self): 
        self.assertNotEqual(frenchToEnglish(None),None)
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
 
unittest.main()