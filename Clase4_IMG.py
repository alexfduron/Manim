from manim import *
from manim.utils.color.X11 import BROWN


class leccion16(Scene):
    def construct(self):

        # agregamos la imagen
        imagen = ImageMobject(r".\media\images\main\fondo.jpg")
        imagen.scale(1.5)

        self.add(imagen)

        # agregamos el titulo
        titulo = Text("Movimiento Rectilineo")
        titulo.set_color(BLACK)
        titulo.move_to(UP * 3.5)

        self.play(Write(titulo))

        self.wait(1)


class leccion17(Scene):
    def construct(self):

        # agregamos la imagen
        imagen = ImageMobject(r".\media\images\Clase4_IMG\fondo.jpg")
        imagen.scale(1.5)

        auto = ImageMobject(r".\media\images\Clase4_IMG\Vehicle-Red-Car.png")
        auto.move_to(DOWN * 3 + LEFT * 4)
        auto.scale(0.5)

        auto1 = auto.copy()
        auto1.move_to(DOWN * 3 + RIGHT * 4)

        calle1 = ImageMobject(r".\media\images\Clase4_IMG\Road.png")
        calle1.move_to(DOWN * 3.5 + LEFT * 5.5)
        calle1.scale(0.5)

        calle2 = calle1.copy()
        calle2.move_to(DOWN * 3.5 + LEFT * 2.5)

        calle3 = calle1.copy()
        calle3.move_to(DOWN * 3.5)

        calle4 = calle1.copy()
        calle4.move_to(DOWN * 3.5 + RIGHT * 2.5)

        calle5 = calle1.copy()
        calle5.move_to(DOWN * 3.5 + RIGHT * 5.5)

        self.add(imagen, calle5, calle4, calle3, calle2, calle1, auto)

        # agregamos el titulo
        titulo = Text("Movimiento Rectilineo")
        titulo.set_color(BLACK)
        titulo.move_to(UP * 3.5)

        self.play(Write(titulo))

        self.play(Transform(auto, auto1), run_time = 5)

        self.wait(1)


class leccion18(Scene):
    def construct(self):

        # agregamos la imagen
        imagen = ImageMobject(r".\media\images\Clase4_IMG\fondo.jpg")
        imagen.scale(1.5)

        tiempo = SVGMobject(r".\media\images\Clase4_IMG\reloj.svg")
        tiempo.move_to(UP * 2 + RIGHT * 4)
        tiempo.set_color(BROWN)

        auto = ImageMobject(r".\media\images\Clase4_IMG\Vehicle-Red-Car.png")
        auto.move_to(DOWN * 3 + LEFT * 4)
        auto.scale(0.5)

        auto1 = auto.copy()
        auto1.move_to(DOWN * 3 + RIGHT * 4)

        calle1 = ImageMobject(r".\media\images\Clase4_IMG\Road.png")
        calle1.move_to(DOWN * 3.5 + LEFT * 5.5)
        calle1.scale(0.5)

        calle2 = calle1.copy()
        calle2.move_to(DOWN * 3.5 + LEFT * 2.5)

        calle3 = calle1.copy()
        calle3.move_to(DOWN * 3.5)

        calle4 = calle1.copy()
        calle4.move_to(DOWN * 3.5 + RIGHT * 2.5)

        calle5 = calle1.copy()
        calle5.move_to(DOWN * 3.5 + RIGHT * 5.5)

        self.add(imagen, calle5, calle4, calle3, calle2, calle1, auto)

        # agregamos el titulo
        titulo = Text("Movimiento Rectilineo")
        titulo.set_color(BLACK)
        titulo.move_to(UP * 3.5)

        self.add_sound(r".\media\audio\car_motor.mp3")

        self.play(Write(titulo), run_time = 2)

        self.play(Write(tiempo), run_time = 4)

        self.play(Transform(auto, auto1), run_time = 3)

        self.wait(0.5)



