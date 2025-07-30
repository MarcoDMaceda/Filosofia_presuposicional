from manim import *


def create_cloud():
    cloud_out = VGroup(
        Circle(radius=0.6),
        Circle(radius=0.5).shift(LEFT * 0.5 + DOWN * 0.2),
        Circle(radius=0.4).shift(RIGHT * 0.5 + DOWN * 0.1),
        Circle(radius=0.45).shift(RIGHT * 0.1 + UP * 0.3),
    )
    cloud_out.set_fill(WHITE, opacity=1).set_stroke(width=0)
    cloud_out.scale(1.5)

    cloud_in = VGroup(
        Circle(radius=0.6),
        Circle(radius=0.5).shift(LEFT * 0.5 + DOWN * 0.2),
        Circle(radius=0.4).shift(RIGHT * 0.5 + DOWN * 0.1),
        Circle(radius=0.45).shift(RIGHT * 0.1 + UP * 0.3),
    )
    cloud_in.set_fill(BLACK, opacity=1).set_stroke(width=0)
    cloud_in.scale(1.4)

    return VGroup(cloud_out, cloud_in)

class ThreeShapesScene(Scene):
    def construct(self):
        rectangles = VGroup(*[Rectangle(width=3, height=1.5) for _ in range(3)])
        rectangles.arrange(DOWN, buff=1)
        rectangles.move_to(ORIGIN)

        ellipse = Ellipse(width=3, height=1.5)
        ellipse.to_edge(RIGHT, buff=1)

        def make_cloud(position):
            cloud_out = VGroup(
                Circle(radius=0.6),
                Circle(radius=0.5).shift(LEFT * 0.5 + DOWN * 0.2),
                Circle(radius=0.4).shift(RIGHT * 0.5 + DOWN * 0.1),
                Circle(radius=0.45).shift(RIGHT * 0.1 + UP * 0.3),
            )
            cloud_out.set_fill(WHITE, opacity=1).set_stroke(width=0)
            cloud_out.scale(1.5)

            cloud_in = VGroup(
                Circle(radius=0.6),
                Circle(radius=0.5).shift(LEFT * 0.5 + DOWN * 0.2),
                Circle(radius=0.4).shift(RIGHT * 0.5 + DOWN * 0.1),
                Circle(radius=0.45).shift(RIGHT * 0.1 + UP * 0.3),
            )
            cloud_in.set_fill(BLACK, opacity=1).set_stroke(width=0)
            cloud_in.scale(1.4)

            cloud_in.to_edge(LEFT, buff=(position[0]+0.1))
            cloud_in.shift(UP * position[1])

            cloud_out.to_edge(LEFT, buff=position[0])
            cloud_out.shift(UP * position[1])

            return VGroup(cloud_out, cloud_in)

        cloud1 = make_cloud([1, 1.5])

        cloud2 = make_cloud([1, -1.5])



        self.play(FadeIn(rectangles))
        self.wait(0.5)

        self.play(FadeIn(ellipse))
        self.wait(0.5)
        self.play(FadeIn(cloud1), FadeIn(cloud2))
        self.wait(3)

        self.play(FadeOut(ellipse),
                  FadeOut(cloud1),
                  FadeOut(cloud2),
                  rectangles[0].animate.scale(1.1).move_to(ORIGIN).move_to(LEFT*4),
                  rectangles[1].animate.scale(1.1),
                  rectangles[2].animate.scale(1.1).move_to(ORIGIN).move_to(RIGHT*4)
                  )

        representaciones = Text("Representaciones").to_corner(UL)

        self.play(Write(representaciones))

        self.wait(2)

        text_1 = Paragraph("\"La lluvia es la", "precipitación de partículas", " líquidas de agua\"", font_size=19, alignment="center").move_to(ORIGIN).move_to(LEFT*4)
        text_2 = Text("Concepción", font_size=20).move_to(ORIGIN)
        text_3 = Text("Imaginación", font_size=20).move_to(ORIGIN).move_to(RIGHT*4)

        self.play(Write(text_1), Write(text_2), Write(text_3))

        self.wait(2)

        referirnos = Text("Nos permiten referirnos a objetos").to_corner(DL)

        self.play(Write(referirnos))

        text_no_lluvia = Paragraph("\"Ninguna precipitación", "de agua es lluvia\"", font_size=20, alignment="center").move_to(ORIGIN).move_to(RIGHT*4)
        consistencia = Text("Consistencia").to_corner(UL)
        eluc_consistencia = Text("No contradicción de las representaciones", font_size=28).to_corner(DL)

        self.play(FadeOut(representaciones),
                  FadeOut(rectangles[1]),
                  Transform(text_3, text_no_lluvia),
                  FadeOut(referirnos),
                  FadeOut(text_2)
                  )

        self.play(Write(consistencia), Write(eluc_consistencia))

        self.wait(1)

        cross = Cross(stroke_width=12.0)
        self.play(FadeIn(cross))

        self.wait(3)

        check = Text("✓", font_size=100, color=GREEN).move_to(ORIGIN)
        text_good = Paragraph("La lluvia es el ", " sudor de las nubes ", " después de hacer ejercicio", font_size=20, alignment="center").move_to(ORIGIN).move_to(RIGHT*4)
        self.play(
            Transform(cross, check),
            Transform(text_3, text_good)
        )

        self.wait(3)

        self.play(FadeOut(cross, text_3, rectangles[2], consistencia, eluc_consistencia))

        cosas = Text("Cosas").to_corner(UL)
        eluc_cosas = Text("Las cosas son aquello a lo que se refieren los objetos", font_size=28).to_corner(DL)
        image = ImageMobject("C:/Users/Usuario/PycharmProjects/Filosofia_presuposicional/media/images/gotas-lluvia-FREEPIK.jpg").scale(0.25).move_to(RIGHT*4.5)
        arrow = Arrow(LEFT, RIGHT)

        self.play(FadeIn(ellipse, image),
                  Write(cosas), Write(eluc_cosas), FadeIn(arrow))

        self.play(Wiggle(arrow))

        # Hablar de las cadenas de referencia.

        self.wait(2)

        rectangles[1].move_to(LEFT*3+DOWN*1.5)
        text_no_lluvia.move_to(LEFT*3+DOWN*1.5)

        ellipse_2 = ellipse.copy()
        image_2 = image.copy()

        arrow2 = Arrow(LEFT, RIGHT).move_to(DOWN*1.5)

        text_again = Paragraph("La lluvia es el ", " sudor de las nubes ", " después de hacer ejercicio", font_size=20, alignment="center").move_to(ORIGIN).move_to(LEFT*3+DOWN*1.5)

        verdad = Text("Verdad").to_corner(UL)
        eluc_verdad = Text("Correspondencia de una representación con la cosa a la que refiere", font_size=28).to_corner(DL)

        self.play(
            Write(verdad), Write(eluc_verdad),
            FadeOut(cosas, eluc_cosas),
            rectangles[0].animate.move_to(LEFT*3+UP*1.5),
            text_1.animate.move_to(LEFT*3+UP*1.5),
            FadeIn(rectangles[1], text_again),
            FadeIn(ellipse_2, image_2),
            FadeIn(arrow2),
            arrow.animate.move_to(UP*1.5),
            ellipse.animate.move_to(RIGHT*3+UP*1.5),
            image.animate.move_to(RIGHT*3+UP*1.5),
            ellipse_2.animate.move_to(RIGHT*3+DOWN*1.5),
            image_2.animate.move_to(RIGHT*3+DOWN*1.5)
        )

        self.wait(1)

        cross = Cross(stroke_width=12.0).scale(0.6)

        check.move_to(UP*2.5)
        cross.move_to(DOWN*0.5)

        self.play(FadeIn(check, cross))

        self.wait(3)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait(3)


