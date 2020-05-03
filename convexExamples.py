from manimlib.imports import *
import os
import pyclbr
import math


class Two_Dimensional_Convex_Set_Demo(GraphScene):
	CONFIG = {
		"x_min": -2,
        "x_max": 20,
        "y_min": -2,
        "y_max": 10,
		"x_labeled_nums" :range(-2,20,2),
	}

	def construct(self):
		SCALE_VALUE = 3

		text_bank = [
			"Lets say we live on a 2 Dimensional plane",
			"And we have a set lets call him Chase",
			"We can pick two points on Chase",
			"Point 1",
			"Point 2",
			"Let's now draw a line",
			"between the two points",
			"lets see if we can get the line",
			"to appear out of Chase",
			"Thats right you can't",
			"That is the fundemental idea",
			"of a Convex set"
		]

		for index, sentence in enumerate(text_bank):
			text_bank[index] = TextMobject(sentence)

		convex_set_points = [
					np.array([-3,2.5,0]), 
					np.array([0,2.5,0]), 
					np.array([3,1.7 ,0]), 
					np.array([3,-1.5,0]),
					np.array([0,-1.5,0]), 
					np.array([-3,0,0])
				]
		for index, array in enumerate(convex_set_points):
			convex_set_points[index] = array/SCALE_VALUE
		convex_set = Polygon(*convex_set_points, fill_color="#FF0000", fill_opacity=1)
		LINE_START = np.array([-1,-1,0])
		LINE_END = np.array([2,1,0])
		
		LINE_START = LINE_START/SCALE_VALUE
		LINE_END = LINE_END/SCALE_VALUE

		# We create our line and its respective endpoint dots
		initial_line = Line(LINE_START, LINE_END)
		intial_first_dot = Dot(LINE_START)
		intial_second_dot = Dot(LINE_END)

		# We define the locations we want our line to travel to
		next_locations = np.array([
			[(-2, 2.5, 0), (2, -1, 0)],
			[(1, 1, 0), (2, 2, 0)],
			[(0, 1, 0), (0, 2.5, 0)],
			[(2, 1, 0), (-1, 2.5, 0)],
			[(-2, 2, 0), (-2, -0.5, 0)],
			[(-3, 0, 0), (3, -1.5, 0)],
			[(-3, 0, 0), (0, -1.5, 0)],
			[(-3, 0, 0), (0,2.5,0)]
		])
		next_locations = next_locations/SCALE_VALUE

		# position text
		text_bank[1].next_to(convex_set.get_corner(UP+RIGHT),UP)
		text_bank[2].next_to(convex_set.get_corner(DOWN+LEFT),DOWN)
		text_bank[3].next_to(intial_first_dot.get_corner(DOWN+LEFT), DOWN)
		text_bank[4].next_to(intial_second_dot.get_corner(UP+RIGHT), UP)
		text_bank[5].next_to(initial_line.get_corner(DOWN+RIGHT), DOWN)
		text_bank[6].next_to(text_bank[5], DOWN)
		text_bank[7].next_to(initial_line.get_corner(DOWN+RIGHT), DOWN)
		text_bank[8].next_to(text_bank[5], DOWN)
		text_bank[9].next_to(initial_line.get_corner(DOWN+RIGHT), DOWN)
		text_bank[11].next_to(text_bank[10], DOWN)

		self.play(FadeIn(text_bank[0]))
		# Here we will make our grid then render it
		self.setup_axes(animate=True)
		self.play(FadeOut(text_bank[0]))
		# We create our polygon which will be our convex set in the 2nd dimension
		
		
		self.play(FadeIn(text_bank[1]))
		self.play(ShowCreation(convex_set))
		self.play(FadeOut(text_bank[1]))

		# We define where we want our initial Line to start
		
		
		self.play(FadeIn(text_bank[2]))
		self.play(FadeOut(text_bank[2]))
		# We then animate the initial line onto the screen

		add_points = [
			FadeIn(text_bank[3]),
			FadeIn(text_bank[4]),
			ShowCreation(intial_first_dot),
			ShowCreation(intial_second_dot)
		]
		fade_out_point_text = [
			FadeOut(text_bank[3]),
			FadeOut(text_bank[4])
		]

		self.wait(.5)
		self.play(*add_points)
		self.wait(.5)
		self.play(*fade_out_point_text)
		self.wait(1)

		add_initial_line_text = [
			FadeIn(text_bank[5]),
			FadeIn(text_bank[6]),
			FadeOut(text_bank[5]),
			FadeOut(text_bank[6])
		]

		self.play(*add_initial_line_text[0:2])
		self.wait(1)
		self.play(*add_initial_line_text[2:4])
		self.play(ShowCreation(initial_line))

		theta0 = 0
		center_text = TextMobject("X$\\_0$ + ")
		end_text = TextMobject("X$\\_0$ + ")
		center_text.next_to(convex_set.get_corner(UP), UP)
		end_text.next_to(center_text[0], RIGHT)
		self.play(ShowCreation(center_text))
		self.play(ShowCreation(end_text))
		while theta0 < 1:
			point_on_set = theta0*LINE_START + (1 - theta0)*LINE_END
			self.play(ShowCreation(Dot(point_on_set)))
			self.play(FadeOut(Dot(point_on_set)))
			first_text = [
				TextMobject(str(theta0)),
				TextMobject(str(1 - theta0))
			]
			second_text = [
				TextMobject(str(theta0+.1)),
				TextMobject(str(1 - theta0+.1))
			]
			
			first_text[0].next_to(center_text,LEFT)
			second_text[0].next_to(center_text,LEFT)
			first_text[1].next_to(end_text, RIGHT)
			second_text[1].next_to(end_text, RIGHT)
			self.play(Transform(first_text[0],second_text[0]))
			self.play(FadeOut(first_text[0]))
			self.play(Transform(first_text[1],second_text[1]))
			self.play(FadeOut(first_text[1]))
			theta0 += round((theta0+.1)*100)/100
		
		try_to_get_line_outside = [
			FadeIn(text_bank[7]),
			FadeIn(text_bank[8]),
			FadeOut(text_bank[7]),
			FadeOut(text_bank[8])
		]
		self.play(*try_to_get_line_outside[0:2])

		
		# here we itterate over the next locations and then move each object to the correct
		# locations at the same time
		for first_point, second_point in next_locations:
			end_line = Line(first_point, second_point)
			end_first_dot = Dot(first_point)
			end_second_dot = Dot(second_point)
			lineseg_animation = []
			lineseg_animation.append(Transform(initial_line, end_line))
			lineseg_animation.append(Transform(intial_first_dot, end_first_dot))
			lineseg_animation.append(Transform(intial_second_dot, end_second_dot))
			self.play(*lineseg_animation)
		
		self.play(*try_to_get_line_outside[2:4])
		self.play(FadeIn(text_bank[9]))

		get_rid_of_leftovers = [
			FadeOut(text_bank[9]),
			FadeOut(convex_set),
			FadeOut(initial_line),
			FadeOut(intial_first_dot),
			FadeOut(intial_second_dot)
		]
		self.play(*get_rid_of_leftovers)
		
		self.play(FadeIn(text_bank[10]))
		self.play(FadeIn(text_bank[11]))

