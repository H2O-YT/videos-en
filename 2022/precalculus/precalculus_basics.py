import sys
import os

this_folder = os.path.dirname(__file__)
previous_folder = os.path.dirname(this_folder)
path_folder = os.path.dirname(previous_folder)
sys.path.insert(0, path_folder)

from basics import *


class PrecalculusIntro(Scene):

    def construct(self):

        welcome = TexRainbow("W", "e", "lcom", "e").scale(2)
        to = Tex("\\textsc{To this precalculus course!}").scale(1.5)
        group = VGroup(welcome, to).arrange(DOWN)
        e1 = welcome[1]
        e2 = welcome[-1]
        rec1 = SurroundingRectangle(e1).set_color(TEAL)
        rec2 = SurroundingRectangle(e2).set_color(LIGHT_BROWN)
        logo = Logo()

        self.play(Write(welcome[:-1]))
        self.play(ReplacementTransform(e1.copy(), e2, path_arc=180*DEGREES))
        self.play(Create(rec1))
        self.play(ReplacementTransform(rec1, rec2))
        self.play(ReplacementTransform(rec2, to))
        self.wait()
        self.play(ShrinkToCenter(group))
        self.play(Write(logo))
        self.wait()