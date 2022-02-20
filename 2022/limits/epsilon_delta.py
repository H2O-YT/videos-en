from manim import *


MY_GREEN = "#198C15"


class Logo(VMobject):

    def __init__(self):

        super().__init__()
        circle = Circle().set_stroke(WHITE).set_fill(MY_GREEN, opacity=1)
        name = MathTex("\\mathrm{H_2O}")
        self.add(circle, name)


class TexRainbow(Tex):

    def __init__(self, *tex_strings, **kwargs):

        super().__init__(*tex_strings, **kwargs)
        self.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)


class EpsilonDeltaScene(Scene):
    def get_delta_lines(self, x0, delta):

        result = VGroup()

        for x_val in [x0 - delta, x0 + delta]:
            line = DashedLine(
                x_val*RIGHT+config.frame_height/2*DOWN,
                x_val*RIGHT+config.frame_height/2*UP,
                color=YELLOW
            ).set_opacity(0.7)
            result.add(line)
        
        return result
    
    def get_epsilon_lines(self, func, x0, delta):

        result = VGroup()

        for y_val in [func(x0 - delta), func(x0 + delta)]:
            line = DashedLine(
                y_val*UP+config.frame_width/2*LEFT,
                y_val*UP+config.frame_width/2*RIGHT,
                color=YELLOW
            ).set_opacity(0.7)
            result.add(line)
        
        return result
    
    def get_limit_lines(self, x0, l):

        result = VGroup()
        
        line1 = DashedLine(
            x0*RIGHT+config.frame_height/2*DOWN,
            x0*RIGHT+config.frame_height/2*UP,
            color=YELLOW
        ).set_opacity(0.7)
        line2 = DashedLine(
            l*UP+config.frame_width/2*LEFT,
            l*UP+config.frame_width/2*RIGHT,
            color=YELLOW
        ).set_opacity(0.7)
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
        symbol = SVGMobject("symbol.svg").to_corner(DL)

        self.add(
            self.ax, graph, delta_lines, epsilon_lines, limit_lines, dot, rec, title,
            text, logo, symbol
        )
    
    def func(self, x):
        return (x**3 - 1)/(x - 1) - 4


class TeachFunctionsScene(Scene):
    
    def setup_function_stuff(self, function, function_string, x_values, discontinuities):
        self.function = function
        self.function_string = function_string
        self.x_values = x_values
        self.y_values = [function(x) for x in x_values]
        self.discontinuities = discontinuities
    
    def construct(self):

        self.show_function_mapping()

    def get_group(self, var_string, var_values, color):

        result = VGroup()

        for var in var_values:
            tex = MathTex(var_string, "=", var).set_color_by_tex(var_string, color)
            result.add(tex)
        
        result.arrange(DOWN)
        ellipse = Ellipse(width=result.width+2.0, height=result.height+2.0)
        ellipse.set_color(color)
        result.add(ellipse)
        
        return result
    
    def show_function_mapping(self):

        input_group = self.get_group("x", self.x_values, YELLOW)
        output_group = self.get_group("y", self.y_values, BLUE)
        groups = VGroup(input_group, output_group).arrange(RIGHT)

        arrow = CurvedArrow(
            *[group.get_top()+0.2*UP for group in groups]
        )
        function_tex = MathTex(self.function_string)
        function_tex.set_color(GREEN)
        function_tex.next_to(arrow, UP)
        arrow_group = VGroup(arrow, function_tex)

        all_groups = VGroup(*groups, arrow_group)
        
        for group in all_groups:
            self.play(Write(group))
            self.wait(2)


class FirstFunction(TeachFunctionsScene):

    def setup(self):
        self.setup_function_stuff(lambda x: 2*x-1, "f", [-3/4, 0, 1/2, 2], None)