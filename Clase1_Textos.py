# This is a sample Python script.
from numbers import Number

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from manim import *
from pydub.utils import FRAME_WIDTHS


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


class Texto_Vertical(Scene):
    def construct(self):

        # agregamos las variables de altura y ancho
        altura_actual = config.pixel_height
        ancho_actual = config.pixel_width

        config.pixel_height = ancho_actual
        config.pixel_width = altura_actual


        config.frame_width = config.frame_height * 9 / 16
        #FRAME_HEIGHT = config.frame_height
        #FRAME_WIDTH = config.frame_width

        rejilla = NumberPlane()
        rejilla.scale(0.5)

        # agregamos el texto
        txt1 = Text("+", color=YELLOW)
        txt2 = Text("UP", color=RED).move_to(UP)
        txt3 = Text("2UP", color=GREEN).move_to(UP*2)
        txt4 = Text("3UP", color=BLUE).move_to(UP*3)
        txt5 = Text("4UP", color=ORANGE).move_to(UP*4)

        txt6 = Text("DOWN", color=RED).move_to(DOWN)
        txt7 = Text("2DOWN", color=GREEN).move_to(DOWN*2)
        txt8 = Text("3DOWN", color=BLUE).move_to(DOWN*3)
        txt9 = Text("4DOWN", color=ORANGE).move_to(DOWN*4)


        # simular
        self.camera.background_color=BLUE_E
        self.add(rejilla)
        self.wait()
        self.play(
            FadeIn(txt1),
            FadeIn(txt2),
            FadeIn(txt3),
            FadeIn(txt4),
            FadeIn(txt5)
        )
        self.play(
            FadeIn(txt6),
            FadeIn(txt7),
            FadeIn(txt8),
            FadeIn(txt9)
        )

        self.wait(1)



class texto_2(Scene):
    def construct(self):

        rejilla = NumberPlane()

        txt1 =  Text("Formula animada con Manim")
        txt1.scale(1.2)
        txt1[17:22].set_color(GREEN)
        txt1.move_to(UP * 2.5) # se usa para mover desde el centro
        #txt1.to_corner(DL, buff=2)    # se usa para mover a la esquina
        #txt1.to_edge(UP, buff=1)      # se usa para mover al borde

        txt2 = MathTex("v","=","{d \\over dt}","\\left(","A"," \\sin \\left(\\omega t + \\phi \\right)","\\right)")
        txt2.scale(0.7)
        txt2.to_edge(LEFT, buff=5)

        txt3=txt2.copy()
        txt3.move_to(UP).to_edge(LEFT, buff=5)

        txt4 = MathTex("v","=","A","{d \\over dt}","\\left("," \\sin \\left(\\omega t + \\phi \\right)","\\right)")
        txt4.scale(0.7)
        txt4.to_edge(LEFT, buff=5)

        txt5 = MathTex("v","=","A"," \\cos \\left(\\omega t + \\phi \\right)","{d \\over dt}","\\left(\\omega t + \\phi \\right)")
        txt5.scale(0.7)
        txt5.move_to(DOWN).to_edge(LEFT, buff=5)

        txt6 = MathTex("v","=","A","\\omega"," \\cos \\left(\\omega t + \\phi \\right)")
        txt6.scale(0.7)
        txt6.move_to(DOWN * 2).to_edge(LEFT, buff=5)

        #self.add(rejilla)
        self.play(Write(txt1), Write(txt2))

        self.play(Transform(txt2,txt3))

        self.play(
            Transform(txt3[0:2].copy(), txt4[0:2])
        )
        self.play(
            Transform(txt3[4].copy().set_color(YELLOW), txt4[2])
        )
        self.play(
            Transform(txt3[2:4].copy(), txt4[3:5]),
            Transform(txt3[5:7].copy(), txt4[5:7])
        )

        self.play(
            Transform(txt4[0:2].copy(), txt5[0:2])
        )
        self.play(
            Transform(txt4[2].copy(), txt5[2])
        )
        self.play(
            Transform(txt4[5].copy().set_color(YELLOW), txt5[3])
        )
        self.play(
            Transform(txt4[3].copy(), txt5[4]),
            Transform(txt4[5].copy(), txt5[5])
        )

        self.play(
            Transform(txt5[0:2].copy(), txt6[0:2])
        )
        self.play(
            Transform(txt5[2].copy(), txt6[2])
        )
        self.play(
            Transform(txt5[4:6].copy().set_color(YELLOW), txt6[3])
        )
        self.play(
            Transform(txt5[3].copy(), txt6[4])
        )

        self.wait(2)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
