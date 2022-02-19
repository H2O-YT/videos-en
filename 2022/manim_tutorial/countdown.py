from manim import *


class Countdown(Scene):
    # self.setup method runs before self.construct. That will allow us to add our
    # countdown to the scene without self.construct
    def setup(self):
        # To create a countdown, we need a text constantly updating.
        # We'll use an update function.
        countdown = VGroup(*[VMobject() for _ in range(4)])
        self.seconds = 60
        # Here goes our updater.
        def countdown_updater(m:Mobject, dt):
            # We're using an updater where m is the mobject variable and dt
            # is the change in time. By default dt is the inverse of our frame rate (FPS).
            # We'll use ceil function because we don't want to get floats.
            self.seconds -= dt
            seconds_countdown = np.ceil(self.seconds)
            separator_text = Text(":", font="Digital-7")
            minutes_equation = (seconds_countdown - seconds_countdown % 60)/60
            minutes_str = str(int(minutes_equation))
            minutes_text = Text(minutes_str, font="Digital-7")
            seconds_equation = seconds_countdown % 60
            seconds_tens_str = str(int((seconds_equation - seconds_equation % 10)/10))
            seconds_units_str = str(int(seconds_equation % 10))
            seconds_tens_text = Text(seconds_tens_str, font="Digital-7")
            seconds_units_text = Text(seconds_units_str, font="Digital-7")
            for text in VGroup(separator_text, minutes_text, seconds_tens_text, seconds_units_text):
                if seconds_countdown > 10:
                    text.set_color(YELLOW)
                else:
                    text.set_color(RED)
            m[0].become(separator_text)
            m[1].become(minutes_text.next_to(countdown[0], LEFT))
            m[2].become(seconds_tens_text.next_to(countdown[0], RIGHT))
            m[3].become(seconds_units_text.next_to(countdown[2], RIGHT))
            m.to_edge(UP)
        # We'll add our updater to countdown.
        countdown.add_updater(countdown_updater)
        # Adding countdown to the scene.
        self.add(countdown)
    
    def construct(self):

        banner = ManimBanner()

        self.play(banner.create())
        self.play(banner.expand())
        self.wait(55)
        self.play(Unwrite(banner), run_time=1.5)


class Thumbnail(Scene):

    def construct(self):

        title = Tex("Countdown in Manim!")
        title.set_color(YELLOW)
        title.scale(2)
        title.to_edge(UP)

        banner = ManimBanner()

        text = Tex("With source code!")
        text.scale(2)
        text.to_edge(DOWN)

        self.add(title, banner, text)