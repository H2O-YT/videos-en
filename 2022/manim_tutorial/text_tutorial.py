from manim import *
import csv
# Using csv for an example


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