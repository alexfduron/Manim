
from manim import *
from pyglet.resource import animation


class leccion12(Scene):
    def construct(self):

        # agregamos las equiciones en variables
        eq1 = MathTex("2x^2+6x+7=0")
        eq1.move_to(UP * 3)

        eq2 = MathTex("x=\\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}")
        eq2.move_to(UP * 1.5)

        eq3 = MathTex(r"x_{1}=\frac{-b + \sqrt{b^2-4ac}}{2a}")

        eq4 = MathTex(r"\left( \begin{array}{cc} 1 & 2 \\ 3 & 4 \end{array} \right)")
        eq4.move_to(DOWN * 2)

        # ahora que lo muestre en la pantalla
        self.play(Write(eq1))
        self.play(Write(eq2))
        self.play(Write(eq3))
        self.play(Write(eq4))

        self.wait(1)


class leccion13(Scene):
    def construct(self):

        # agregamos las equiciones en variables
        eq1 = MathTex("2x^2+6x+7=0")
        eq1.scale(1.5)
        eq1.move_to(UP)

        eq2 = MathTex("2x^2", "+6x", "+7", "=0")
        eq2.scale(1.5)
        eq2.move_to(DOWN)

        self.play(Write(eq1))
        self.play(Write(eq2[0]))
        self.play(Write(eq2[1]))
        self.play(Write(eq2[2]))
        self.play(Write(eq2[3]))

        self.wait(1)


class leccion14(Scene):
    def construct(self):

        c1 = "#0F2C67"
        c2 = "#CD1818"
        c3 = "#F3950D"
        c4 = "#F4E185"

        eq1 = MathTex("2x^2+6x+7=0")
        eq1.scale(1.5)
        eq1.move_to(UP)

        # cuando usamos el comando \frac en latex no se puede separar
        # por lo tanto cambiamos al comando \over en latex
        eq2 = MathTex("{-b \\pm \\sqrt{b^2-4ac}} "," \\over "," {2a}")
        eq2.set_color(c4)
        eq2.scale(1.5)
        eq2.move_to(DOWN)
        eq2[1].set_color(c3)
        eq2[2].set_color(c2)

        self.play(Write(eq1))
        self.play(Write(eq2))

        self.wait(1)


class leccion15(Scene):
    def construct(self):

        c1 = "#0F2C67"
        c2 = "#CD1818"
        c3 = "#F3950D"
        c4 = "#F4E185"

        self.camera.background_color = c1

        eq0 = MathTex("x=", "2.5")
        eq0.move_to(UP * 2 + LEFT * 2)
        eq0.scale(1.5)

        eq1 = MathTex("y=", "1.5")
        eq1.move_to(UP * 2 + RIGHT * 2)
        eq1.scale(1.5)

        eq0.set_color(c3)
        eq1.set_color(c2)

        eq2 = MathTex("z=(","2.5",")^2+(","1.5",")^2")
        eq2.set_color(c4)
        eq2.move_to(DOWN)
        eq2.scale(1.5)
        eq2[1].set_color(c3)
        eq2[3].set_color(c2)

        self.play(Write(eq0))
        self.play(Write(eq1))
        self.play(Write(eq2[0]), Write(eq2[2]), Write(eq2[4]))
        self.play(Transform(eq0[1],eq2[1]), Transform(eq1[1],eq2[3]))

        self.wait(1)


