#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value="") -> None:
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if type(new_value) != type("asd"):
            print("The value must be a string.")
        self._value = new_value

    def is_sentence(self):
        if self.value.endswith('.'):
            return True
        else:
            return False
     
    def is_question(self):
        if self.value.endswith('?'):
            return True
        else:
            return False
    
    def is_exclamation(self):
        if self.value.endswith('!'):
            return True
        else:
            return False
    
    def count_sentences(self):
        number = []
        regex = r"[.!?]+"

        if self.value != "":
            number = [sent for sent in re.split(regex,self.value) if sent != ""]
        return len(number)
    

c = MyString("asd...asd...")