# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from manim import *

class prueba(Scene):
    def construct(self):
        cuadro = Square()
        circulo = Circle()
        circulo.set_fill(PINK, opacity = 0.5)

        self.play(Create(cuadro))
        self.play(Transform(cuadro, circulo))
        self.wait(2)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
