from manim import *


MY_GREEN = "#198C15"


class Logo(VMobject):

    def __init__(self):
        super().__init__()
        circle = Circle().set_stroke(WHITE).set_fill(MY_GREEN, opacity=1)
        name = MathTex("\\mathrm{H_2O}")
        self.add(circle, name)


class Thumbnail(Scene):

    def construct(self):

        def func(x):
            return (x/3)**2

        title = Tex("Single variable derivative").scale(2).to_edge(UP)
        rec = SurroundingRectangle(title).set_stroke(WHITE).set_fill(BLACK, opacity=1)

        ax = Axes()
        labels = ax.get_axis_labels()

        graph = ax.plot(func, color = RED)
        secant_line = ax.get_secant_slope_group(
            1, graph, dx = 2, dx_label = "dx", dy_label = "dy", secant_line_length=100
        )
        dot1 = Dot(ax.c2p(1, func(1)))
        dot2 = Dot(ax.c2p(3, func(3)))

        logo = Logo().to_corner(DL)

        formula = MathTex(
            "f'(", "x", ")=\\lim_{", "h", "\\to 0}", "{f(", "x", "+", "h", ")-f(", "x",
            ")\\over", "h}"
        )
        formula.set_color_by_tex("x", YELLOW)
        formula.set_color_by_tex("h", BLUE)
        formula.scale(1.5)
        formula.to_edge(DR)
        rec2 = SurroundingRectangle(formula).set_fill(BLACK, opacity=1)

        self.add(ax, labels, graph, secant_line, dot1, dot2, rec, title, logo, rec2, formula)
