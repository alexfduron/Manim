# This is a sample Python script.
from numbers import Number

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from manim import *

class leccion1(Scene):
    def construct(self):
        texto1 = Text("Hola Amigo")     # creamos el texto en una variable
        self.add(texto1)                # se agrega el texto a la escena
        self.wait(1)                    # se colocan 3 segundos de espera

class leccion2(Scene):
    def construct(self):
        texto2 = Text("Curso de Manim")
        self.add(texto2)        # agrega el texto inmediatamente
        self.wait(1)
        self.remove(texto2)     # quita el texto inmediatamente
        self.wait(1)


class leccion3(Scene):
    def construct(self):
        texto3 = Text("Curso de Manim con animacion FadeIn")
        self.play(FadeIn(texto3))
        self.wait(1)
        self.play(FadeOut(texto3))
        self.wait(1)
        texto4 = Text("Curso de Manim con animacion Write")
        self.play(Write(texto4))
        self.wait(1)
        self.play(FadeOut(texto4))
        self.wait(1)


class leccion4(Scene):
    def construct(self):
        rejilla = NumberPlane()     # se usa para medir las distacias dentro de la pantalla
        self.add(rejilla)
        self.wait(1)

        texto5 = Text("Teorema").move_to(RIGHT + UP)
        texto6 = Text("Lema").move_to(LEFT + DOWN)
        self.add(texto5, texto6)
        self.wait(1)


class leccion5(Scene):
    def construct(self):
        rejilla = NumberPlane()     # se usa para medir las distacias dentro de la pantalla
        self.add(rejilla)
        self.wait(1)

        texto7 = Text("A").move_to(RIGHT + UP)
        texto8 = Text("B").move_to(LEFT + DOWN)
        texto9 = Text("C").move_to(LEFT * 2.5)
        texto10 = Text("D").move_to(DOWN * 3.2)
        self.add(texto7, texto8, texto9, texto10)
        self.wait(1)



class leccion6(Scene):
    def construct(self):
        rejilla = NumberPlane()     # se usa para medir las distacias dentro de la pantalla
        self.add(rejilla)
        self.wait(1)

        texto11 = Text("A").move_to(np.array([1,1,0]))
        texto12 = Text("B").move_to(np.array([-1,-1,0]))
        texto13 = Text("C").move_to(np.array([-2.5,0,0]))
        texto14 = Text("D").move_to(np.array([0,-3.2,0]))
        self.add(texto11, texto12, texto13, texto14)
        self.wait(1)


class leccion7(Scene):
    def construct(self):
        rejilla = NumberPlane()  # se usa para medir las distacias dentro de la pantalla
        self.add(rejilla)
        self.wait(1)

        texto15 = Text("Curso de Manim").move_to(np.array([0, 1, 0]))
        texto16 = Text("Curso de Manim").move_to(np.array([0, 0, 0]))
        texto17 = Text("Primer paso").move_to(np.array([0, -1, 0]))
        texto18 = Text("Segundo paso").move_to(np.array([0, -2, 0]))
        self.play(FadeIn(texto15))
        self.wait(1)
        self.play(Transform(texto15, texto16))  # tiene el efecto de movimiento ya que tienen el mismo texto
        self.wait(1)
        self.play(Transform(texto15, texto17))  # tiene el efecto de movimiento y de cambio
        self.wait(1)
        self.play(Transform(texto15, texto18))
        self.wait(1)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
