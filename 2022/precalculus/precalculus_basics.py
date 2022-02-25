import sys
import os

this_folder = os.path.dirname(__file__)
previous_folder = os.path.dirname(this_folder)
path_folder = os.path.dirname(previous_folder)
sys.path.insert(0, path_folder)

from basics import *
from copy import deepcopy
from types import FunctionType, NoneType


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
        self.wait()


class FunctionMapping(Scene):

    def setup_function_stuff(self, x_vals, steps, x_str, y_str, f_str, func_str):
        self.x_vals = x_vals
        self.y_vals = []
        for x_val in x_vals:
            try:
                y_val = self.func(x_val)
                self.y_vals.append(y_val)
            except:
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
            
            x_val_decimals = len(str(x_val).split(".")[1])

            if x_val_decimals <= 3:
                x_val_rounded = check_and_convert_to_int(np.round(x_val, decimals=x_val_decimals))

            else:
                x_val_rounded = check_and_convert_to_int(np.round(x_val, decimals=3))
                x_val_rounded = str(x_val_rounded)+"\\ldots"

            for i in range(len(func_str)):
                if isinstance(func_str[i], FunctionType):
                    func_str[i] = func_str[i](x_val_rounded)

            tex = MathTex(self.f_str, "(", x_val_rounded, ")", "=", *func_str)
            group.add(tex)

            if self.steps != None:

                steps = deepcopy(self.steps)
                
                for step in steps:
                    for i in range(len(step)):
                        if isinstance(step[i], FunctionType):
                            step[i] = step[i](x_val)
                            step_part_decimals = len(str(step[i]).split(".")[1])
                            if step_part_decimals <= 3:
                                step[i] = check_and_convert_to_int(np.round(step[i], decimals=step_part_decimals))
                            else:
                                step[i] = check_and_convert_to_int(np.round(step[i], decimals=3))
                                step[i] = str(x_val_rounded)+"\\ldots"
                    tex = MathTex(self.f_str, "(", x_val_rounded, ")", "=", *step)
                    group.add(tex)

            if y_val != "Impossible":
                y_val_decimals = len(str(y_val).split(".")[1])
                if step_part_decimals <= 3:
                    y_val_rounded = check_and_convert_to_int(np.round(y_val, decimals=y_val_decimals))
                else:
                    y_val_rounded = check_and_convert_to_int(np.round(y_val, decimals=3))
                    y_val_rounded = str(y_val_rounded)+"\\ldots"

                tex = MathTex(self.f_str, "(", x_val_rounded, ")", "=", y_val_rounded)
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
            x_val_decimals = len(str(x_val).split(".")[1])
            if x_val_decimals <= 3:
                x_val_rounded = check_and_convert_to_int(np.round(x_val, decimals=x_val_decimals))
            else:
                x_val_rounded = check_and_convert_to_int(np.round(x_val, decimals=3))
                x_val_rounded = str(x_val_rounded)+"\\ldots"

            tex = MathTex(self.x_str, "=", x_val_rounded)
            x_vals_group.add(tex)

        x_vals_group.arrange(DOWN)
        x_group.add(x_vals_group)

        y_group = VGroup()
        y_vals_group = VGroup()

        for y_val in self.y_vals:
            if y_val != "Impossible":
                y_val_decimals = len(str(x_val).split(".")[1])
                if y_val_decimals <= 3:
                    y_val_rounded = check_and_convert_to_int(np.round(y_val, decimals=y_val_decimals))
                else:
                    y_val_rounded = check_and_convert_to_int(np.round(y_val, decimals=3))
                    y_val_rounded = str(y_val_rounded)+"\\ldots"
                tex = MathTex(self.y_str, "=", y_val_rounded)
            else:
                tex = Tex(y_val).set_color(RED)
            y_vals_group.add(tex)

        y_vals_group.arrange(DOWN)
        y_group.add(y_vals_group)

        total_groups = VGroup(x_group, y_group)
        group = VGroup(x_vals_group, y_vals_group).arrange(RIGHT, buff=2)
        colors = [YELLOW, BLUE]
        strings = ["A", "B"]

        for total_group, vals_group, color, string in zip(total_groups, group, colors, strings):

            for tex in vals_group:
                tex.set_color_by_tex(self.x_str, YELLOW)
                tex.set_color_by_tex(self.y_str, BLUE)

            shape_group = VGroup()
            
            ellipse = Circle(radius=vals_group.width/2)
            ellipse.set_color(color)
            ellipse.surround(vals_group)
            tex = MathTex(string).set_color(color).next_to(ellipse, UP)
            shape_group.add(ellipse, tex)

            total_group.add(shape_group)
        
        arrow_group = VGroup()
        set1 = x_group[1][1]
        set2 = y_group[1][1]
        arrow = CurvedArrow(
            set1.get_top()+0.1*UP, set2.get_top()+0.1*UP, angle=-45*DEGREES
        ).set_color(PURPLE)
        tex = MathTex(self.f_str).set_color(GREEN).next_to(arrow, UP)
        arrow_group.add(arrow, tex)
        result.add(x_group, y_group, arrow_group)

        return result
    
    def construct(self):

        mapping_group = self.get_mapping_group()
        f_steps_group = self.get_f_steps_group()
        y_group = self.get_y_group()

        f_steps_group.to_edge(DOWN)
        y_group.next_to(f_steps_group, UP)

        x_map_group = mapping_group[0]
        y_map_group = mapping_group[1]
        arrow_group = mapping_group[2]
        
        x_vals_group = x_map_group[0]
        y_vals_group = y_map_group[0]

        f_general = f_steps_group[0]
        y_general = y_group[0]
        
        self.play(Write(x_map_group))
        self.play(Write(y_general))
        self.play(Write(f_general))

        for i in range(len(self.x_vals)):

            x_val = x_vals_group[i]
            self.play(Indicate(x_val))
            self.wait()

            f_general.save_state()
            y_general.save_state()

            f_steps = f_steps_group[1:][i]
            y_val1 = y_group[1:][i]

            for j in range(len(f_steps)):
                anims = [Transform(f_general, f_steps[j])]
                if j == 0:
                    anims.append(Transform(y_general, y_val1))
                self.play(*anims)
                self.wait()
            
            self.play(Circumscribe(f_general))
            self.play(Indicate(y_general))
            self.wait()
            
            y_val2 = y_vals_group[i]

            self.play(Write(y_val2))
            self.wait()

            arrow = Arrow(x_val.get_right()+0.1*RIGHT, y_val2.get_left()+0.1*LEFT)
            self.play(Create(arrow))
            self.wait()
            self.play(Uncreate(arrow))
            self.play(Restore(f_general), Restore(y_general))
            self.wait()
        
        y_group_set = y_map_group[1]
        self.play(Write(y_group_set))
        self.wait()
        self.play(Write(arrow_group))
        self.wait()


