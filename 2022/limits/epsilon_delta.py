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


class TeachFunctionScene(Scene):

    def setup_function_stuff(self, function, x_vals, steps, x_str, y_str, f_str):
        self.function = function
        self.x_vals = x_vals
        self.steps = steps
        self.x_str = x_str
        self.y_str = y_str
        self.f_str = f_str

    def get_function_steps_group(self, x_val=None):
        result = VGroup()

        steps = self.steps

        if x_val == None:
            for i in range(len(steps[0])):
                if isinstance(steps[0][i], function):
                    steps[0][i] = self.x_str
            tex = MathTex(self.f_str, "(", self.x_str, ")", "=", *steps[0])
            result.add(tex)
        
        else:
            for i in range(len(steps)):
                for j in range(len(steps[i])):
                    if isinstance(steps[i][j], function):
                        steps[i][j] = steps[i][j](x_val)
                        if i == 0:
                            steps[i][j] = "("+str(x_val)+")"
                tex = MathTex(self.f_str, "(", x_val, ")", "=", *steps[i])
                result.add(tex)
            tex = MathTex(self.f_str, "(", x_val, ")", "=", self.function(x_val))
            result.add(tex)
        
        for part in result:
            part.set_color_by_tex(self.x_str, YELLOW)
            part.set_color_by_tex(self.f_str, GREEN)
            part.to_edge(DOWN)
        
        return result

    def get_y_tex(self, x_val=None):

        if x_val == None:
            tex = MathTex(self.y_str, "=", self.f_str, "(", self.x_str, ")")
        else:
            tex = MathTex(self.y_str, "=", self.f_str, "(", x_val, ")")
        
        tex.set_color_by_tex(self.f_str, GREEN)
        tex.set_color_by_tex(self.x_str, YELLOW)
        tex.set_color_by_tex(self.y_str, BLUE)
        
        return tex
    
    def get_input_output_group(self):
        
        x_vals = self.x_vals
        y_vals = [self.function(x) for x in self.x_vals]
        x_group = VGroup(VGroup(), VGroup())
        y_group = VGroup(VGroup(), VGroup())
        arrow_group = VGroup()
        result = VGroup()

        for x, y in zip(x_vals, y_vals):
            x_tex = MathTex(self.x_str, "=", x)
            x_tex.set_color_by_tex(self.x_str, YELLOW)
            x_group[0].add(x_tex)
            y_tex = MathTex(self.y_str, "=", y)
            y_tex.set_color_by_tex(self.y_str, BLUE)
            y_group[0].add(y_tex)
        
        x_group[0].arrange(DOWN)
        y_group[0].arrange(DOWN)

        colors = [YELLOW, BLUE]
        tex_groups = VGroup(x_group, y_group)
        tex_sets = VGroup(MathTex("A"), MathTex("B"))
        for tex_group, color, tex_set in zip(tex_groups, colors, tex_sets):
            ellipse = Ellipse(width=tex_group[0].width+1.0, height=tex_group[0].height+1.0)
            ellipse.set_color(color)
            ellipse.surround(tex_group)
            tex_set.next_to(ellipse, UP)
            tex_set.set_color(RED)
            tex_group[1].add(ellipse, tex_set)
        
        arrow = CurvedArrow(
            x_group[1][1].get_top()+0.2*UR,
            y_group[1][1].get_top()+0.2*UL,
            angle=-PI/4
        )

        result.add(x_group, y_group)
        result.arrange(RIGHT, buff=0.5)

        arrow_tex = MathTex(self.f_str).set_color(GREEN).next_to(arrow, UP)
        arrow_group.add(arrow, arrow_tex)
        result.add(arrow_group)

        return result
    

class Function1(TeachFunctionScene):

    def setup(self):
        x_vals = [-3/4, 0, 1/2, 2]
        step1 = ["2", lambda x: x, "-", "1"]
        step2 = [lambda x: 2*x, "-", "1"]
        steps = [step1, step2]
        self.setup_function_stuff(self.func, x_vals, steps, "x", "y", "f")
    
    def func(self, x):
        return 2*x-1

    def construct(self):

        group = self.get_input_output_group()
        f_tex = self.get_function_steps_group()
        y_tex = self.get_y_tex()
        y_tex.next_to(f_tex, UP)
        
        self.add(group, y_tex, f_tex)