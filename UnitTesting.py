from Computer import ComputerMode
from CodeValidation import CodeValidator
import unittest

class TestingComputer(unittest.TestCase):
    def setUp(self):
        self.Comp1 = ComputerMode('b')
        self.Comp2 = ComputerMode('C')

    def test_randomCode(self):
        code1 = self.Comp1.randomCode()
        self.assertEqual(4,len(code1))

    def test_feedback(self):
        feedback1 = self.Comp1.giveFeedback(['R','L','G','B'],['R','L','B','G'])
        self.assertEqual('BBWW',feedback1)

    def test_randomCode44(self):
        code2 = self.Comp2.randomCode()
        self.assertEqual(5,len(code2))
    
    def test_feedback44(self):
        feedback2 = self.Comp2.giveFeedbackMM44(['R','L','G','B','_'],['R','L','_','B','G'])
        self.assertEqual('BBWBW',feedback2)

class TestingValidators(unittest.TestCase):
    def setUp(self):
        self.CodeVali = CodeValidator()
    
    def test_CLValid(self):
        codeA = self.CodeVali.codeLengthValidation('RGbY')
        self.assertEqual(True,codeA)
    
    def test_CCValid(self):
        codeB = self.CodeVali.codeColorValidation('rbkw')
        self.assertEqual(False,codeB)
    
    def test_CLValid44(self):
        codeC = self.CodeVali.MM44codeLengthValidator('lwk')
        self.assertEqual(False,codeC)
    
    def test_CCValid44(self):
        codeD = self.CodeVali.MM44codeColorValidator('_gl_w')
        self.assertEqual(True,codeD)
        
unittest.main()