class Facultades(Scene):
    def construct(self):
        facultades = Text("Facultades trascendentales").to_corner(UL)
        eluc_facultades = Text("Nos permtien formar representaciones", font_size=28).to_corner(DL)
        def make_cloud(position):
            cloud_out = VGroup(
                Circle(radius=0.6),
                Circle(radius=0.5).shift(LEFT * 0.5 + DOWN * 0.2),
                Circle(radius=0.4).shift(RIGHT * 0.5 + DOWN * 0.1),
                Circle(radius=0.45).shift(RIGHT * 0.1 + UP * 0.3),
            )
            cloud_out.set_fill(WHITE, opacity=1).set_stroke(width=0)
            cloud_out.scale(1.5)

            cloud_in = VGroup(
                Circle(radius=0.6),
                Circle(radius=0.5).shift(LEFT * 0.5 + DOWN * 0.2),
                Circle(radius=0.4).shift(RIGHT * 0.5 + DOWN * 0.1),
                Circle(radius=0.45).shift(RIGHT * 0.1 + UP * 0.3),
            )
            cloud_in.set_fill(BLACK, opacity=1).set_stroke(width=0)
            cloud_in.scale(1.4)

            cloud_in.move_to(ORIGIN)
            cloud_out.move_to(ORIGIN)

            # cloud_in.to_edge(LEFT, buff=(position[0]+0.1))
            cloud_in.shift(RIGHT * position[0])

            # cloud_out.to_edge(LEFT, buff=position[0])
            cloud_out.shift(RIGHT * position[0  ])

            return VGroup(cloud_out, cloud_in)


        cloud1 = make_cloud([-2, 0])

        cloud2 = make_cloud([2, 0])

        sens = Text("Sensibilidad", font_size=20).move_to(LEFT*2)
        entend = Text("Entendimiento", font_size=20).move_to(RIGHT*2)

        self.play(Write(facultades), FadeIn(cloud1, cloud2))
        self.play(Write(sens), Write(entend))
        self.play(Write(eluc_facultades))

        self.wait(3)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        rectangles = VGroup(*[Rectangle(width=2, height=1) for _ in range(3)]).move_to(LEFT)
        rectangles[0].shift(UP*2)
        rectangles[1].shift(ORIGIN)
        rectangles[2].shift(DOWN*2)

        self.play(FadeIn(rectangles))
        rectangles_copy = rectangles.copy()
        # rectangles.move_to(LEFT*4)
        # rectangles_copy.move_to(RIGHT*2)
        self.play(rectangles_copy.animate.move_to(RIGHT*2),
                  rectangles.animate.move_to(LEFT*4))

        referencia = Text("Referencia").to_corner(UL)
        eluc_referencia = Text("Nos dice de qué facultad proviene cada representación", font_size=28).to_corner(DL)

        image = ImageMobject("C:/Users/Usuario/PycharmProjects/Filosofia_presuposicional/media/images/Arcoiris.png").scale(0.25).move_to(LEFT*2)
        image2 = image.copy()
        image.move_to(LEFT*4+UP*2)
        image2.move_to(RIGHT*2+UP*2)

        manzana = Text("Manzana", font_size=20).move_to(LEFT*4)
        manzana2 = manzana.copy()
        manzana2.move_to(RIGHT*2)

        dios = Text("Dios", font_size=20).move_to(LEFT*4+DOWN*2)
        dios2 = dios.copy()
        dios2.move_to(RIGHT*2+DOWN*2)

        self.play(Write(referencia))
        self.play(Write(eluc_referencia),
                  rectangles.animate.move_to(LEFT*4),
                  rectangles_copy.animate.move_to(RIGHT*2)
                  )
        self.play(FadeIn(image, image2, manzana, manzana2, dios, dios2))

        self.wait(3)

        pert1 = Text("∈").move_to(LEFT*2.5+UP*2)
        pert2 = Text("∈").move_to(LEFT*2.5)
        pert3 = Text("∈").move_to(LEFT*2.5+DOWN*2)
        pert4 = Text("∈").move_to(RIGHT*3.5+UP*2)
        pert5 = Text("∈").move_to(RIGHT*3.5)
        pert6 = Text("∈").move_to(RIGHT*3.5+DOWN*2)
        self.play(Write(pert1),
                  Write(pert2),
                  Write(pert3),
                  Write(pert4),
                  Write(pert5),
                  Write(pert6))

        cloud1 = make_cloud([-1, 0]).shift(UP*2).scale(0.8)
        cloud2 = make_cloud([-1, 0]).scale(0.8)
        cloud3 = make_cloud([-1, 0]).shift(DOWN*2).scale(0.8)
        cloud4 = make_cloud([5, 0]).shift(UP*2).scale(0.8)
        cloud5 = make_cloud([5, 0]).scale(0.8)
        cloud6 = make_cloud([5, 0]).shift(DOWN*2).scale(0.8)

        self.play(FadeIn(cloud1, cloud2, cloud3, cloud4, cloud5, cloud6))

        sens.move_to(LEFT)
        entend.move_to(RIGHT*5)
        sens2 = sens.copy().shift(UP*2)
        sens3 = sens.copy().shift(DOWN*2)
        entend2 = entend.copy().shift(UP*2)
        entend3 = entend.copy().shift(DOWN*2)

        self.play(Write(sens),
                  Write(entend),
                  Write(sens2),
                  Write(entend3),
                  Write(sens3),
                  Write(entend2),
                  )

        self.wait(3)

        cross = Text("✗", font_size=70, color=RED).move_to(LEFT*2.5+DOWN*2)
        tick = Text("✓", font_size=70, color=GREEN).move_to(LEFT*2.5)

        cross2 = cross.copy().move_to(RIGHT*3.5+UP*2)
        tick2 = tick.copy().shift(UP*2)
        tick3 = tick.copy().shift(RIGHT*6)
        tick4 = tick3.copy().shift(DOWN*2)

        self.play(FadeIn(cross),
                  FadeIn(tick),
                  FadeIn(tick2),
                  FadeIn(tick3),
                  FadeIn(tick4),
                  FadeIn(cross2),
                  )

        self.wait(3)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        completitud = Text("Completitud").to_corner(UL)
        eluc_completitud = Text("Toda representación se origina en la sensibilidad o en el entendimiento", font_size = 28).to_corner(DL)

        self.play(Write(completitud))
        self.play(Write(eluc_completitud))

        rectangles[0].move_to(LEFT*5).scale(1.1)
        rectangles[1].move_to(RIGHT*2).scale(1.1)
        pert1.move_to(LEFT*3.5)
        pert2.move_to(RIGHT*3.5)
        cloud1.move_to(ORIGIN).move_to(LEFT*2)
        cloud2.move_to(RIGHT*5)

        self.play(FadeIn(rectangles[0]),
                  FadeIn(rectangles[1]),
                  FadeIn(pert1),
                  FadeIn(pert2),
                  FadeIn(cloud1),
                  FadeIn(cloud2),
                  )

        sens.move_to(LEFT*2)
        entend.move_to(RIGHT*5)

        disyuncion = Text("o").move_to(ORIGIN)

        representacion = Text("Representación", font_size=20).move_to(LEFT*5)
        representacion2 = representacion.copy().move_to(RIGHT*2)

        self.play(Write(sens), Write(entend), Write(disyuncion), Write(representacion), Write(representacion2))

        self.wait(3)


