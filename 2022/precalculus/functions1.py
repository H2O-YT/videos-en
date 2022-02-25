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
func_str = ["2", lambda x: x if isinstance(x, str) else "("+str(x)+")", "-", "1"]
x_vals = [-0.75, 0, 0.5, 1]
steps = [[lambda x: check_and_convert_to_int(2*x), "-", "1"]]
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
    return x

def get_string2(x):
    if x-1 >= 0:
        return "{"+str(x-1)+"^"
    else:
        return "{("+str(x-1)+")^"

def get_string3(x):
    return str(x-1)+"}"

def get_string4(x):
    return "{"+str((x-1)**3)

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


x_str3 = "t"
y_str3 = "y"
f_str3 = "h"
func_str3 = ["{1", "\\over", lambda x: x+"}" if isinstance(x, str) else str(x)+"}"]
x_vals3 = [-3, -0.5, 0, 0.5, 3]
steps3 = None
discontinuities3 = [np.array([0, None], dtype=float or NoneType)]

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