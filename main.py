# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from manim import *
#from manimlib.imports import *

class prueba(Scene):
    def construct(self):
        cuadro = Square()
        cuadro.set_color(BLUE)
        circulo = Circle()
        circulo.set_color(BLUE)
        circulo.set_fill(RED_B, opacity = 0.5)

        self.play(Write(cuadro))
        self.play(Transform(cuadro, circulo))
        self.wait(2)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
