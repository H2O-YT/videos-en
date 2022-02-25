from manim import *


MY_GREEN = "#198214"

def check_and_convert_to_int(x):
    if x - int(x) == 0:
        x = int(x)
    return x

def get_number_tex(x, decimals=3, parentheses=False):
    if isinstance(x, str):
        return x
    else:
        if x - int(x) != 0:
            original_decimals = len(str(x).split(".")[1])
            if original_decimals <= decimals:
                x = np.round(x, decimals=original_decimals)
                x = str(x)
            else:
                x = np.round(x, decimals=decimals)
                x = str(x)+"\\ldots"
        else:
            x = check_and_convert_to_int(x)
            x = str(x)
        if parentheses:
            x = "("+x+")"
    return x


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


class Outro(Scene):

    def construct(self):
        title = TexRainbow("Thanks for watching").scale(2).to_edge(UP)
        text = Tex("Click anything you want here").next_to(title, DOWN)
        self.play(Write(title), run_time=1)
        self.play(GrowFromCenter(text), run_time=1)
        self.wait(18)