import numpy as np
from manim import *
from networkx.algorithms.bipartite.basic import color
from numpy.ma.core import set_fill_value



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


class grafica3D(ThreeDScene):
    def construct(self):

        # creamos los colores con los que vamos a trabajar
        cielo = "#C4DDFF"
        azul = "#0016DE"
        rojo = "#B20600"

        # modificamos el fondo de la pantalla
        self.camera.background_color = cielo

        # agregamos el plano cartesiano
        ax = ThreeDAxes().set_color(azul)
        x = MathTex("x")
        x.set_color(azul)
        x.move_to(np.array([5,0.5,0]))
        y = MathTex("y")
        y.set_color(azul)
        y.move_to(np.array([0.5,5,0]))
        z = MathTex("z")
        z.set_color(azul)
        z.move_to(np.array([0.5,0,3]))


        # agregamos texto
        txt3d = MathTex("z = (x^2 + 3y^2)e^{1 - x^2 - y^2}")
        txt3d.set_color(BLACK)
        txt3d.to_corner(UL)

        txt1 = MathTex(r"\theta \leftarrow", r"0^\circ ")
        txt1.set_color(BLACK)
        txt1.move_to(RIGHT * 5.3 + UP * 3)

        txt2 = MathTex(r"\phi \leftarrow", r"0^\circ ")
        txt2.set_color(BLACK)
        txt2.move_to(RIGHT * 5.3 + UP * 1.7)

        txt3 = MathTex(r"\theta \leftarrow", r"{45}^\circ ")
        txt3.set_color(BLACK)
        txt3.move_to(RIGHT * 5.3 + UP * 3)

        txt4 = MathTex(r"\phi \leftarrow", r"{60}^\circ ")
        txt4.set_color(BLACK)
        txt4.move_to(RIGHT * 5.3 + UP * 1.7)


        # agregamos el grafico
        curva = Surface(
            lambda u, v: np.array([
                u,
                v,
                (u ** 2 + 3 * v ** 2) * np.exp(1 - u ** 2 - v ** 2)
            ]),
            v_range=[-3,3],
            u_range=[-3,3],
            checkerboard_colors=[RED_D, RED_E],
            resolution=(15,15)
        )

        curva.set_fill_by_checkerboard(rojo, azul, opacity=0.5)


        # simulamos
        # orientamos la camara
        self.set_camera_orientation(theta=45 * DEGREES, phi=60 * DEGREES)
        self.add(ax, x, y, z)

        # agregamos texto fijo
        self.add_fixed_in_frame_mobjects(txt3d)

        # agregamos el grafico
        self.play(Write(curva))

        # cambio de camara
        self.add_fixed_in_frame_mobjects(txt1, txt2)
        self.play(FadeIn(txt1, txt2))
        self.move_camera(theta=0*DEGREES, phi=0*DEGREES)

        self.play(FadeOut(txt1[1], txt2[1]))
        self.add_fixed_in_frame_mobjects(txt3[1], txt4[1])
        self.play(FadeIn(txt3[1], txt4[1]))
        self.move_camera(theta=PI/4, phi=PI/3)

        # aplicamos rotacion al grafico
        self.begin_ambient_camera_rotation(rate=0.10)

        self.wait(2)



