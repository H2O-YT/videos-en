import sys
import os

path_folder = os.path.dirname(__file__)
sys.path.insert(0, path_folder)

from precalculus_basics import *


class Thumbnail(Scene):

    def construct(self):

        title = TexRainbow("What's a function?").scale(2.5).to_edge(UP)
        text = Tex("Inclusive video").scale(1.5).next_to(title, DOWN)
        rec = SurroundingRectangle(VGroup(title, text))
        rec.set_fill(BLACK, opacity=1)

        ax = NumberPlane()
        graph = ax.plot(lambda x: x**3-2, color=RED)

        symbol = SVGMobject("symbol.svg")
        logo = Logo()
        VGroup(symbol, logo).arrange(RIGHT).to_corner(DR)
        eq = MathTex("y", "=", "x", "^3", "-", "2")
        eq.set_color_by_tex("y", BLUE)
        eq.set_color_by_tex("x", YELLOW)
        eq.scale(2)
        eq.set_stroke(BLACK, width=10, background=True)
        eq.to_corner(DL)

        self.add(ax, graph, rec, title, text, logo, symbol, eq)


x_str = "x"
y_str = "y"
f_str = "f"
func_str = ["2", (lambda x: x if isinstance(x, str) else "("+str(x)+")"), "-", "1"]


class FunctionIntro1(FunctionIntro):

    def setup(self):
        self.setup_function_stuff(x_str, y_str, f_str, func_str)
    
    def construct(self):

        super().construct()
        text = Tex("But what's a function?")
        text.set_color(ORANGE)
        text.scale(1.5)
        text.to_edge(DOWN)

        self.play(FadeIn(text, shift=UP))
        self.wait(2)