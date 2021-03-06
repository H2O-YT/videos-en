from manim import *
import csv
# Using csv for Example2
from random import random, uniform
# Using random for Example3


class Thumbnail(Scene):

    def construct(self):

        title = Tex("Text with and without \\LaTeX")
        title.set_color(YELLOW)
        title.scale(2)
        title.to_edge(UP)

        banner = ManimBanner()

        text = Tex("More examples!")
        text.scale(2)
        text.to_edge(DOWN)

        self.add(title, banner, text)


class Beginning(Scene):
    
    def construct(self):

        self.show_banner()
        self.show_text()

    def show_banner(self):

        banner = ManimBanner()

        self.play(banner.create())
        self.play(banner.expand())
        self.play(Unwrite(banner))

    def show_text(self):

        text = Text(
            "Check the video description.\n"
            +"There's a GitHub link where\n"
            +"you can see the source code\n"
            +"for each example.", font="Arial",
            weight=BOLD
        )

        self.play(Write(text), run_time=3.0)
        self.wait()


class Example1(Scene):

    def construct(self):
        
        self.initialize_stuff()
        self.animate_dimensions()

    def initialize_stuff(self):

        self.width = ValueTracker(4)
        self.height = ValueTracker(3)

        # Since Python variables save the last value setting, we use always_redraw which is an update function.
        
        rec = always_redraw(
            lambda: Rectangle(
                height=self.height.get_value(), width=self.width.get_value()
            ).set_fill(
                BLUE, opacity=1
            )
        )

        width_brace = always_redraw(lambda: Brace(rec, direction=UP))
        height_brace = always_redraw(lambda: Brace(rec, direction=RIGHT))

        width_text = always_redraw(
            lambda: Text(
                "width = "+str(np.round(self.width.get_value(), decimals=2)),
                font="Arial", weight=BOLD
            ).next_to(width_brace, UP)
        )
        height_text = always_redraw(
            lambda: Text(
                "height = "+str(np.round(self.height.get_value(), decimals=2)),
                font="Arial", weight=BOLD
            ).next_to(height_brace, RIGHT)
        )

        braces = VGroup(width_brace, height_brace)
        texts = VGroup(width_text, height_text)

        self.play(DrawBorderThenFill(rec))
        self.play(Write(braces))
        self.play(Write(texts))

    def animate_dimensions(self):

        self.set_dimensions(0.3, 0.5)
        self.set_dimensions(2, 1)
        self.set_dimensions(4, 3)
        self.set_dimensions(2, 2)
        self.wait()

    def set_dimensions(self, width, height):
        
        self.play(
            self.width.animate.set_value(width), self.height.animate.set_value(height)
        )