def hsl_to_hsv(h, s, l):
    v = l + s*min(l, 1-l)
    s = 0 if v==0 else 2*(1-l/v)
    return ManimColor.from_hsv(np.array([h, s, v]))


class Estetica1(Scene):
    def construct(self):
        sensibilidad = Text("Sensibilidad").to_corner(UL)
        eluc_sensibilidad = Text("Facultad de recibir información por los sentidos", font_size=28).to_corner(DL)

        self.play(Write(sensibilidad))
        self.play(Write(eluc_sensibilidad))

        width = 6
        height = 3
        pupil_radius = 0.7
        lash_count = 10
        lash_length = 0.5

        a = width / 2
        b = height / 2

        # Upper and lower eyelid as parametric curves
        upper_lid = ParametricFunction(
            lambda t: (t, b * np.cos(t/2), 0),
            t_range=(-PI, PI),
            color=BLUE_D,
            stroke_width=4,
        )

        lower_lid = ParametricFunction(
            lambda t: (t, -b * np.cos(t/2), 0),
            t_range=(-PI, PI),
            color=BLUE_D,
            stroke_width=4,
        )

        # Iris, pupil, and shine
        iris = Circle(radius=pupil_radius * 1.5, color=BLUE_D, fill_opacity=1)
        pupil = Circle(radius=pupil_radius, color=BLUE_E, fill_opacity=1)
        shine = Circle(radius=pupil_radius * 0.3, color=WHITE, fill_opacity=1)
        shine.shift(0.3 * LEFT + 0.3 * UP)

        # Center iris and pupil
        iris.move_to(ORIGIN)
        pupil.move_to(ORIGIN)

        # Eyelashes along the upper lid
        # lashes = VGroup()
        # for i in range(lash_count):
        #     t = PI - i * PI / (lash_count - 1)
        #     point = upper_lid.point_from_proportion(i / (lash_count - 1))
        #     # Compute outward normal vector

        eye = VGroup(upper_lid, lower_lid, iris, pupil, shine)
        eye.scale(0.5).move_to(3*LEFT)

        cosa = Ellipse(width=3, height=1.5, color=WHITE).move_to(RIGHT*3)
        venus = ImageMobject("C:/Users/Usuario/PycharmProjects/Filosofia_presuposicional/media/images/venus.jpg").scale(0.1).move_to(RIGHT*3)

        self.play(FadeIn(eye, cosa, venus))

        point1 = Dot().move_to(RIGHT*2)

        self.play(FadeIn(point1))
        self.play(point1.animate.move_to(LEFT*3))

        cuarteto = ImageMobject("C:/Users/Usuario/PycharmProjects/Filosofia_presuposicional/media/images/cuarteto.jpg").scale(0.5).move_to(RIGHT*3)

        oido = Text("(Imagen de oido)", font_size=20).move_to(LEFT*3)

        self.wait(1)

        self.play(FadeOut(point1), Transform(eye, oido), FadeOut(venus), FadeIn(cuarteto))

        wave = ParametricFunction(
            lambda t: (t, 0.1 * np.cos(40*t), 0),
            t_range=(-PI/8, PI/8),
            color=BLUE_D,
            stroke_width=4,
        ).move_to(RIGHT*2)

        self.play(FadeIn(wave))
        self.play(wave.animate.move_to(LEFT*3))

        self.wait(1)

        cloud = create_cloud()
        cloud.move_to(RIGHT*3)

        sensibilidad_little = Text("Sensibilidad", font_size=28).move_to(RIGHT*3)

        r_blanco2 = Rectangle(width=3, height=1.5, fill_opacity=0).move_to(LEFT*3)

        pert1 = Text("∈", font_size=80)

        representacion_sensible = Paragraph("Representación", "sensible", font_size=28, alignment="center").move_to(LEFT*3)
        cosa_text = Text("Cosa", font_size=28).move_to(RIGHT*3)

        arrow = Arrow(start=LEFT, end=RIGHT)

        self.play(Transform(eye, r_blanco2), FadeOut(cuarteto, wave), FadeOut(point1))
        self.play(Write(representacion_sensible), Write(cosa_text), FadeIn(arrow))
        self.wait(3)

        self.play(Transform(cosa, cloud), Transform(cosa_text, sensibilidad_little), FadeOut(arrow), FadeIn(pert1))

        self.wait(3)

        self.play(FadeOut(sensibilidad),
                  FadeOut(representacion_sensible),
                  FadeOut(eye),
                  FadeOut(pert1),
                  FadeOut(cosa_text),
                  FadeOut(eluc_sensibilidad),
                  FadeOut(cosa),
                  FadeOut(pert1)
        )

        self.wait(1)


