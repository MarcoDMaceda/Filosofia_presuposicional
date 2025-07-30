from manim import *


TEXT_COLOR = BLACK
BACKGROUND_COLOR = WHITE
BOX_COLOR = GREEN
SENSATION_COLOR = RED
PURE_COLOR = BLUE

def create_prism(width, height, depth, color):
    """Creates a 2D VGroup that looks like a 3D prism."""
    front = Rectangle(width=width, height=height, fill_color=color, fill_opacity=0.8, stroke_color=BLACK)
    skew_vector = np.array([depth, depth * 0.5, 0])
    top = Polygon(
        front.get_corner(UL), front.get_corner(UR),
        front.get_corner(UR) + skew_vector, front.get_corner(UL) + skew_vector,
        fill_color=color, fill_opacity=0.95, stroke_color=BLACK
    )
    side = Polygon(
        front.get_corner(UR), front.get_corner(DR),
        front.get_corner(DR) + skew_vector, front.get_corner(UR) + skew_vector,
        fill_color=color, fill_opacity=0.85, stroke_color=BLACK
    )
    return VGroup(front, top, side)


class RepresScene(Scene):
    """
    A complete layout overhaul to faithfully recreate the source image's
    strict grid, alignment, and connector style. This version fixes all
    known runtime errors.
    """
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        self.create_mobjects()
        self.position_mobjects()
        self.animate_mobjects()

    def create_mobjects(self):
        """Defines all visual elements for the scene."""
        fs = 18  # A smaller font size for a perfect fit

        self.gegenstand = VGroup(
            create_prism(width=2, height=1, depth=0.4, color=BOX_COLOR),
            Text("Gegenstand", color=TEXT_COLOR, font_size=fs)
        )
        self.intuicion = Paragraph("Intuición", "(referencia inmediata\na un Gegenstand)", alignment="center", color=TEXT_COLOR, font_size=fs, line_spacing=0.9)
        self.multiplicidad = Paragraph("Multiplicidad", "de la intuición", alignment="center", color=TEXT_COLOR, font_size=fs, line_spacing=0.9)
        self.concepcion = Paragraph("Concepción", "(referencia mediata", "a un Gegenstand)", alignment="center", color=TEXT_COLOR, font_size=fs, line_spacing=0.9)
        self.cognicion = Paragraph("Cognición", "(referencia", "determinada a", "un objeto)", alignment="center", color=TEXT_COLOR, font_size=fs, line_spacing=0.9)
        self.repres_text = Paragraph("Representación", "(género)", alignment="center", color=TEXT_COLOR, font_size=fs + 2)       
        self.intu_intelectual = Paragraph("Intuición intelectual", "(origen en el", "entendimiento)", alignment="center", color=TEXT_COLOR, font_size=fs, line_spacing=0.9)
        self.null_symbol = Text("φ", color=TEXT_COLOR, font_size=36)
        self.intu_sensible = Paragraph("Intuición sensible", "(origen en el", "sensibilidad)", alignment="center", color=TEXT_COLOR, font_size=fs, line_spacing=0.9)
        self.sensacion = Text("Sensación", color=SENSATION_COLOR, font_size=fs)
        self.morfe = Text("Morfé", color=BLUE, font_size=fs).next_to(self.sensacion, RIGHT)
        self.sensacion_morfe = VGroup(self.sensacion, self.morfe)
        self.intu_empirica = Text("Intuición empírica", color=TEXT_COLOR, font_size=fs)
        self.intu_pura = Text("Intuición pura", color=TEXT_COLOR, font_size=fs)
        self.red_square = Square(side_length=0.15, color=SENSATION_COLOR, fill_opacity=1).set_stroke(width=0)
        self.blue_square1 = Square(side_length=0.15, color=PURE_COLOR, fill_opacity=1).set_stroke(width=0)
        self.blue_square2 = Square(side_length=0.15, color=PURE_COLOR, fill_opacity=1).set_stroke(width=0)
        
        self.concepcion_pura = Paragraph("Concepción", "pura o noción", "(origen en el", "entendimiento)", alignment="center", color=TEXT_COLOR, font_size=fs, line_spacing=0.9)
        self.juicio = Paragraph("Juicio", "(unificación de", "concepciones o juicios)", alignment="center", color=TEXT_COLOR, font_size=fs, line_spacing=0.9)
        self.cognicion_pura = Text("Cognición pura", color=TEXT_COLOR, font_size=fs)
        self.cognicion_empirica = Paragraph("Cognición empírica", "o experiencia", alignment="center", color=TEXT_COLOR, font_size=fs, line_spacing=0.9)
        self.categoria = Paragraph("Categoría", "(noción", "atómica)", alignment="center", color=TEXT_COLOR, font_size=fs, line_spacing=0.9)
        self.predicable = Text("Predicable", color=TEXT_COLOR, font_size=fs)
        self.combinacion = Paragraph("Combinación", "de categorías", alignment="center", color=TEXT_COLOR, font_size=fs, line_spacing=0.9)
        self.pred_desligado = Paragraph("Predicable", "totalmente", "desligado de la", "experiencia", alignment="center", color=TEXT_COLOR, font_size=fs, line_spacing=0.9)
        self.idea = Text("Idea", color=TEXT_COLOR, font_size=fs + 2)
        self.esquema_tras = Paragraph("Esquema", "trascendental", alignment="center", color=TEXT_COLOR, font_size=fs, line_spacing=0.9)
        self.esquema = Text("Esquema", color=TEXT_COLOR, font_size=fs)
        self.concepcion_empirica_final = Paragraph("Concepción", "empírica", alignment="center", color=TEXT_COLOR, font_size=fs, line_spacing=0.9)
        

    def position_mobjects(self):
        """Positions all Mobjects using a strict grid system to match the source image."""
        self.gegenstand[1].move_to(self.gegenstand[0][0].get_center())

        R_5, R_4, R_3, R_2, R_1 = 3 * UP, 1.5*UP, 0 * UP, 1.5 * DOWN, 3 * DOWN
        C0, C1, C2 = -6 * RIGHT, -3*RIGHT, 0*RIGHT
        C3, C4, C5 = 0 * RIGHT, 2 * RIGHT, 5 * RIGHT
        C6, C7 = 6 * RIGHT, 7 * RIGHT
        
        self.repres_text.move_to(C0 + R_3)
        self.multiplicidad.move_to(C1 + R_4)
        self.intuicion.move_to(C1 + R_5)
        self.gegenstand.move_to(C1 + R_3)
        self.concepcion.move_to(C1 + R_2)
        self.cognicion.move_to(C1 + R_1)
        
        self.intu_intelectual.move_to(C2 + R_5+0.3*UP)
        self.intu_sensible.move_to(C2 + R_4+0.5*UP)
        self.sensacion_morfe.next_to(self.intu_sensible, DOWN, buff=0.1).align_to(self.intu_sensible, LEFT)
        self.null_symbol.move_to(self.intu_intelectual.get_center() + 5.5*RIGHT)
        
        self.intu_empirica.move_to(C4 + R_4+0.8*UP+0.4*RIGHT)
        self.intu_pura.next_to(self.intu_empirica, DOWN, buff=0.4, aligned_edge=LEFT)
        self.blue_square1.next_to(self.intu_empirica, DOWN, buff=0.1)
        self.red_square.next_to(self.blue_square1, LEFT, buff=0.1)
        self.blue_square2.next_to(self.intu_pura, DOWN, buff=0.1)
        
        self.concepcion_pura.move_to(C3 + R_2)
        self.juicio.move_to(C3+R_3)
        
        self.cognicion_pura.move_to(C3 + R_1+0.3*UP+0.75*LEFT)
        self.cognicion_empirica.next_to(self.cognicion_pura, DOWN, buff=0.4, aligned_edge=LEFT)
        
        self.categoria.move_to(C4 + R_3)
        self.combinacion.move_to(C4+R_3+1*DOWN+1.25*RIGHT)
        self.predicable.move_to(C4+R_2)
        self.pred_desligado.move_to(C4+R_2+1*DOWN+1.25*RIGHT)
        self.idea.move_to(C4+R_1)

        self.esquema_tras.move_to(C5 + R_3)
        self.esquema.move_to(C5 + R_2)
        
        self.concepcion_empirica_final.move_to(C6 + R_1)

    def animate_mobjects(self):
        """Creates connectors and runs the animation, matching the source image's style."""
        # line_for_brace = Line(self.intuicion.get_edge_center(UP), self.cognicion.get_edge_center(DOWN))
        # main_brace = Brace(line_for_brace, direction=LEFT, buff=0.5).next_to(self.repres_text, RIGHT)
        # arrow_multi_intu = Arrow(self.multiplicidad.get_right(), self.intuicion.get_left(), color=TEXT_COLOR, buff=0.2)
        # arrow_intu_geg = Arrow(self.intuicion.get_bottom(), self.gegenstand.get_top(), color=TEXT_COLOR, buff=0.2)
        # arrow_geg_concep = DashedVMobject(Arrow(self.gegenstand.get_bottom(), self.concepcion.get_top(), color=TEXT_COLOR, buff=0.2), num_dashes=15)
        # arrow_concep_cog = Arrow(self.concepcion.get_bottom(), self.cognicion.get_top(), color=TEXT_COLOR, buff=0.2)
        
        # brace_intu = Brace(self.intuicion, direction=RIGHT, color=TEXT_COLOR)
        
        # *** FIX IS HERE ***
        # Removed the erroneous .get_center() calls.
        # fork_point_intu = brace_intu.get_tip()
        # horiz_line_intu = Line(fork_point_intu, fork_point_intu + 0.5*RIGHT, color=TEXT_COLOR)
        
        # elbow_to_intel = Elbow(width=0.8, angle=PI, color=TEXT_COLOR).set_points_as_corners([horiz_line_intu.get_end(), horiz_line_intu.get_end() + 1.7*UP, self.intu_intelectual.get_left()])
        # line_to_sensible = Line(horiz_line_intu.get_end(), self.intu_sensible.get_left(), color=TEXT_COLOR)
        # arrow_to_null = Arrow(self.intu_intelectual.get_right(), self.null_symbol.get_left(), color=TEXT_COLOR, buff=0.2)
        
        # brace_sensible = Brace(VGroup(self.intu_sensible, self.sensacion_morfe), direction=RIGHT, color=TEXT_COLOR)

        # *** AND FIX IS HERE ***
        # fork_point_sens = brace_sensible.get_tip()
        # horiz_line_sens = Line(fork_point_sens, fork_point_sens + 0.5*RIGHT, color=TEXT_COLOR)

        # line_to_empirica = Line(horiz_line_sens.get_end(), self.blue_square1.get_left(), color=TEXT_COLOR)
        # line_to_pura = Line(horiz_line_sens.get_end(), self.blue_square2.get_left(), color=TEXT_COLOR)

        # brace_concep = Brace(self.concepcion, direction=RIGHT, color=TEXT_COLOR)
        # arrow_concep_pura = Arrow(brace_concep.get_tip(), self.concepcion_pura.get_left(), color=TEXT_COLOR, buff=0.1)
        # elbow_concep_juicio = Elbow(width=1, color=TEXT_COLOR).set_points_as_corners([self.concepcion.get_bottom(), self.concepcion.get_bottom() + 1.25*DOWN, self.juicio.get_left()])
        
        # brace_cog = Brace(VGroup(self.cognicion_pura, self.cognicion_empirica), direction=LEFT, color=TEXT_COLOR)
        # line_cog_fork = Line(self.cognicion.get_right(), brace_cog.get_tip(), color=TEXT_COLOR)
        
        # arrow_concep_pura_cat = Arrow(self.concepcion_pura.get_right(), self.categoria.get_left(), color=TEXT_COLOR, buff=0.2)
        # arrow_cat_comb = Arrow(self.categoria.get_bottom(), self.combinacion.get_top(), color=TEXT_COLOR, buff=0.1)
        # arrow_comb_pred = Arrow(self.combinacion.get_bottom(), self.predicable.get_top(), color=TEXT_COLOR, buff=0.1)
        # arrow_pred_idea = Arrow(self.pred_desligado.get_bottom(), self.idea.get_top(), color=TEXT_COLOR, buff=0.2)
        # arrow_cat_esq_tras = Arrow(self.categoria.get_right(), self.esquema_tras.get_left(), color=TEXT_COLOR, buff=0.2)
        # arrow_pred_esq = Arrow(self.predicable.get_right(), self.esquema.get_left(), color=TEXT_COLOR, buff=0.2)
        # arrow_pura_esq_tras = Elbow(width=1, angle=-PI/2, color=TEXT_COLOR).set_points_as_corners([self.intu_pura.get_right(), self.intu_pura.get_right() + 2.5*RIGHT, self.esquema_tras.get_bottom()])
        # arrow_esq_tras_final = Arrow(self.esquema_tras.get_right(), self.concepcion_empirica_final.get_left(), color=TEXT_COLOR, buff=0.2)
        # arrow_esq_final = Arrow(self.esquema.get_bottom(), self.concepcion_empirica_final.get_top(), color=TEXT_COLOR, buff=0.2)

        R_5, R_4, R_3, R_2, R_1 = 3 * UP, 1.5*UP, 0 * UP, 1.5 * DOWN, 3 * DOWN
        C0, C1, C2 = -6 * RIGHT, -3*RIGHT, 0*RIGHT
        C3, C4, C5 = 0 * RIGHT, 2 * RIGHT, 5 * RIGHT
        C6, C7 = 6 * RIGHT, 7 * RIGHT

        brace_repres = BraceBetweenPoints(point_1=C1+R_1+1.25*LEFT+0.5*DOWN, point_2=C1+R_5+1.25*LEFT+0.5*UP, direction=LEFT, color=BLACK)

        brace_intuic = BraceBetweenPoints(point_1=C3+R_5+1*LEFT+0.9*UP, point_2=C3+R_4+1*LEFT, direction=LEFT, color=BLACK)

        brace_sensible = BraceBetweenPoints(point_1=C4+R_4+0.4*LEFT+UP, point_2=C4+R_4+0.4*LEFT-0.5*UP, color=BLACK)

        brace_concepcion = BraceBetweenPoints(point_1=C4+R_3+0.4*LEFT+0.5*UP, point_2=C4+R_1+0.4*LEFT+0.5*DOWN, color=BLACK)

        brace_cognicion = BraceBetweenPoints(point_1=C3+R_1+1.5*LEFT+0.5*UP, point_2=C3+R_1+1.5*LEFT+0.5*DOWN, color=BLACK)

        line_pura = Line(start=self.intu_pura.get_right(), end=C5+R_4+0.15*UP, color=BLACK, stroke_width=2)
        arrow_pura = Arrow(C5+R_4+0.15*UP, self.esquema_tras.get_top(), buff=0, color=BLACK, stroke_width=2)


        arrow_categ = Arrow(start=self.categoria.get_right(), end=self.esquema_tras.get_left(), color=BLACK, stroke_width=2)

        line_empir = Line(start=self.intu_empirica.get_right(), end=C6+R_4+0.8*UP, color=BLACK, stroke_width=2)
        arrow_empir = Arrow(start=C6+R_4+0.8*UP, end=self.concepcion_empirica_final.get_top(), color=BLACK, buff=0, stroke_width=2)

        
        # self.play(Write(self.repres_text), Create(main_brace))
        self.play(Write(self.repres_text))
        self.play(FadeIn(brace_repres))
        self.play(FadeIn(self.gegenstand))
        self.play(Write(self.multiplicidad))
        self.play(Write(self.intuicion))
        self.play(FadeIn(brace_intuic))
        # self.play(Write(self.multiplicidad), GrowArrow(arrow_multi_intu))
        # self.play(Write(self.intuicion), GrowArrow(arrow_intu_geg))
        # self.play(Write(self.concepcion), Create(arrow_geg_concep))
        # self.play(Write(self.cognicion), GrowArrow(arrow_concep_cog))
        self.next_section()
        
        # self.play(Create(brace_intu), Create(horiz_line_intu))
        # self.play(Create(elbow_to_intel), Create(line_to_sensible))
        
        self.play(Write(self.intu_intelectual), Write(self.intu_sensible))
        self.play(Write(self.sensacion_morfe))
        # self.play(Write(self.null_symbol))
        # self.play(GrowArrow(arrow_to_null), Write(self.null_symbol))
        # self.play(Create(brace_sensible), Create(horiz_line_sens))
        # self.play(Create(line_to_empirica), Create(line_to_pura))
        self.play(FadeIn(brace_sensible))
        self.play(Write(self.intu_empirica), Create(VGroup(self.red_square, self.blue_square1)))
        self.play(Write(self.intu_pura), Create(self.blue_square2))
        self.next_section()
        
        # self.play(Create(brace_concep))
        # self.play(Create(brace_concep), GrowArrow(arrow_concep_pura))
        self.play(Write(self.concepcion))
        self.play(Write(self.concepcion_pura))
        # self.play(Create(elbow_concep_juicio))
        self.play(Write(self.juicio))
        # self.play(GrowArrow(arrow_concep_pura_cat), Write(self.categoria))
        self.play(FadeIn(brace_concepcion))
        self.play(Write(self.categoria))
        # self.play(Write(self.combinacion), GrowArrow(arrow_cat_comb))
        self.play(Write(self.predicable))
        self.play(Write(self.combinacion))
        # self.play(Write(self.predicable), GrowArrow(arrow_comb_pred))
        self.play(Write(self.idea))
        self.play(Write(self.pred_desligado))
        # self.play(GrowArrow(arrow_pred_idea), Write(self.idea))
        self.next_section()

        # self.play(Create(brace_cog), Create(line_cog_fork))
        self.play(Write(self.cognicion))
        self.play(FadeIn(brace_cognicion))
        self.play(Write(self.cognicion_pura), Write(self.cognicion_empirica))
        self.next_section()

        self.play(Create(line_pura), Create(arrow_pura), Create(arrow_categ))
        self.play(Write(self.esquema_tras))

        # self.play(Write(self.esquema_tras), GrowArrow(arrow_cat_esq_tras))
        self.play(Write(self.esquema))
        # self.play(GrowArrow(arrow_pred_esq), Write(self.esquema))
        # self.play(Create(arrow_pura_esq_tras))
        # self.play(GrowArrow(arrow_esq_tras_final), GrowArrow(arrow_esq_final), Write(self.concepcion_empirica_final))
        self.play(Create(line_empir), Create(arrow_empir))
        self.play(Write(self.concepcion_empirica_final))
        self.wait(3)    
        


with tempconfig({
    "quality": "high_quality",  # Or "medium_quality", "low_quality", etc.
    "save_last_frame": False,   # save a PNG of the last frame (-s)
    "write_to_movie": True,
    "preview": True,            # Opens the video after rendering
    "output_file": "representaciones",   # Optional: name of the output file
}):
    RepresScene().render()

