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