from manim import *


MY_GREEN = "#198C15"


class Logo(VMobject):

    def __init__(self):
        super().__init__()
        circle = Circle().set_stroke(WHITE).set_fill(MY_GREEN, opacity=1)
        name = MathTex("\\mathrm{H_2O}")
        self.add(circle, name)

class EpsilonDeltaScene(Scene):
    def get_delta_lines(self, x0, delta):

        result = VGroup()

        for x_val in [x0 - delta, x0 + delta]:
            line = DashedLine(
                x_val*RIGHT+config.frame_height/2*DOWN,
                x_val*RIGHT+config.frame_height/2*UP,
                color=YELLOW
            )
            result.add(line)
        
        return result
    
    def get_epsilon_lines(self, func, x0, delta):

        result = VGroup()

        for y_val in [func(x0 - delta), func(x0 + delta)]:
            line = DashedLine(
                y_val*UP+config.frame_width/2*LEFT,
                y_val*UP+config.frame_width/2*RIGHT,
                color=YELLOW
            )
            result.add(line)
        
        return result
    
    def get_limit_lines(self, x0, l):

        result = VGroup()
        
        line1 = DashedLine(
            x0*RIGHT+config.frame_height/2*DOWN,
            x0*RIGHT+config.frame_height/2*UP,
            color=YELLOW
        )
        line2 = DashedLine(
            l*UP+config.frame_width/2*LEFT,
            l*UP+config.frame_width/2*RIGHT,
            color=YELLOW
        )
        result.add(line1, line2)

        return result


class Thumbnail(EpsilonDeltaScene):

    def construct(self):

        title = Tex("$\\varepsilon$-$\\delta$ definition of limits").scale(2.5).to_edge(UP)
        text = Tex("Full explanation").scale(1.5).next_to(title, DOWN)
        group = VGroup(title, text)
        rec = SurroundingRectangle(group).set_stroke(WHITE).set_fill(BLACK, opacity=1)

        self.ax = NumberPlane()
        graph = self.ax.plot(self.func, discontinuities=[-1], color=RED)

        x0 = 1
        l = -1
        delta = 0.5
        
        delta_lines = self.get_delta_lines(x0, delta)
        epsilon_lines = self.get_epsilon_lines(self.func, x0, delta)
        limit_lines = self.get_limit_lines(x0, l)
        dot = Dot(self.ax.c2p(x0, l), color=BLACK).set_stroke(RED, width=4)

        logo = Logo().to_corner(DR)
        subscribe = Text("Subscribe", font="Arial", weight=BOLD).to_corner(DL)
        rec2 = SurroundingRectangle(subscribe, color=WHITE, corner_radius=0.2, buff=0.3)
        rec2.set_fill(PURE_RED, opacity=1)

        self.add(
            self.ax, graph, delta_lines, epsilon_lines, limit_lines, dot, rec, title,
            text, logo, rec2, subscribe
        )
    
    def func(self, x):
        return (x**3 - 1)/(x - 1) - 4