class Example2(Scene):
    # Vaccination in Chile. Data from
    # https://github.com/owid/covid-19-data/blob/master/public/data/vaccinations/country_data/Chile.csv

    def construct(self):

        self.show_title()
        self.initialize_ax()
        self.show_graph()
    
    def show_title(self):

        title = Tex("Vaccination in Chile")
        title.scale(2)
        title.to_edge(UP)

        text = Tex("Chile population in 2020: 19.12 million")
        text.next_to(title, DOWN)

        self.add(title, text)

    def initialize_ax(self):

        self.ax = Axes(x_range=[0, 8, 1], y_range=[17660000, 17730000, 10000])
        # range=[min, max, step]
        self.ax.add_coordinates(range(1, 8), range(17670000, 17730000, 20000))
        self.ax.scale(0.75)

        x_axis_label = self.ax.get_x_axis_label(
            Tex("Latest 7 days until 02/14/2022"),
            edge=DOWN, direction=DOWN
        )
        y_axis_label = self.ax.get_y_axis_label(
            Tex("Total people vaccinated in Chile").rotate(90*DEGREES),
            edge=LEFT, direction=LEFT
        )
        axis_labels = VGroup(x_axis_label, y_axis_label)

        self.play(Write(self.ax))
        self.play(Write(axis_labels))
    
    def show_graph(self):

        graph = self.ax.plot_line_graph(
            x_values=self.load_data()[0], y_values=self.load_data()[1]
        )
        
        self.play(Create(graph))

    def load_data(self):

        self.x_vals = list(range(1, 8))

        with open('Chile.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            self.y_vals = []
            for row in reader:
                self.y_vals.append(int(row['people_vaccinated']))
        self.y_vals = self.y_vals[-7:]

        return [self.x_vals, self.y_vals]


class Example3(Scene):

    def construct(self):
        
        self.initialize_stuff()
        self.start_generating_random_points()
    
    def initialize_stuff(self):

        title = Tex("Average distance between two\\\\points on the unit circle")
        title.scale(2)
        title.to_edge(UP)

        c = Circle(radius=1)
        self.points = []

        self.fixed_point = Dot(RIGHT)
        # RIGHT = np.array([1, 0])
        # And (1, 0) belongs to the unit circle
        self.line = Line(0.5*DOWN, 0.5*UP).set_color(YELLOW).to_edge(DOWN).shift(LEFT)
        # This line will divide rec into two parts: the tex part and the text part


        tex = MathTex("\\bar{d}").set_color(GREEN).next_to(self.line, LEFT)
        self.text = Text("ERROR", font="Digital-7").next_to(self.line, RIGHT)
        group = VGroup(tex, self.text)
        rec = SurroundingRectangle(group)
        
        self.play(Write(title))
        self.play(Create(c))
        self.play(Create(self.fixed_point))
        self.play(Write(group))
        self.play(Create(self.line))
        self.wait()

    def start_generating_random_points(self):
        
        def update_func(m):
            m.become(Text(str(np.round(self.average_distance(), decimals=3)), font="Digital-7"))
            m.set_color(BLUE)
            m.next_to(self.line, RIGHT)

        i = 0
        while i < 100:
            if i == 0:
                self.text.add_updater(update_func)
                # Since Python saves the last value setting, we added updated_func as self.text's updater
            self.generate_random_point()
            i += 1

    def generate_random_point(self):

        random_x = uniform(-1, 1)
        random_number = random()

        if random_number < 0.5:
            random_sign = 1
        else:
            random_sign = -1
        random_y = random_sign * np.sqrt(1 - random_x**2)
        self.points.append(random_x*RIGHT+random_y*UP)

        self.add(Line(self.fixed_point.get_center(), self.points[-1]), Dot(self.points[-1]))
        self.bring_to_front(self.fixed_point)
        # This just brings to front the mobject self.fixed_point
        self.wait(0.1)
    
    def average_distance(self):

        result = 0
        for point in self.points:
            result += (
                np.sqrt(
                    (self.fixed_point.get_center()[0]-point[0])**2 + (self.fixed_point.get_center()[1]-point[1])**2
                )
            )
        result /= len(self.points)
        return result


class Example4(Scene):

    def construct(self):

        self.initialize_stuff()
        self.changing_function_value()
    
    def initialize_stuff(self):

        ax = NumberPlane()
        self.tracker = ValueTracker(1)

        tex1 = MathTex("f", "(", "x", ",", "y", ")", "=", "x", "y")
        tex1.set_color_by_tex("x", YELLOW)
        tex1.set_color_by_tex("y", BLUE)
        tex1.set_color_by_tex("f", GREEN)

        slider_group = self.get_slider()
        group = VGroup(tex1, slider_group).arrange(DOWN).to_corner(UL)
        rec = SurroundingRectangle(group).set_fill(BLACK, opacity=1)

        graph = always_redraw(lambda: ax.plot_implicit_curve(
            lambda x,y: x*y - self.tracker.get_value(), color=RED
        ))

        self.play(Write(ax))
        self.play(Create(graph))
        self.play(DrawBorderThenFill(rec))
        self.play(Write(group))


    def get_slider(self):
        
        tex2 = MathTex("f", "(", "x", ",", "y", ")")
        tex2.set_color_by_tex("x", YELLOW)
        tex2.set_color_by_tex("y", BLUE)
        tex2.set_color_by_tex("f", GREEN)

        line = NumberLine(x_range=[-10, 10, 4], length=4)
        dot = always_redraw(
            lambda: LabeledDot(DecimalNumber(self.tracker.get_value(), color=BLACK), color=GREEN).move_to(
                line.n2p(self.tracker.get_value())
            ).scale(0.4)
        )
        slider = VGroup(line, dot)

        result = VGroup(tex2, slider).arrange(RIGHT)

        return result
    
    def changing_function_value(self):

        self.play(self.tracker.animate.set_value(8.0))
        self.wait()
        self.play(self.tracker.animate.set_value(0.2))
        self.wait()
        self.tracker.set_value(-1.0)
        self.play(self.tracker.animate.set_value(-7.0))
        self.wait()