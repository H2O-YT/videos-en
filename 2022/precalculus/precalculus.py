from manim import *
from types import FunctionType
from copy import deepcopy


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

        title = Tex("Precalculus course").scale(2.5).to_edge(UP)
        text = Tex("From functions to limits").scale(1.5).next_to(title, DOWN)
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


class FunctionIntroduction(Scene):
    
    def setup_function_stuff(self, x_str, y_str, f_str, func_str):
        self.x_str = x_str
        self.y_str = y_str
        self.f_str = f_str
        self.func_str = func_str
    
    def construct(self):
        title = TexRainbow("Let's see a function").scale(2)
        y = MathTex(self.y_str, "=", self.f_str, "(", self.x_str, ")").scale(1.5)
        func = MathTex(self.f_str, "(", self.x_str, ")", "=", *self.func_str).scale(1.5)
        group = VGroup(title, y, func)
        for part in group[1:]:
            part.set_color_by_tex(self.x_str, YELLOW)
            part.set_color_by_tex(self.y_str, BLUE)
            part.set_color_by_tex(self.f_str, GREEN)
        group.arrange(DOWN)
        self.play(Write(title))
        self.wait()
        self.play(Write(group[1:]))
        self.wait()


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

        steps = deepcopy(self.steps)

        if x_val == None:
            for i in range(len(steps[0])):
                if isinstance(steps[0][i], FunctionType):
                    steps[0][i] = self.x_str
            tex = MathTex(self.f_str, "(", self.x_str, ")", "=", *steps[0])
            result.add(tex)
        
        else:
            for i in range(len(steps)):
                for j in range(len(steps[i])):
                    if isinstance(steps[i][j], FunctionType):
                        val = steps[i][j](x_val)
                        if val - int(val) == 0:
                            val = int(val)
                        steps[i][j] = val
                    if steps[i][j] == self.x_str:
                        steps[i][j] = "("+str(x_val)+")"
                tex = MathTex(self.f_str, "(", x_val, ")", "=", *steps[i])
                result.add(tex)
            val = self.function(x_val)
            if val - int(val) == 0:
                val = int(val)
            tex = MathTex(self.f_str, "(", x_val, ")", "=", val)
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

        result.add(x_group, y_group)
        result.arrange(RIGHT, buff=0.5)

        arrow = CurvedArrow(
            x_group[1][1].get_top()+0.2*UR,
            y_group[1][1].get_top()+0.2*UL,
            angle=-PI/4
        )
        arrow_tex = MathTex(self.f_str).set_color(GREEN).next_to(arrow, UP)
        arrow_group.add(arrow, arrow_tex)
        result.add(arrow_group)

        result.scale(0.8)

        return result
    
    def construct(self):
        self.show_function_mapping()
    
    def show_function_mapping(self):

        in_out_group = self.get_input_output_group()
        f_x = VGroup(*[self.get_function_steps_group(x) for x in [None, *self.x_vals]])
        y_f_x = VGroup(*[self.get_y_tex(x) for x in [None, *self.x_vals]])
        y_f_x.next_to(f_x, UP)

        x_group = in_out_group[0]
        y_group = in_out_group[1]
        arrow_group = in_out_group[2]

        f_x_general = f_x[0][0]
        y_f_x_general = y_f_x[0]

        self.play(Write(x_group))
        self.play(Write(y_f_x_general), Write(f_x_general))
        self.wait()

        x_vals_group = x_group[0]
        y_vals_group = y_group[0]

        for i in range(len(x_vals_group)):

            self.play(Indicate(x_vals_group[i]))
            self.wait()
            y_f_x_general.save_state()
            f_x_general.save_state()
            self.play(Transform(y_f_x_general, y_f_x[i+1]))

            for j in range(len(f_x[i+1])):
                self.play(Transform(f_x_general, f_x[i+1][j]))
                self.wait()
            
            self.play(Circumscribe(f_x_general))
            self.play(Indicate(y_f_x_general))
            self.wait()
            self.play(Write(y_vals_group[i]))
            
            arrow = Arrow(
                x_vals_group[i].get_right()+0.1*RIGHT, y_vals_group[i].get_left()+0.1*LEFT
            )
            self.play(Create(arrow))
            self.wait()
            self.play(Uncreate(arrow))
            self.play(Restore(f_x_general), Restore(y_f_x_general))
            self.wait()
        
        y_set_group = y_group[1]
        self.play(Write(y_set_group))
        self.play(Write(arrow_group))
        self.wait()


class FunctionIntro1(FunctionIntroduction):
    
    def setup(self):
        self.setup_function_stuff("x", "y", "f", ["2", "x", "-", "1"])
    
    def construct(self):
        super().construct()
        text = Tex("But what's a function?").scale(1.5)
        text.set_color(ORANGE).to_edge(DOWN)
        self.play(GrowFromCenter(text))
        self.wait()


class Function1(TeachFunctionScene):

    def setup(self):
        x_vals = [-3/4, 0, 1/2, 2]
        step1 = ["2", "x", "-", "1"]
        step2 = [lambda x: 2*x, "-", "1"]
        self.setup_function_stuff(self.func, x_vals, [step1, step2], "x", "y", "f")
    
    def func(self, x):
        return 2*x-1