class VisualizeFunction(Scene):

    def setup_function_stuff(self, x_vals, discontinuities, x_str, y_str, f_str, func_str):
        self.x_vals = x_vals
        self.y_vals = []
        for x_val in x_vals:
            try:
                y_val = check_and_convert_to_int(self.func(x_val))
                self.y_vals.append(y_val)
            except:
                y_val = "Impossible"
                self.y_vals.append(y_val)
        self.discontinuities = discontinuities
        self.x_str = x_str
        self.y_str = y_str
        self.f_str = f_str
        self.func_str = func_str
    
    def func(self, x):
        pass

    def get_general_group(self):

        result = VGroup()

        y_general = MathTex(self.y_str, "=", self.f_str, "(", self.x_str, ")")
        result.add(y_general)

        func_str = deepcopy(self.func_str)

        for i in range(len(func_str)):
            if isinstance(func_str[i], FunctionType):
                func_str[i] = func_str[i](self.x_str)
        
        f_general = MathTex(self.f_str, "(", self.x_str, ")", "=", *func_str)
        result.add(f_general)

        for tex in result:
            tex.set_color_by_tex(self.x_str, YELLOW)
            tex.set_color_by_tex(self.y_str, BLUE)
            tex.set_color_by_tex(self.f_str, GREEN)
        
        result.arrange(DOWN)

        return result
    
    def get_x_vals(self):

        result = VGroup()

        for x_val in self.x_vals:
            tex = MathTex(self.x_str, "=", x_val)
            tex.set_color_by_tex(self.x_str, YELLOW)
            result.add(tex)
        
        result.arrange(DOWN)
        
        return result
    
    def get_y_vals(self):
        
        result = VGroup()

        for y_val in self.y_vals:
            if y_val != "Impossible":
                tex = MathTex(self.y_str, "=", y_val)
                tex.set_color_by_tex(self.y_str, BLUE)
                result.add(tex)
            else:
                tex = Tex(y_val).set_color(RED)
                result.add(tex)
        
        result.arrange(DOWN)

        return result

    def show_title_part(self):
        title = TexRainbow("Let's visualize our function!").scale(2)
        self.play(Write(title))
        self.wait()
        self.play(Unwrite(title))
        self.wait()

    def visualize_function(self):

        ax = NumberPlane().add_coordinates()

        if self.discontinuities == None:
            graph = FunctionGraph(self.func, color=ORANGE)
        else:
            discontinuities = set([discontinuity[0] for discontinuity in self.discontinuities])
            graph = FunctionGraph(self.func, color=ORANGE, discontinuities=discontinuities)

        general_group = self.get_general_group()
        x_vals = self.get_x_vals()
        y_vals = self.get_y_vals()

        group = VGroup(general_group, x_vals).arrange(DOWN).to_corner(UL)
        rec = always_redraw(lambda: SurroundingRectangle(group).set_fill(BLACK, opacity=1))

        self.play(Write(ax))
        self.play(Write(rec), Write(group))
        self.wait()
        self.play(Indicate(x_vals))
        self.wait()

        dots = VGroup()

        for x in self.x_vals:
            dot = Dot(ax.c2p(x, 0)).set_color(ORANGE)
            dots.add(dot)
            self.play(Create(dot))
        
        self.wait()
        self.play(group.animate.become(VGroup(general_group, y_vals).arrange(DOWN).to_corner(UL)))
        self.play(Indicate(group[1]))
        self.wait()

        for i in range(len(self.y_vals)):
            if self.y_vals[i] != "Impossible":
                self.bring_to_back(ax, dots[i])
                self.play(dots[i].animate.shift(self.y_vals[i]*UP))
            else:
                self.play(Uncreate(dots[i]))
        
        self.wait()

        text = Tex("Let's extend ", "$A$ ", "to more values!").to_edge(DOWN)
        text.set_color_by_tex("$A$", YELLOW)
        rec2 = SurroundingRectangle(text).set_fill(BLACK, opacity=1)
        self.play(Write(rec2), Write(text))
        self.wait(2)
        self.play(Unwrite(rec2), ShrinkToCenter(text))
        self.wait()
        self.play(FadeOut(dots))
        self.bring_to_back(ax, graph)
        self.play(Create(graph))

        if self.discontinuities != None:

            for i in range(len(self.discontinuities)):
                discontinuity = self.discontinuities[i]
                nondefined_points = VGroup()
                defined_points = VGroup()
                try:
                    y_val = self.func(discontinuity[0])
                    if discontinuity[1] != None:
                        if discontinuity[1] != y_val:
                            dot = Dot(discontinuity).set_fill(BLACK, opacity=1).set_stroke(ORANGE, width=4)
                            nondefined_points.add(dot)
                        else:
                            dot = Dot(discontinuity).set_fill(ORANGE, opacity=1).set_stroke(ORANGE, width=4)
                            defined_points.add(dot)
                        self.play(Create(dot))
                except:
                    if discontinuities[1] != None:
                        dot = Dot(discontinuity).set_fill(BLACK, opacity=1).set_stroke(ORANGE, width=4)
                        nondefined_points.add(dot)
                        self.play(Create(dot))

            self.wait()
            dot = nondefined_points[0].copy()
            tex = Tex("means the graph doesn't include that point")
            aclaration = VGroup(dot, tex).arrange(RIGHT).to_edge(DOWN)
            rec = always_redraw(lambda: SurroundingRectangle(aclaration).set_fill(BLACK, opacity=1))
            self.play(Write(rec), Write(aclaration))

            if len(defined_points) > 0:
                self.wait(2)
                dot = defined_points[0].copy()
                tex2 = Tex("means the graph includes that point")
                self.play(aclaration.animate.become(VGroup(dot, tex2).arrange(RIGHT).to_edge(DOWN)))

        self.wait(2)

    def construct(self):
        self.show_title_part()
        self.visualize_function()