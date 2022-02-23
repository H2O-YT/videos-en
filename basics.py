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


class TexRainbow(Tex):
    
    def __init__(self, *tex_strings, **kwargs):
        super().__init__(*tex_strings, **kwargs)
        self.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)