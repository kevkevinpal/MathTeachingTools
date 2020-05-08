from manimlib.imports import *
import os
import pyclbr
import math

	



class integers(Scene):
	def construct(self):
		question = TextMobject("What does $\\mathbb{Z}$ mean?")
		self.play(FadeIn(question))
		self.wait(3)
		self.play(FadeOut(question))
		awnser = TextMobject("It is the set of any whole number (ie no fractions allowed)")
		number_line = NumberLine(include_numbers=True)
		awnser.next_to(number_line, UP)
		awnser_animation = [
			FadeIn(awnser),
			FadeIn(number_line)
			]
		self.play(*awnser_animation)
		self.wait(4)

class reals(Scene):
    def construct(self):
                question = TextMobject("What does $\\mathbb{R}$ mean?")
                self.play(FadeIn(question))
                self.wait(3)
                self.play(FadeOut(question))
                awnser = TextMobject("It is the set of any real number (ie decimals allowed)")
                numbers_to_show = [-5,-4.5,-4,-3.5,-3,-2.5]
                number_line = NumberLine(tick_frequency=.1,numbers_to_show=numbers_to_show, include_numbers=True)
                awnser.next_to(number_line, UP)
                awnser_animation = [
                        FadeIn(awnser),
                        FadeIn(number_line)
                        ]
                self.play(*awnser_animation)
                self.wait(4)

