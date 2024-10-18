import numpy as np
from manim import *
from numpy import *
from typing_extensions import runtime


class grafica(Scene):
    def construct(self):

        # creamos los colores con los que vamos a trabajar
        cielo = "#C4DDFF"
        azul  = "#0016DE"
        rojo  = "#B20600"

        # modificamos el fondo de la pantalla
        self.camera.background_color = cielo

        # agregamos el plano cartesiano
        ax = Axes(x_length = 9,
                  y_length = 3,
                  x_range = [-1, 14, 1],
                  y_range = [-3.5, 3.5, 1],
                  axis_config = {"include_tip":True})
                  #x_axis_config = {"numbers_to_include": [3.14, 6.28, 9.42, 12.56]}

        ax.set_color(azul)


        p1 = MathTex("\pi")
        p1.set_color(azul)
        p1.scale(0.8)
        p1.move_to(ax.coords_to_point(PI, -0.8))

        p2 = MathTex('2\pi')
        p2.set_color(azul)
        p2.scale(0.8)
        p2.move_to(ax.coords_to_point(2*PI, -0.8))

        p3 = MathTex('3\pi')
        p3.set_color(azul)
        p3.scale(0.8)
        p3.move_to(ax.coords_to_point(3 * PI, -0.8))

        p4 = MathTex('4\pi')
        p4.set_color(azul)
        p4.scale(0.8)
        p4.move_to(ax.coords_to_point(4 * PI, -0.8))


        # agregamos los nombres de las funciones
        eq0 = MathTex('y = \sin{x}')
        eq0.set_color(azul)
        eq0.scale(2)
        eq0.move_to(UP * 2.5)

        eq1 = eq0.copy()

        eq2 = MathTex('y = 2 \sin{x}')
        eq2.set_color(azul)
        eq2.scale(2)
        eq2.move_to(UP * 2.5)

        eq3 = MathTex('y = 0.5 \sin{x}')
        eq3.set_color(azul)
        eq3.scale(2)
        eq3.move_to(UP * 2.5)

        # agregamos las funciones
        curva0 = ax.plot(lambda x: np.sin(x), x_range=[0,4 * PI])
        curva0.set_color(rojo)

        curva1 = curva0.copy()

        curva2 = ax.plot(lambda x: 3 * np.sin(x), x_range=[0,4 * PI])
        curva2.set_color(rojo)

        curva3 = ax.plot(lambda x: 0.5 * np.sin(x), x_range=[0,4 * PI])
        curva3.set_color(rojo)

        # simulamos
        self.add(ax, p1, p2, p3, p4)
        self.play(Write(curva1), Write(eq1))
        self.play(Transform(curva1, curva2), Transform(eq1, eq2), run_time=1)
        self.play(Transform(curva1, curva0), Transform(eq1, eq0), run_time=1)
        self.play(Transform(curva1, curva3), Transform(eq1, eq3), run_time=1)
        self.play(Transform(curva1, curva0), Transform(eq1, eq0), run_time=1)

        self.wait(1)