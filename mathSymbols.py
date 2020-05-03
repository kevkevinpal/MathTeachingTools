from manimlib.imports import *
import os
import pyclbr
import math

	



class thereExists(Scene):
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
