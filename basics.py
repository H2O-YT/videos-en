from manim import *


MY_GREEN = "#198214"


class Logo(VMobject):

    def __init__(self, squared=False):

        super().__init__()
        shape = Circle(color=WHITE).set_fill(MY_GREEN, opacity=1)
        tex = MathTex("\\mathrm{H_2O}")

        if squared:
            shape = Square().set_stroke(width=0).set_fill(MY_GREEN, opacity=1)
        
        self.add(shape, tex)