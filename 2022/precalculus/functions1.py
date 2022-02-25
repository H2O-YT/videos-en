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
func_str = ["2", lambda x: get_number_tex(x, parentheses=True), "-", "1"]
x_vals = [-0.75, 0, 0.5, 1]
steps = [[lambda x: get_number_tex(2*x), "-", "1"]]
discontinuities = None

def func(x):
    return 2*x-1


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
        self.wait()


class FunctionMapping1(FunctionMapping):

    def setup(self):
        self.setup_function_stuff(x_vals, steps, x_str, y_str, f_str, func_str)

    def func(self, x):
        return func(x)


class VisualizeFunction1(VisualizeFunction):

    def setup(self):
        self.setup_function_stuff(x_vals, discontinuities, x_str, y_str, f_str, func_str)
    
    def func(self, x):
        return func(x)


def get_string1(x):
    return get_number_tex(x)

def get_string2(x):
    if x-1 >= 0:
        return "{"+get_number_tex(x-1)+"^"
    else:
        return "{"+get_number_tex(x-1, parentheses=True)+"^"

def get_string3(x):
    return get_number_tex(x-1)+"}"

def get_string4(x):
    return "{"+get_number_tex((x-1)**3)

x_str2 = "x"
y_str2 = "y"
f_str2 = "g"
func_str2 = ["{(", get_string1, "-", "1", ")^", "3", "\\over", get_string1, "-", "1}"]
x_vals2 = range(-1, 3)
step1func2 = [get_string2, "3", "\\over", get_string3]
step2func2 = [get_string4, "\\over", get_string3]
steps2 = [step1func2, step2func2]
discontinuities2 = [RIGHT]

def func2(x):
    return (x-1)**3/(x-1)


class FunctionIntro2(FunctionIntro):

    def setup(self):
        self.setup_function_stuff(x_str2, y_str2, f_str2, func_str2)


class FunctionMapping2(FunctionMapping):

    def setup(self):
        self.setup_function_stuff(x_vals2, steps2, x_str2, y_str2, f_str2, func_str2)
    
    def func(self, x):
        return func2(x)


class VisualizeFunction2(VisualizeFunction):

    def setup(self):
        self.setup_function_stuff(x_vals2, discontinuities2, x_str2, y_str2, f_str2, func_str2)
    
    def func(self, x):
        return func2(x)


x_str3 = "t\\relax"
y_str3 = "y"
f_str3 = "h"
func_str3 = ["{1", "\\over", lambda x: get_number_tex(x)+"}"]
x_vals3 = [-3, -0.5, 0, 0.5, 3]
steps3 = None
discontinuities3 = [[0, None]]

def func3(x):
    return 1/x


class FunctionIntro3(FunctionIntro):

    def setup(self):
        self.setup_function_stuff(x_str3, y_str3, f_str3, func_str3)


class FunctionMapping3(FunctionMapping):

    def setup(self):
        self.setup_function_stuff(x_vals3, steps3, x_str3, y_str3, f_str3, func_str3)
    
    def func(self, x):
        return func3(x)


class VisualizeFunction3(VisualizeFunction):

    def setup(self):
        self.setup_function_stuff(x_vals3, discontinuities3, x_str3, y_str3, f_str3, func_str3)
    
    def func(self, x):
        return func3(x)


class FunctionDefinition(Scene):

    def construct(self):
        self.show_definition()
    
    def show_definition(self):

        title = TexRainbow("Definition").scale(2).to_edge(UP)
        definition1p1 = Tex("A ", "function")
        definition1p2 = MathTex("f").set_color(GREEN)
        definition1p3 = Tex("is ", "a ", "rule ", "that")
        definition1 = VGroup(definition1p1, definition1p2, definition1p3).arrange(RIGHT)
        definition2p1 = Tex("assigns ", "to ", "each ", "element")
        definition2p2 = MathTex("x", " \\in", "A")
        definition2p2.set_color_by_tex("x", YELLOW)
        definition2p2.set_color_by_tex("A", YELLOW)
        definition2 = VGroup(definition2p1, definition2p2).arrange(RIGHT)
        definition3p1 = Tex("an ", "\\textbf{unique} ", "element")
        definition3p2 = MathTex("y", "\\in", "B")
        definition3p2.set_color_by_tex("y", BLUE)
        definition3p2.set_color_by_tex("B", BLUE)
        definition3 = VGroup(definition3p1, definition3p2).arrange(RIGHT)
        definition = VGroup(definition1, definition2, definition3).arrange(DOWN).scale(2)

        aclaration1 = MathTex("y", "=", "f", "(", "x", ")")
        aclaration1.set_color_by_tex("y", BLUE)
        aclaration1.set_color_by_tex("f", GREEN)
        aclaration1.set_color_by_tex("x", YELLOW)
        aclaration2 = Tex("means")
        aclaration3 = MathTex("x").set_color(BLUE)
        aclaration4 = Tex("corresponds ", "to")
        aclaration5 = MathTex("y").set_color(YELLOW)
        aclaration6 = Tex("in")
        aclaration7 = MathTex("f").set_color(GREEN)
        aclaration = VGroup(aclaration1, aclaration2, aclaration3, aclaration4, aclaration5, aclaration6, aclaration7)
        aclaration.arrange(RIGHT).scale(1.5).to_edge(DOWN)

        self.play(GrowFromCenter(title))
        for part in definition:
            for group in part:
                if isinstance(group, Tex):
                    for tex_part in group:
                        self.add(tex_part)
                        self.wait(0.5)
                else:
                    self.add(group)
                    self.wait(0.5)
        for part in aclaration:
            if isinstance(part, Tex):
                for tex_part in part:
                    self.add(tex_part)
                    self.wait(0.5)
            else:
                self.add(part)
                self.wait(0.5)