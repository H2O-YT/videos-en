from manim import *


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
            ).next_to(height_brace, UP)
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
