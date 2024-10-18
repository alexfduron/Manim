from manim import *
from networkx.algorithms.bipartite.basic import color


class leccion8(Scene):
    def construct(self):

        # colores nativos en manim
        # color = WHITE
        # color = BLACK
        txt0 = Text("Curso de Manim - PURPLE", color = PURPLE).move_to(UP * 3.5)
        txt1 = Text("Curso de Manim - YELLOW", color = YELLOW).move_to(UP * 2.5)
        txt2 = Text("Curso de Manim - BLUE", color = BLUE).move_to(UP * 1.5)
        txt3 = Text("Curso de Manim - GREEN", color = GREEN).move_to(UP * 0.5)
        txt4 = Text("Curso de Manim - GRAY", color = GRAY).move_to(DOWN * 0.5)
        txt5 = Text("Curso de Manim - RED", color = RED).move_to(DOWN * 1.5)
        txt6 = Text("Curso de Manim - ORANGE", color = ORANGE).move_to(DOWN * 2.5)
        txt7 = Text("Curso de Manim - PINK", color = PINK).move_to(DOWN * 3.5)

        self.play(Write(txt0))
        self.play(Write(txt1))
        self.play(Write(txt2))
        self.play(Write(txt3))
        self.play(Write(txt4))
        self.play(Write(txt5))
        self.play(Write(txt6))
        self.play(Write(txt7))

        self.wait(1)


class leccion9(Scene):
    def construct(self):

        # se definen los colores por notacion Hexadecimal
        color1 = "#0F2C67"
        color2 = "#CD1818"
        color3 = "#F3950D"
        color4 = "#F4E185"

        # ahora cambiamos el color del fondo
        self.camera.background_color = color1

        # ahora agregamos texto en la pantalla
        txt1 = Text("Pitagoras", color = color2).move_to(UP * 2).scale(2)
        txt2 = Text("Pitagoras").move_to(UP * 0.5).scale(1.5)
        txt2.set_color(color3)
        txt3 = Text("Pitagoras").move_to(DOWN).set_color(color4)
        txt4 = Text("Pitagoras", color = BLUE).move_to(DOWN * 2).scale(0.75)
        txt5 = Text("Pitagoras").move_to(DOWN * 3).scale(0.5)
        txt5.set_color(WHITE)

        # ahora que lo muestre en la pantalla
        self.play(Write(txt1))
        self.play(Write(txt2))
        self.play(Write(txt3))
        self.play(Write(txt4))
        self.play(Write(txt5))

        self.wait(1)


class leccion10(Scene):
    def construct(self):

        # se definen los colores por notacion Hexadecimal
        color1 = "#0F2C67"
        color2 = "#CD1818"
        color3 = "#F3950D"
        color4 = "#F4E185"

        # ahora agregamos texto en la pantalla
        txt1 = Text("Pitagoras").scale(2).set_color_by_gradient(color1, color2)
        txt2 = Text("Pitagoras").scale(3)
        txt2.set_color_by_gradient(color1, color2, color3, color4)

        # ahora lo mostramos en la pantalla
        self.play(Write(txt1))
        self.play(Write(txt2))

        self.wait(1)


class leccion11(Scene):
    def construct(self):

        # se definen los colores por notacion Hexadecimal
        color1 = "#0F2C67"
        color2 = "#CD1818"
        color3 = "#F3950D"
        color4 = "#F4E185"

        # ahora agregamos texto en la pantalla
        txt1 = MarkupText(f'Curso de <span fgcolor="{color4}">Manim</span>', color=color2)
        txt1.move_to(UP * 2)
        txt1.scale(2)

        txt2 = Text("Curso Manim", t2c={'[3:5]':color4})
        txt2.scale(2)
        txt2.move_to(UP * 0.5)


        txt3 = Text("0123456789", t2c={'[1:5]':color4})
        txt3.scale(2)
        txt3.move_to(DOWN)

        txt4 = Text("0123456789", t2c = {'[5:-2]': color4})
        txt4.scale(2)
        txt4.move_to(DOWN * 2)

        # ahora lo mostramos en la pantalla
        self.play(Write(txt1))
        self.play(Write(txt2))
        self.play(Write(txt3))
        self.play(Write(txt4))

        self.wait(1)




