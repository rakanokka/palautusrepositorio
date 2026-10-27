import unittest
from calculator import Calculator

class StubIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def read(self, text):
        return self.inputs.pop(0)

    def write(self, text):
        self.outputs.append(text)

class TestCalculaor(unittest.TestCase):
    
    def test_one_sum(self):
        io = StubIO(["1", "3", "-9999"])
        calc = Calculator(io)
        calc.execute()
        self.assertEqual(io.outputs[0], "Summa: 4")

    def test_two_sums(self):
        io = StubIO(["11", "11", "-1", "2", "-9999"])
        calc = Calculator(io)
        calc.execute()
        self.assertEqual(io.outputs[0], "Summa: 22")
        self.assertEqual(io.outputs[1], "Summa: 1")