class Estetica2(Scene):
    def construct(self):

        title = Text("¿Qué información nos llega a los sentidos?").to_corner(UL)
        ejemplos = Paragraph("- Colores", "- Sonidos", "- Olores", "- Calor", "- Felicidad", "- Dolor", "- ...", font_size=28).move_to(UP*1.5)


        self.play(Write(title))
        self.wait(1)
        self.play(Write(ejemplos))
        self.wait(3)

        sensacion = Text("Sensación", font_size=28).move_to(UP*1.5)

        self.play(Transform(ejemplos, sensacion))

        self.wait(3)

        no_solo = Text("Pero no solo eso... También:").to_edge(LEFT)

        self.play(Write(no_solo))

        self.wait(3)

        posicion = Text("La posición que ocupa una cosa", font_size=28).move_to(DOWN*1.5)
        momento = Text("El momento en el que pasa una cosa", font_size=28).move_to(DOWN*3)

        self.play(Write(posicion))
        self.play(Write(momento))

        self.wait(3)

        espacio = Text("Espacio", font_size=28).move_to(DOWN*1.5)
        tiempo = Text("Tiempo", font_size=28).move_to(DOWN*3)

        self.play(Transform(posicion, espacio))
        self.play(Transform(momento, tiempo))

        self.wait(3)

        morfe = Text("Morfé", font_size=28).move_to(DOWN*2.25)

        self.play(Transform(posicion, morfe), Transform(momento, morfe))

        self.wait(3)

        self.play(FadeOut(no_solo, momento))

        ejemplos2 = sensacion.copy()
        posicion2 = morfe.copy()


        self.play(ejemplos.animate.move_to(LEFT*1), ejemplos2.animate.move_to(RIGHT*6), posicion.animate.move_to(LEFT*1+0.5*DOWN), posicion2.animate.move_to(RIGHT*6+0.5*DOWN))

        cloud = create_cloud().move_to(RIGHT*2+UP*2)

        rainbow_high = [hsl_to_hsv(h/360, 1, 0.5) for h in range(361)]
        r = Rectangle(width=3, height=1.5, fill_opacity=0, sheen_direction=(RIGHT+UP)).set_color(color=rainbow_high).move_to(LEFT*4+0.25*DOWN)

        empirica = Paragraph("Representación", "empírica", font_size=28, alignment="center").move_to(LEFT*4+0.25*DOWN)

        r_blanco = Rectangle(width=3, height=1.5, fill_opacity=0, sheen_direction=RIGHT).move_to(RIGHT*3+0.25*DOWN)
        r_blanco2 = Rectangle(width=3, height=1.5, fill_opacity=0).move_to(LEFT*2+UP*2)
        sensibilidad = Text("Sensibilidad", font_size=28).move_to(RIGHT*2+UP*2)
        pert1 = Text("∈").move_to(UP*2)
        representacion_sensible = Paragraph("Representación", "sensible", font_size=28, alignment="center").move_to(LEFT*2+UP*2)

        puro = Paragraph("Representación", "pura", font_size=28, alignment="center").move_to(RIGHT*3+0.25*DOWN)

        self.play(Create(r), Create(r_blanco))

        self.play(Write(empirica), Write(puro))


        start = ejemplos2.get_left() + DOWN * 0.05
        end = ejemplos2.get_right() + DOWN * 0.05

        linea_tachado = Line(start, end, color=RED, stroke_width=6)

        self.play(Create(linea_tachado))

        self.wait(3)


        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        self.wait(1)

# with tempconfig({
#     "quality": "low_quality",  # Or "medium_quality", "low_quality", etc.
#     "save_last_frame": False,   # save a PNG of the last frame (-s)
#     "write_to_movie": True,
#     "preview": True,            # Opens the video after rendering
#     "output_file": "my_scene4",   # Optional: name of the output file
# }):
#     Estetica2().render()

