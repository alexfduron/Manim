import numpy as np
from manim import *




class hexagono(Scene):
    def construct(self):

        # agregamos los colores deseados
        rosa = "#C12786"
        azul = "#133160"
        gris = "#AAAAAA"
        verde = "#008000"

        # agregamos la imagen de fondo
        img_fondo = SVGMobject(r".\media\images\Clase4_IMG\honduras.svg")

        # agregamos las cooredenadas
        coor1 = np.array([3 * np.cos(0 * DEGREES), 3 * np.sin(0 * DEGREES), 0])
        coor2 = np.array([3 * np.cos(60 * DEGREES), 3 * np.sin(60 * DEGREES), 0])
        coor3 = np.array([3 * np.cos(120 * DEGREES), 3 * np.sin(120 * DEGREES), 0])
        coor4 = np.array([3 * np.cos(180 * DEGREES), 3 * np.sin(180 * DEGREES), 0])
        coor5 = np.array([3 * np.cos(240 * DEGREES), 3 * np.sin(240 * DEGREES), 0])
        coor6 = np.array([3 * np.cos(300 * DEGREES), 3 * np.sin(300 * DEGREES), 0])

        # agregamos los puntos
        p1 = Dot()
        p1.set_color(azul)
        p1.move_to(coor1)

        p2 = Dot()
        p2.set_color(azul)
        p2.move_to(coor2)

        p3 = Dot()
        p3.set_color(azul)
        p3.move_to(coor3)

        p4 = Dot()
        p4.set_color(azul)
        p4.move_to(coor4)

        p5 = Dot()
        p5.set_color(azul)
        p5.move_to(coor5)

        p6 = Dot()
        p6.set_color(azul)
        p6.move_to(coor6)

        # agregamos las lineas
        l1 = Line(p1, p2)
        l1.set_color(verde)

        l2 = Line(p2, p3)
        l2.set_color(verde)

        l3 = Line(p3, p4)
        l3.set_color(verde)

        l4 = Line(p4, p5)
        l4.set_color(verde)

        l5 = Line(p5, p6)
        l5.set_color(verde)

        l6 = Line(p6, p1)
        l6.set_color(verde)

        # agregamos las geometrias
        c0 = Circle(3)
        c0.set_color(gris)

        c1 = Circle(3)
        c1.set_color(rosa)
        c1.shift(coor1)

        c2 = Circle(3)
        c2.set_color(rosa)
        c2.shift(coor2)

        c3 = Circle(3)
        c3.set_color(rosa)
        c3.shift(coor3)

        c4 = Circle(3)
        c4.set_color(rosa)
        c4.shift(coor4)

        c5 = Circle(3)
        c5.set_color(rosa)
        c5.shift(coor5)

        c6 = Circle(3)
        c6.set_color(rosa)
        c6.shift(coor6)

        # simulacion
        self.add(img_fondo)
        self.play(Create(c0))

        self.play(Create(p1))
        self.play(Create(c1))
        self.play(Create(p2))
        self.play(Create(l1))
        self.play(Create(c2))
        self.play(Create(p3))
        self.play(Create(l2))
        self.play(Create(c3))
        self.play(Create(p4))
        self.play(Create(l3))
        self.play(Create(c4))
        self.play(Create(p5))
        self.play(Create(l4))
        self.play(Create(c5))
        self.play(Create(p6))
        self.play(Create(l5))
        self.play(Create(c6))
        self.play(Create(l6))
        self.play(FadeOut(c1, c2, c3, c4, c5, c6))
        self.play(FadeOut(c0))

        self.wait(2)