class grafica3D_2(ThreeDScene):
    def construct(self):

        # creamos los colores con los que vamos a trabajar
        cielo = "#C4DDFF"
        azul = "#0016DE"
        rojo = "#B20600"

        # modificamos el fondo de la pantalla
        self.camera.background_color = cielo

        # agregamos el plano cartesiano
        ax = ThreeDAxes().set_color(azul)
        x = MathTex("x")
        x.set_color(azul)
        x.move_to(np.array([5, 0.5, 0]))
        y = MathTex("y")
        y.set_color(azul)
        y.move_to(np.array([0.5, 5, 0]))
        z = MathTex("z")
        z.set_color(azul)
        z.move_to(np.array([0.5, 0, 3]))

        # agregamos texto
        surf1 = Text("Esfera")
        surf1.set_color(BLACK)
        surf1.to_corner(UL)

        surf2 = Text("Toro")
        surf2.set_color(BLACK)
        surf2.to_corner(UL)

        surf3 = Text("Catenoide")
        surf3.set_color(BLACK)
        surf3.to_corner(UL)

        # agregamos el grafico
        esfera = Surface(
            lambda u, v: np.array([
                2 * np.cos(v) * np.cos(u),
                2 * np.sin(v) * np.cos(u),
                2 * np.sin(u)
            ]),
            u_range=[-PI, PI],
            v_range=[0, 2*PI],
            resolution=(15,30),
            checkerboard_colors=(rojo, azul),
            fill_opacity=0.5,
            stroke_opacity=1,
            stroke_color=BLACK
        )

        toro = Surface(
            lambda u, v: np.array([
                (3 + 1 * np.cos(v)) * np.cos(u),
                (3 + 1 * np.cos(v)) * np.sin(u),
                1 * np.sin(v)
            ]),
            u_range=[-PI, PI],
            v_range=[0, 2*PI],
            resolution=(15, 30)
        )

        catenoide = Surface(
            lambda u, v: np.array([
                0.5 * np.cosh(v / 0.5) * np.cos(u),
                0.5 * np.cosh(v / 0.5) * np.sin(u),
                v
            ]),
            u_range=[-PI, PI],
            v_range=[-1, 1],
            resolution=(10, 30),

        )

        catenoide.set_fill_by_value(
            axes=ax,
            colors=[
                (RED, -1),
                (YELLOW, 0),
                (GREEN, 1)
            ],
            axis=2
        )

        # simulamos
        # orientamos la camara
        self.set_camera_orientation(theta=45 * DEGREES, phi=60 * DEGREES)
        self.add(ax, x, y, z)

        # agregamos texto fijo
        self.add_fixed_in_frame_mobjects(surf1)

        # aplicamos rotacion al grafico
        self.begin_ambient_camera_rotation(rate=0.10)

        # agregamos el grafico esfera
        self.play(Write(esfera))

        # cambiamos el texto fijo
        self.play(FadeOut(surf1))
        self.add_fixed_in_frame_mobjects(surf2)
        self.play(FadeIn(surf2))

        #cambiamos el grafico
        self.play(Transform(esfera, toro))

        # cambiamos el texto fijo
        self.play(FadeOut(surf2))
        self.add_fixed_in_frame_mobjects(surf3)
        self.play(FadeIn(surf3))

        # cambiamos el grafico
        self.play(Transform(esfera, catenoide))

        self.wait(2)


class grafica_2(Scene):
    def construct(self):

        # creamos los colores con los que vamos a trabajar
        cielo = "#C4DDFF"
        azul = "#0016DE"
        rojo = "#B20600"
        purpura = "#800080"

        # modificamos el fondo de la pantalla
        self.camera.background_color = cielo

        # agregamos texto
        txt1 = Text("Epicicloide")
        txt1.set_color(RED)
        txt1.move_to(UP * 3.5)

        namex = MathTex(r"x = 2.5 \cos( \theta ) - 0.5 \cos(5 \theta)")
        namex.set_color(BLACK)
        namex.move_to(RIGHT * 3.5 + UP)

        namey = MathTex(r"x = 2.5 \sin( \theta ) - 0.5 \sin(5 \theta)")
        namey.set_color(BLACK)
        namey.move_to(RIGHT * 3.5)

        rango = MathTex(r"\theta \in (0.5 \pi)")
        rango.set_color(BLACK)
        rango.move_to(RIGHT * 3.5 + DOWN)


        # agregamos los ejes
        ax = Axes(
            x_range=[-3.5,3.5,1],
            y_range=[-3.5,3.5,1],
            x_length=7,
            y_length=7,
            axis_config={"include_tip":True}
        )
        ax.set_color(GREY)
        ax.move_to(np.array([-3.5,0,0]))

        # agregamos los graficos
        circulo_grande = ParametricFunction(
            lambda u: np.array([
                2 * np.sin(u),
                2 * np.cos(u),
                0
            ]),
            color=BLUE,
            t_range=np.array([0, 2 * PI, 0.01])
        )
        circulo_grande.move_to(ax.coords_to_point(0, 0))

        epicicloide = ParametricFunction(
            lambda u: np.array([
                2.5 * np.cos(u) - 0.5 * np.cos(5 * u),
                2.5 * np.sin(u) - 0.5 * np.sin(5 * u),
                0
            ]),
            color=purpura,
            t_range=np.array([0, 2 * PI, 0.01])
        )
        epicicloide.move_to(ax.coords_to_point(0, 0))


        # simulacion
        self.add(txt1, ax)
        self.play(Write(namex), Write(namey), Write(rango))

        # agregamos los graficos
        self.play(Write(circulo_grande), run_time=1)
        self.play(Write(epicicloide), run_time=1)

        self.wait(1)

