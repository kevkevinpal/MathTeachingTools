from manimlib.imports import *
import os
import pyclbr
import math

	



class thereExists(Scene):
	def construct(self):
		question = TextMobject("What does $\\exists$ mean?")
		thereExistsSymbol = TextMobject("$\\exists$")
		self.play(FadeIn(question))