class non_convex_set_demo(GraphScene):
	CONFIG = {
		"x_min": -2,
        "x_max": 20,
        "y_min": -2,
        "y_max": 10,
		"x_labeled_nums" :range(-2,20,2),
	}
			
	def construct(self):
		SCALE_VALUE = 4

		text_bank = [
			"Let's take a look at",
			"a non Convex set"
		]
		for index, sentence in enumerate(text_bank):
			text_bank[index] = TextMobject(sentence)

		non_convex_set_points = [
			np.array([1,0,0]),
			np.array([2,0,0]),
			np.array([2.2,2,0]),
			np.array([1.5,3,0]),
		]
		for index, array in enumerate(non_convex_set_points):
			non_convex_set_points[index] = array/SCALE_VALUE
		
		non_convex_set = Polygon(*non_convex_set_points, fill_color="#FFC0CB", fill_opacity=1)
		# Text positions
		text_bank[1].next_to(text_bank[0],DOWN)

		self.setup_axes(animate=True)
		title_text = [
			FadeIn(text_bank[0]),
			FadeIn(text_bank[1]),
			FadeOut(text_bank[0]),
			FadeOut(text_bank[1])
		]
		self.play(*title_text[0:2])
		self.play(*title_text[2:4])

		self.play(FadeIn(non_convex_set))

			

		


class Plot6(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 10,
        "x_tick_frequency" : 0.5,
        "axes_color" : BLUE,
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : math.sin(x), color = GREEN)

        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.label_direction = UP
        # List of values of positions
        values_decimal_x=[0,0.5,1,1.5,3.35]
        # Transform positions to tex labels
        list_x = [*["%s"%i for i in values_decimal_x]]
        # List touples of (position,label)
        values_x = [
            (i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            tex = TexMobject(x_tex)
            tex.scale(0.7)
            tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(tex)
        self.play(
            Write(self.x_axis_labels),
            Write(self.x_axis),
            Write(self.y_axis)
        )

#class Code(Scene):
#	code = CodeMobject("Helloword.html",
#				coordinates=[-5,3],
#				run_time=3,
#				scale_factor=0.3,
#				line_spacing=0.2,
#				tab_spacing=0.6,
#				font="Monospac821 BT",
#				indentation_char="  ")
#	code.scale(1)
#	self.play(Write(code),run_time=1)
#	def draw_code_all_lines_at_a_time(self, code):
#		self.play(*[Write(code[i]) for i in range(code.__len__())], run_time=code.run_time)


class Test(ThreeDScene):
	def construct(self):
		self.set_camera_orientation(phi=45 * DEGREES)
		self.begin_ambient_camera_rotation(2)
		rect = Rectangle(width=3, height=3, fill_color= ORANGE, fill_opacity=0.4, stroke_color= BLACK)
		dot_temp = Dot(point=[0,1,3])
		line_to_dot = Line(ORIGIN, dot_temp)
		unit_vector = line_to_dot.get_unit_vector()
		dot = Dot(point=dot_temp.get_center(), radius= 1).set_color(GREEN)
		rect.rotate_to_match_vector(unit_vector)
		self.add(rect)
		self.add(line_to_dot)
		self.add(dot)
		self.wait(5)

