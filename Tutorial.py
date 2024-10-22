
from manim import *
from networkx.drawing import circular_layout


class CreateCircle(Scene):
    def construct(self):

        circulo = Circle()
        circulo.set_color(BLUE)
        circulo.set_fill(PINK, opacity=0.5)

        self.play(Create(circulo))

        self.wait(1)



class BoxToCircle(Scene):
    def construct(self):

        circulo = Circle()
        circulo.set_color(BLUE)
        circulo.set_fill(PINK, opacity=0.5)

        caja = Square()
        caja.set_color(BLUE)
        caja.set_fill(RED, opacity=0.5)
        caja.rotate(PI / 4)

        self.play(Create(caja))
        self.play(Transform(caja, circulo))
        self.play(FadeOut(caja))

        self.wait(1)


class BoxToCircle2(Scene):
    def construct(self):

        circulo = Circle()
        circulo.set_fill(PINK, opacity=0.5)
        circulo.scale(1)
        circulo.move_to(LEFT * 2)

        caja = Square()
        caja.set_fill(BLUE, opacity=0.5)
        caja.next_to(circulo, RIGHT, buff=0.5) # buff=0.5 aplicamos un margen de distancia entre los dos objetos.
        caja.scale(1)

        self.add(NumberPlane())
        self.play(Create(circulo), Create(caja))

        self.wait(1)


class DifRotBox(Scene):
    def construct(self):

        L_Box = Square(color=BLUE, fill_opacity=0.7).shift(LEFT * 2)
        R_Box = Square(color=GREEN, fill_opacity=0.7).shift(RIGHT * 2)

        self.play(
            L_Box.animate.rotate(PI), # animate intenta interpolar dos objetos idénticos
            Rotate(R_Box, angle=PI),
            run_time=2
        )
        self.wait()


class TwoTransforms(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        txt =Text("Transform").move_to(UP * 3)
        self.play(FadeIn(txt))
        self.play(Transform(a, b))
        self.play(Transform(a, c))
        self.play(FadeOut(a), FadeOut(txt))

    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        txt = Text("Replacement Transform").move_to(UP * 3)
        self.play(FadeIn(txt))
        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(c), FadeOut(txt))

    def construct(self):
        self.transform()
        self.wait(0.5)  # wait for 0.5 seconds
        self.replacement_transform()


