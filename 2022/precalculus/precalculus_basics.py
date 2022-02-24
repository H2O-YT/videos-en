import sys
import os

this_folder = os.path.dirname(__file__)
previous_folder = os.path.dirname(this_folder)
path_folder = os.path.dirname(previous_folder)
sys.path.insert(0, path_folder)

from basics import *
from copy import deepcopy
from types import FunctionType


class PrecalculusIntro(Scene):

    def construct(self):

        welcome = TexRainbow("W", "e", "lcom", "e").scale(2)
        to = Tex("\\textsc{To this precalculus course!}").scale(1.5)
        group = VGroup(welcome, to).arrange(DOWN)
        e1 = welcome[1]
        e2 = welcome[-1]
        rec1 = SurroundingRectangle(e1).set_color(TEAL)
        rec2 = SurroundingRectangle(e2).set_color(LIGHT_BROWN)
        logo = Logo()

        self.play(Write(welcome[:-1]))
        self.play(ReplacementTransform(e1.copy(), e2, path_arc=180*DEGREES))
        self.play(Create(rec1))
        self.play(ReplacementTransform(rec1, rec2))
        self.play(ReplacementTransform(rec2, to))
        self.wait()
        self.play(ShrinkToCenter(group))
        self.play(Write(logo))
        self.wait()


class FunctionIntro(Scene):

    def setup_function_stuff(self, x_str, y_str, f_str, func_str):
        self.x_str = x_str
        self.y_str = y_str
        self.f_str = f_str
        self.func_str = func_str

    def construct(self):
        
        text = TexRainbow("Let's see a function!").scale(2)
        y_tex = MathTex(self.y_str, "=", self.f_str, "(", self.x_str, ")").scale(1.5)
        func_str = deepcopy(self.func_str)
        for i in range(len(func_str)):
            if isinstance(func_str[i], FunctionType):
                func_str[i] = func_str[i](self.x_str)
        f_tex = MathTex(self.f_str, "(", self.x_str, ")", "=", *func_str).scale(1.5)
        group = VGroup(text, y_tex, f_tex).arrange(DOWN)
        
        for tex in group[1:]:
            tex.set_color_by_tex(self.x_str, YELLOW)
            tex.set_color_by_tex(self.y_str, BLUE)
            tex.set_color_by_tex(self.f_str, GREEN)
        
        self.play(Write(text))
        self.play(GrowFromCenter(group[1:]))
        self.wait(2)


class FunctionMapping(Scene):

    def setup_function_stuff(self, x_vals, steps, x_str, y_str, f_str, func_str):
        self.x_vals = x_vals
        self.y_vals = []
        for x_val in x_vals:
            try:
                y_val = self.func(x_val)
            except:
                pass
            finally:
                y_val = "Impossible"
            self.y_vals.append(y_val)
        self.steps = steps
        self.x_str = x_str
        self.y_str = y_str
        self.f_str = f_str
        self.func_str = func_str
    
    def func(self, x):
        pass

    def get_y_group(self):

        result = VGroup()

        tex = MathTex(self.y_str, "=", self.f_str, "(", self.x_str, ")")
        result.add(tex)

        for x_val in self.x_vals:
            tex = MathTex(self.y_str, "=", self.f_str, "(", x_val, ")")
            result.add(tex)
        
        for tex in result:
            tex.set_color_by_tex(self.x_str, YELLOW)
            tex.set_color_by_tex(self.y_str, BLUE)
            tex.set_color_by_tex(self.f_str, GREEN)
        
        return result
    
    def get_f_steps_group(self):

        result = VGroup()

        func_str = deepcopy(self.func_str)

        for i in range(len(func_str)):
            if isinstance(func_str[i], FunctionType):
                func_str[i] = func_str[i](self.x_str)

        tex = MathTex(self.f_str, "(", self.x_str, ")", "=", *func_str)
        result.add(tex)

        for x_val, y_val in zip(self.x_vals, self.y_vals):

            group = VGroup()
            func_str = deepcopy(self.func_str)

            for i in range(len(func_str)):
                if isinstance(func_str[i], FunctionType):
                    func_str[i] = func_str[i](x_val)

            tex = MathTex(self.f_str, "(", self.x_str, ")", "=", *func_str)
            group.add(tex)

            steps = deepcopy(self.steps)
            
            for step in steps:
                for i in range(len(step)):
                    if isinstance(step[i], FunctionType):
                        step[i] = step[i](x_val)
                tex = MathTex(self.f_str, "(", x_val, ")", "=", *step)
                group.add(tex)
            
            if y_val != "Impossible":
                tex = MathTex(self.f_str, "(", x_val, ")", "=", check_and_convert_to_int(y_val))
            else:
                tex = Tex(y_val).set_color(RED)
            group.add(tex)

            result.add(group)
        
        for i in range(len(result)):
            if i == 0:
                result[i].set_color_by_tex(self.x_str, YELLOW)
                result[i].set_color_by_tex(self.y_str, BLUE)
                result[i].set_color_by_tex(self.f_str, GREEN)
            else:
                for tex in result[i]:
                    tex.set_color_by_tex(self.f_str, GREEN)
        
        return result
    
    def get_mapping_group(self):

        result = VGroup()

        x_group = VGroup()
        x_vals_group = VGroup()

        for x_val in self.x_vals:
            tex = MathTex(self.x_str, "=", x_val)
            x_vals_group.add(tex)

        x_vals_group.arrange(DOWN)
        x_group.add(x_vals_group)

        y_group = VGroup()
        y_vals_group = VGroup()

        for y_val in self.y_vals:
            if y_val != "Impossible":
                tex = MathTex(self.y_str, "=", y_val)
            else:
                tex = Tex(y_val).set_color(RED)
            y_vals_group.add(y_group)

        y_vals_group.arrange(DOWN)
        y_group.add(y_vals_group)

        total_groups = VGroup(x_group, y_group)
        group = VGroup(x_vals_group, y_vals_group).arrange(RIGHT, buff=4)
        colors = [YELLOW, BLUE]
        strings = ["A", "B"]

        for total_group, vals_group, color, string in zip(total_groups, group, colors, strings):

            for tex in vals_group:
                tex.set_color_by_tex(self.x_str, YELLOW)
                tex.set_color_by_tex(self.y_str, BLUE)

            shape_group = VGroup()
            
            ellipse = Ellipse(width = vals_group.width+1, height=vals_group.height+1)
            ellipse.set_color(color)
            ellipse.surround(vals_group)
            tex = MathTex(string).set_color(color).next_to(ellipse, UP)
            shape_group.add(ellipse, tex)

            total_group.add(shape_group)
        
        arrow_group = VGroup()
        set1 = x_group[1][1]
        set2 = y_group[1][1]
        arrow = CurvedArrow(
            set1.get_top()+0.1*UP, set2.get_top()+0.1*UP, angle=-90*DEGREES
        ).set_color(PURPLE)
        tex = MathTex(self.f_str).set_color(GREEN).next_to(arrow, UP)
        arrow_group.add(arrow, tex)
        result.add(x_group, y_group, arrow_group)

        return result