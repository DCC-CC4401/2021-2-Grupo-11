import sys

class Hola:

    def print():
        print("hola")

def str_to_class(str):
    return getattr(sys.modules[__name__], str)

str_to_class("Hola").print()