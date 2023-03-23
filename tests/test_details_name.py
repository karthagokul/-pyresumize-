import sys

sys.path.append("src")
import spacy
from pyresumize.modules import NameStandardEngine
from unittest import TestCase


class Nameesting(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def test_name(self):
        self.nlp = spacy.load("en_core_web_sm")
        engine = NameStandardEngine(self.nlp)
        # Since its a private method
        result = engine.process("I am Working")
        self.assertEqual("", result)
        result = engine.process("Eindhoven is a city in Netherlands")
        self.assertEqual("", result)
        result = engine.process("")
        self.assertEqual("", result)
        # valid One
        result = engine.process("Gokul Kartha karthagokul@gmail.com")
        self.assertEqual("Gokul Kartha", result)
        # Todo
        # result=engine.process("Gokul S kartha")
        # self.assertEqual("Gokul S kartha",result)
