from manim import *
from scipy.fftpack import shift

# class ModelEQs(Scene):
# 	def construct(self):
# 		ODSys_R = Tex(r"$ \dot{R_i} = \rho_{i} + R_{i} \sum_{j} C_{ij} S_{j}$")

# 		ODSys_S = Tex(r"$\dot{S_i} = \epsilon S_{i} \sum_{j} C_{ij}^{T} R_{j} - \mu_{i} S_{i}.$")

# 		# self.play(Write(ODSys_R))
# 		ODSys_S.next_to(ODSys_R, DOWN)
# 		self.play(Write(ODSys_R), Write(ODSys_S))
# 		# self.wait(1)
# 		self.play(FadeOut(ODSys_R), FadeOut(ODSys_S))
# 		self.wait(3)

class titleSplash(Scene):
	def construct(self):
		main = Text("Relating diversity and stability \n in ecological dynamic models")
		sub1 = Text("Riley Kouns", font_size=25)
		sub2 = Text("with Ben Ridenhour", font_size=15)
		sub1.next_to(main, DOWN*2)
		sub2.next_to(sub1, DOWN*1)

		# self.play(sub1.animate(run_time=0.75)
		self.play(FadeIn(main, run_time=3.5))
		self.play(FadeIn(sub1,sub2, shift=UP, run_time=2))
		self.wait(3)
		self.play(FadeOut(main, sub1,sub2))
		self.wait(3)

class intro(Scene):
	def construct(self):
		title = Tex("Problem Motivation")
		title.to_edge(UP)
		bound = Tex(r"$\alpha$",  r"$<$", r"$(NC)^{-\frac{1}{2}}$", font_size=60)
		bound_name = Tex(r"Bound within which communities will almost certainly not crash", font_size=35)
		bound_name.next_to(bound, DOWN*2.5)

		sub_bound = Tex(r"$\alpha$", r"?", font_size=70)


		self.play(FadeIn(title))
		self.play(Write(bound))
		self.wait(1)
		self.play(FadeIn(bound_name, shift=UP))
		self.wait(3)
		framebox1 = SurroundingRectangle(bound[2], buff = .1)
		framebox2 = SurroundingRectangle(bound[0], buff = .1)
		self.play(
			Create(framebox1),
		)
		self.wait(3)
		self.play(
			ReplacementTransform(framebox1,framebox2, run_time=3),
		)

		self.wait(3)

		self.play(Uncreate(framebox2))


		self.play(TransformMatchingTex(bound,sub_bound), FadeOut(bound_name, shift=DOWN))
		caption1 = Tex(r"Equilibrium is\textquotedblleft baked\textquotedblright  into the Jacobian", font_size=35)
		caption2 = Tex(r"How might we study diversity and stability simultaneously?", font_size=35)
		caption1.next_to(sub_bound, 2.5*DOWN)
		caption2.next_to(sub_bound, 2.5* DOWN)
		self.play(FadeIn(caption1, shift=UP))
		self.wait(3)
		self.play(TransformMatchingTex(caption1,caption2))
		self.wait(3)
		self.play(Unwrite(sub_bound, reverse=True))
		self.play(FadeOut(title))
		self.play(caption2.animate(run_time=1.5).shift(UP*1))
		self.wait(3)
		self.play(FadeOut(caption2, shift=DOWN))
		self.wait(2)


class worksCited(Scene):
	def construct(self):
		main = Text("Works Cited")
		self.add(main.to_edge(UP))
		self.play(FadeIn(main, run_time=1))

		# work1 = Tex(r"May, R. Will a Large Complex System be Stable?. \textit{Nature} \textbf{238}, 413–414 (1972). https://doi.org/10.1038/238413a0", font_size=20)
		# work2 = Tex(r"Butler, S., O’Dwyer, J.P. Stability criteria for complex microbial communities. \textit{Nat Commun} \textbf{9}, 2970 (2018). https://doi.org/10.1038/s41467-018-05308-z", font_size=20)
		# work3 = Tex(r"Arnoldi, J-F. et al. Resilience, reactivity and variability : A mathematical comparison of ecological stability measures. \textit{Journal of Theoretical Biology}. \textbf{389}. (2015). 10.1016/j.jtbi.2015.10.012", font_size=20)
		# work1.next_to(main, DOWN*2)
		# work2.next_to(work1, DOWN)
		# work3.next_to(work2, DOWN)
		# works = VGroup(work1,work2,work3)
		# works.arrange(UP, center=False, aligned_edge=LEFT)  

		work = Tex(r"\hangindent= 0.7cm \begin{flushleft} May, R. Will a Large Complex System be Stable?. \textit{Nature} \textbf{238}, 413–414 (1972). https://doi.org/10.1038/238413a0 \\ \vspace{5mm} Jost, L. Partitioning Diversity into Independent Alpha and Beta Components. \textit{Ecology}, \textbf{88}, 2427-2439. (2007) http://dx.doi.org/10.1890/06-1736.1 \\ \vspace{5mm} Arnoldi, J-F. et al. Resilience, reactivity and variability : A mathematical comparison of ecological stability measures. \textit{Journal of Theoretical Biology}. \textbf{389}. (2015). 10.1016/j.jtbi.2015.10.012 \\ \vspace{5mm} Butler, S., O’Dwyer, J.P. Stability criteria for complex microbial communities. \textit{Nat Commun} \textbf{9}, 2970 (2018). https://doi.org/10.1038/s41467-018-05308-z \\ \vspace{5mm} The Manim Community Developers. (2022). Manim – Mathematical Animation Framework (Version v0.16.0) [Computer software]. https://www.manim.community/\end{flushleft}", font_size=25)
		self.play(FadeIn(work))
		self.wait(2)
		# manim_credit = Tex(r"Animated in manim", font_size=35)
		# manim_credit.next_to(work, DOWN*4)
		# self.play(Write(manim_credit))
		self.wait(3)

		# self.play(FadeIn(works, run_time=1.5))


# class odEQs(Scene):
# 	def construct(self):
# 		ODSys = MathTex(r" \dot{R_i} & = \rho_{i} + R_{i} \sum_{j}^{N} C_{ij} S_{j} \\ \dot{S_i} & = \epsilon S_{i} \sum_{j}^{N} C_{ij}^{T} R_{j} - \mu_{i} S_{i}.")
# 		self.play(Write(ODSys))
# 		self.wait(3)
# 		self.play(FadeOut(ODSys))
# 		self.wait(1)


class EQs(Scene):
	def construct(self):
		subcol1 = BLUE_B
		subcol2 = GOLD_A

		title1 = Text("Population Dynamic Models", font_size=45)
		self.add(title1.to_edge(UP))

		glvSys = MathTex(r"\dot{S_i}=r_i S_i (1-\frac{S_i}{k_i}) + S_i \sum_{j=1, j\neq i}^N (a_{i,j} S_j)", color=subcol1)

		self.play(Write(glvSys))
		# self.play(Write(glvGroup))
		self.wait(1)
		self.play(glvSys.animate(run_time=0.75).shift(UP*0.5 + LEFT*4).scale(0.65))
		# self.play(FadeOut(glvGroup, shift=UP*2 + LEFT*2))
		glvText = Text("Generalized Lotka-Volterra", font_size=32, color=subcol1)
		glvText.next_to(glvSys, UP*1)
		self.play(Write(glvText))
		glvGroup = VGroup(glvText, glvSys)

		# gLV Bullet List
		glvList = BulletedList("Standard for population dynamics", "Not tailored to particular species", height=6, width=6)
		glvList.set_color_by_tex("Standard for population dynamics", subcol1)
		glvList.set_color_by_tex("Not tailored to particular species", subcol1)
		glvList.next_to(glvGroup, DOWN*2).to_edge(DOWN).shift(UP*0.5)
		self.play(Write(glvList))
		self.wait(2)

		# Divider
		median = Line((0,2,0), (0,-4,0))
		self.play(Write(median))

		# O'Dwyer
		odSys = MathTex(r" \dot{R_i} & = \rho_{i} + R_{i} \sum_{j=1}^{N} C_{ij} S_{j} \\ \dot{S_i} & = \epsilon S_{i} \sum_{j=1}^{N} C_{ij}^{T} R_{j} - \mu_{i} S_{i}", color=subcol2)
		odText = Text("Butler Resource-competition", font_size=32, color=subcol2)
		odText.next_to(glvText, RIGHT*9.25)
		odText.shift(DOWN*0.05)

		odSys.scale(0.65).next_to(odText, DOWN*0.5)
		self.play(Write(odSys))
		self.wait(1)
		self.play(odSys.animate(run_time=0.75))
		self.play(Write(odText))

		odGroup = VGroup(odText, odSys)

		# O'Dwyer list
		# odList.next_to(glvGroup, DOWN*2).to_edge(DOWN).shift(UP*1)
		odList = BulletedList("\"Numerical difficulties\"", "Designed for microbial interactions", height=6, width=6)
		odList.set_color_by_tex("\"Numerical difficulties\"", subcol2)
		odList.set_color_by_tex("Designed for microbial interactions", subcol2)
		odList.next_to(odGroup, DOWN*2).to_edge(DOWN).shift(UP*0.5)
		self.play(Write(odList))
		self.wait(2)

		#Clean-up
		self.wait(1)
		self.play(Unwrite(glvSys, reverse=True), Unwrite(glvList, reverse=True))
		self.play(Unwrite(odSys, reverse=True), Unwrite(odList, reverse=True))
		self.play(glvText.animate().shift(DOWN*1), odText.animate().shift(DOWN*1))
		self.play(Unwrite(title1, reverse=True), Unwrite(median, reverse=True))



	### Section E
		title2 = Text("Now, to compare stability and diversity...", font_size=35)
		self.add(title2.to_edge(DOWN).shift(UP*2))
		self.play(Write(title2))
		self.wait(3)


# class scatter(Scene):
# 	def construct(self):
# 		import pandas as pd
# 		coords = pd.read_csv(r"C:/Users/riley/Microbiome/animation/CSVs/gLV2.csv", index_col=0)

# 		# axes = Axes(
# 		# 	# y_range = [coords.iloc[:,0].min(), coords.iloc[:,0].max(), 1],
# 		# 	y_range = [0,10, 1],
# 		# 	# x_range = [coords.iloc[:,-1].min(), coords.iloc[:,-1].max(), 0.5],
# 		# 	x_range = [1.8, 2.0, 1], 
# 		# 	x_length=25,
# 		# 	axis_config={"include_numbers": True},
# 		# ).add_coordinates()
# 		# axes.to_edge(UL)
# 		# axis_labels = axes.get_axis_labels(x_label='D', y_label='\mathcal{R}_{0}')
# 		# # self.play(FadeIn(axes))
# 		# self.add(axes)
# 		# 


# 		plane = NumberPlane(
#             x_range = (0, 7),
#             y_range = (0, 5),
#             x_length = 7,
#             axis_config={"include_numbers": True},
#         )

# 		plane.center()

# 		gLV2_group = VGroup()
# 		for i in range(coords.shape[0]): 
# 			point = Point(location=[coords.iloc[i,-1],coords.iloc[i,0] , 1], color=BLUE_B)
# 			# axis.coords_to_point
# 			# self.add(point)
# 			# gLV2_group.add(point)
# 		# self.play(FadeIn(gLV2_group))

# 		self.add(plane.coords_to_point([coords.iloc[0,-1], coords.iloc[0,0]]))

# 		# for i in range(10):
# 		# 	point = Point(location=[i,3,1], color=GOLD_E)
# 		# 	self.add(point)


# 		# graph = axes.plot(lambda x: x**2,
# 		# 	color = YELLOW,
# 		# 	# x_range = [coords.iloc[:,-1].min(), coords.iloc[:,-1].max()]
# 		# 	x_range = [1.8, 2.0, 1]
# 		# )

# 		line_graph = plane.plot_line_graph(
#             x_values = [0, 1.5, 2, 2.8, 4, 6.25],
#             y_values = [1, 3, 2.25, 4, 2.5, 1.75],
#             line_color=GOLD_E,
#             vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
#             stroke_width = 4,
#         )

		

# 		# self.play(Create(graph))
# 		self.add(plane,line_graph)



# 		self.wait(2)
# 		# dots = VGroup(*[Dot().move_to(self.coords_to_point(coord[0],coord[1])) for coord in coords])
# 		# self.add(dots)
# 		# print(coords)



# ### OD System
		
# 		ODSys = MathTex(r" \dot{R_i} & = \rho_{i} + R_{i} \sum_{j}^{N} C_{ij} S_{j} \\ \dot{S_i} & = \epsilon S_{i} \sum_{j}^{N} C_{ij}^{T} R_{j} - \mu_{i} S_{i}.")
# 		# self.play(Write(ODSys))
# 		# self.wait(3)
# 		# self.play(FadeOut(ODSys))
# 		# self.wait(1)

class Diversity(Scene):
	def construct(self):
		title = Text("Diversity Indices")
		title.to_edge(UP)

		self.play(FadeIn(title))

		question = Tex(r"How can we quantify the \textquotedblleft diversity\textquotedblright of communities \\that always have $N$ species?", font_size=45)
		self.play(Write(question))
		self.wait(3)
		self.play(Unwrite(question, reverse=True))
		self.wait(3)

		ind1_name = Tex("Simpson concentration", font_size=35)
		ind3_name = Tex("Gini-Simpson index", font_size=35)
		ind2_name = Tex("Shannon entropy", font_size=35)

		ind1 = MathTex(r"H", r"_{Si}",  r"\equiv", r"\sum_{i=1}^{N}", r"p_i", r"^2")
		ind3 = MathTex(r"H", r"_{GS}", r"\equiv", r"-", r"\sum_{i=1}^{N}", r"p_i", r"\ln (p_i)")
		ind2 = MathTex(r"H", r"_{Sh}", r"\equiv", r"1-", r"\sum_{i=1}^{N}", r"p_i", r"^2")
		ind1_name.next_to(ind1, DOWN*3)
		ind2_name.next_to(ind2, DOWN*3)
		ind3_name.next_to(ind3, DOWN*3)

		D = MathTex(r"D=", r"\frac{1}{1-H_{GS}}")
		D_name = Tex(r"Effective number of species (from Gini-Simpson index)", font_size=35)
		D_name.next_to(D, DOWN*3)

		self.play(Write(ind1), Write(ind1_name))
		self.wait(2)
		self.play(TransformMatchingTex(ind1,ind2), TransformMatchingTex(ind1_name,ind2_name))
		self.wait(2)
		self.play(TransformMatchingTex(ind2,ind3), TransformMatchingTex(ind2_name,ind3_name))

		self.wait(2)

		self.play(FadeOut(ind3), FadeOut(ind3_name))
		self.play(Write(D), Write(D_name))
		self.wait(3)

		self.play(FadeOut(title), FadeOut(D), FadeOut(D_name))
		self.wait(1)

class Arnoldi(Scene):
	def construct(self):
		title = Text("Stability Measures")
		sub = Text("for some community matrix A.", font_size=25)

		R_0 = MathTex(r"\mathcal{R}_0",  r"= -\frac{1}{2} \lambda_{\text{dom}}(A+A^T)", height=1)
		R_inf = MathTex(r"\mathcal{R}_{\infty} = -\text{Re}(\lambda_{\text{dom}}(A))")
		I_S = MathTex(r"\mathcal{I}_S = \frac{1}{2} \parallel -(A\otimes I + I \otimes A) ^{-1} \parallel _{spectral} ^{-1}")
		I_D = MathTex(r"\mathcal{I}_D = (\text{sup}_{\omega}\parallel(i \omega - A) ^{-1}\parallel_{spectral})^{-1}")
		measures = VGroup(R_0, R_inf, I_S, I_D)

		# for measure in measures:
		# 	measure.set_color_by_tex_to_color_map({
		# 		"\mathcal{R}_0": TEAL
        #     })

		sub.next_to(measures, DOWN*4)

		kw = {"run_time": 3, "path_arc": PI / 2}
        # self.wait()
        # self.play(TransformMatchingShapes(target, source, **kw))

		self.add(title.to_edge(UP))
		
		self.play(FadeIn(title, run_time=1))

		self.play(Write(R_0, run_time=1.25), Write(sub))
		self.wait(3)

		self.play(TransformMatchingShapes(R_0,R_inf, **kw))
		self.wait(3)
		self.play(TransformMatchingTex(R_inf,I_S, **kw))
		self.wait(3)
		self.play(TransformMatchingShapes(I_S,I_D, **kw))
		self.wait(3)

		self.play(FadeOut(title), FadeOut(I_D), FadeOut(sub))
		self.wait(2)


class StabDiv(Scene):
	def construct(self):
		subcol1=BLUE_B
		subcol2 = GOLD_A
		rad = 0.08/3
		alph = 0.6
		axis_font_size = 35

		import numpy as np
		import pandas as pd

		title1 = Tex("Initial resilience, $\mathcal{R}_{0}$", font_size=30)
		title2 =  Tex("$vs.$", font_size=30)
		title3 = Tex("Effective number of species, $D$", font_size=30)
		title1.next_to(title2, UP)
		title3.next_to(title2, DOWN)

		Ns = Tex("with rows representing $N=3,5,10$.", font_size=20)
		Ns.next_to(title3, DOWN*5)

		titles = VGroup(title1,title2,title3, Ns)
		self.play(Write(titles))


		coords = pd.read_csv(r"C:/Users/riley/Microbiome/animation/CSVs/gLV3.csv", index_col=0)
		
		xlims = (coords.iloc[:,-1].min() - 1/9, coords.iloc[:,-1].max() + 1/9)
		ylims = (coords.iloc[:,0].min() - 1/9, coords.iloc[:,0].max() + 1/9)
		xmargin = 0.01*(xlims[1]-xlims[0])
		ymargin = 0.03*(ylims[1]-ylims[0])
		number_plane_gLV_A = NumberPlane(
			x_range=(2.5, 3+1/9, 0.1),
			y_range=(ylims[0]-ymargin, ylims[1]+ymargin , np.round((ylims[1]-ylims[0])/5, decimals=2)),
			x_length=10,
			y_length=5,
			axis_config={"include_numbers": True, "font_size": axis_font_size},
			tips=True,
			background_line_style={
				"stroke_color":GRAY_B
			}
		).scale(0.4).to_edge(UP+LEFT)

		gLV3_group = VGroup()

		for i in range(coords.shape[0]): 
			dot = Dot(number_plane_gLV_A.coords_to_point(coords.iloc[i,-1], coords.iloc[i,0], 0), fill_opacity=alph, radius=rad, color=subcol1)
			gLV3_group.add(dot)


#################

		coords = pd.read_csv(r"C:/Users/riley/Microbiome/animation/CSVs/OD3_CL1_noP.csv", index_col=0)
		
		xlims = (coords.iloc[:,-1].min() - 1/9, coords.iloc[:,-1].max() + 1/9)
		ylims = (coords.iloc[:,0].min() - 1/9, coords.iloc[:,0].max() + 1/9)
		xmargin = 0.01*(xlims[1]-xlims[0])
		ymargin = 0.03*(ylims[1]-ylims[0])
		number_plane_OD_A = NumberPlane(
			x_range=(1.0, 3+1/9, 0.5),
			y_range=(ylims[0]-ymargin, ylims[1]+ymargin , np.round((ylims[1]-ylims[0])/5, decimals=2)),
			x_length=10,
			y_length=5,
			axis_config={"include_numbers": True, "font_size": axis_font_size},
			background_line_style={
				"stroke_color":GRAY_B
			}
		).scale(0.4).to_edge(UP+RIGHT)#.move_to(RIGHT*4)

		# number_plane_OD_A

		OD3_CL1_group = VGroup()
		for i in range(coords.shape[0]): 
			dot = Dot(number_plane_OD_A.coords_to_point(coords.iloc[i,-1], coords.iloc[i,0], 0), fill_opacity=alph, radius=rad, color=subcol2)
			OD3_CL1_group.add(dot)


		self.play(Create(number_plane_gLV_A), Create(number_plane_OD_A))
		# self.play(Write(gLV3_group))
		# self.play(Create(number_plane_OD_A))

		self.play(Write(gLV3_group), Write(OD3_CL1_group))

		# self.wait(1)
		self.wait(1)

##############
##############

		coords = pd.read_csv(r"C:/Users/riley/Microbiome/animation/CSVs/gLV5.csv", index_col=0)
		
		xlims = (coords.iloc[:,-1].min() - 1/9, coords.iloc[:,-1].max() + 1/9)
		ylims = (coords.iloc[:,0].min() - 1/9, coords.iloc[:,0].max() + 1/9)
		xmargin = 0.01*(xlims[1]-xlims[0])
		ymargin = 0.03*(ylims[1]-ylims[0])
		number_plane_gLV_B = NumberPlane(
			x_range=(4.4, 5+1/9, 0.1),
			y_range=(ylims[0]-ymargin, ylims[1]+ymargin , np.round((ylims[1]-ylims[0])/5, decimals=2)),
			x_length=10,
			y_length=5,
			axis_config={"include_numbers": True, "font_size": axis_font_size},
			tips=True,
			background_line_style={
				"stroke_color":GRAY_B
			}
		).scale(0.4).to_edge(LEFT)

		gLV5_group = VGroup()

		for i in range(coords.shape[0]): 
			dot = Dot(number_plane_gLV_B.coords_to_point(coords.iloc[i,-1], coords.iloc[i,0], 0), fill_opacity=alph, radius=rad, color=subcol1)
			gLV5_group.add(dot)

		# self.play(Create(number_plane_gLV_B))
		# self.play(Write(gLV5_group))

#################

		coords = pd.read_csv(r"C:/Users/riley/Microbiome/animation/CSVs/OD5_CL1_noP.csv", index_col=0)
		
		xlims = (coords.iloc[:,-1].min() - 1/9, coords.iloc[:,-1].max() + 1/9)
		ylims = (coords.iloc[:,0].min() - 1/9, coords.iloc[:,0].max() + 1/9)
		xmargin = 0.01*(xlims[1]-xlims[0])
		ymargin = 0.03*(ylims[1]-ylims[0])
		number_plane_OD_B = NumberPlane(
			x_range=(1.0, 5+1/9, 0.5),
			y_range=(ylims[0]-ymargin, ylims[1]+ymargin , np.round((ylims[1]-ylims[0])/5, decimals=2)),
			x_length=10,
			y_length=5,
			axis_config={"include_numbers": True, "font_size": axis_font_size},
			background_line_style={
				"stroke_color":GRAY_B
			}
		).scale(0.4).to_edge(RIGHT)#.move_to(RIGHT*4)

		# number_plane_OD_A

		OD5_CL1_group = VGroup()
		for i in range(coords.shape[0]): 
			dot = Dot(number_plane_OD_B.coords_to_point(coords.iloc[i,-1], coords.iloc[i,0], 0), fill_opacity=alph, radius=rad, color=subcol2)
			OD5_CL1_group.add(dot)

		# self.play(Create(number_plane_gLV_B))
		# self.play(Write(gLV5_group))

		self.play(Create(number_plane_gLV_B),Create(number_plane_OD_B))
		# self.play()
		self.play(Write(gLV5_group), Write(OD5_CL1_group))

		self.wait(0.1)

################
################
		coords = pd.read_csv(r"C:/Users/riley/Microbiome/animation/CSVs/gLV10.csv", index_col=0)
		
		xlims = (coords.iloc[:,-1].min() - 1/9, coords.iloc[:,-1].max() + 1/9)
		ylims = (coords.iloc[:,0].min() - 1/9, coords.iloc[:,0].max() + 1/9)
		xmargin = 0.01*(xlims[1]-xlims[0])
		ymargin = 0.03*(ylims[1]-ylims[0])
		number_plane_gLV_C = NumberPlane(
			x_range=(9.0, 10+1/9, 0.2),
			y_range=(ylims[0]-ymargin, ylims[1]+ymargin , 0.2),
			x_length=10,
			y_length=5,
			axis_config={"include_numbers": True, "font_size": axis_font_size},
			tips=True,
			background_line_style={
				"stroke_color":GRAY_B
			}
		).scale(0.4).to_edge(DOWN+LEFT)

		gLV10_group = VGroup()

		for i in range(coords.shape[0]): 
			dot = Dot(number_plane_gLV_C.coords_to_point(coords.iloc[i,-1], coords.iloc[i,0], 0), fill_opacity=alph, radius=rad, color=subcol1)
			gLV10_group.add(dot)

		# self.play(Create(number_plane_gLV_B))
		# self.play(Write(gLV10_group))

#################

		coords = pd.read_csv(r"C:/Users/riley/Microbiome/animation/CSVs/OD10_CL1_noP.csv", index_col=0)
		
		xlims = (coords.iloc[:,-1].min() - 1/9, coords.iloc[:,-1].max() + 1/9)
		ylims = (coords.iloc[:,0].min() - 1/9, coords.iloc[:,0].max() + 1/9)
		xmargin = 0.01*(xlims[1]-xlims[0])
		ymargin = 0.03*(ylims[1]-ylims[0])
		number_plane_OD_C = NumberPlane(
			x_range=(4.0, 10+1/9, 1),
			y_range=(ylims[0]-ymargin, ylims[1]+ymargin , 0.1),
			x_length=10,
			y_length=5,
			axis_config={"include_numbers": True, "font_size": axis_font_size},
			background_line_style={
				"stroke_color":GRAY_B
			}
		).scale(0.4).to_edge(DOWN+RIGHT)#.move_to(RIGHT*4)


		OD10_CL1_group = VGroup()
		for i in range(coords.shape[0]): 
			dot = Dot(number_plane_OD_C.coords_to_point(coords.iloc[i,-1], coords.iloc[i,0], 0), fill_opacity=alph, radius=rad, color=subcol2)
			OD10_CL1_group.add(dot)

		self.play(Create(number_plane_gLV_C), Create(number_plane_OD_C))
		# self.play(Create(number_plane_OD_C))
		self.play(Write(gLV10_group), Write(OD10_CL1_group))

		self.wait(2)

class FurtherResults(Scene):
	def construct(self):
		title = Tex(r"Further Results")
		title.to_edge(UP)
		self.play(FadeIn(title))

		OD5_CL1= ImageMobject("C:/Users/riley/Microbiome/animation/myplots/OD5_CL1_stab_div.png")
		OD5_CL1.scale(0.5)
		OD5_CL1.to_edge(RIGHT, buff=0.25)

		gLV5= ImageMobject("C:/Users/riley/Microbiome/animation/myplots/gLV5_stab_div.png")
		gLV5.scale(0.5)
		gLV5.to_edge(LEFT, buff=0.25)

		OD10_CL1= ImageMobject("C:/Users/riley/Microbiome/animation/myplots/OD10_CL1_stab_div.png")
		OD10_CL1.scale(0.5)
		OD10_CL1.to_edge(RIGHT, buff=0.25)

		gLV10= ImageMobject("C:/Users/riley/Microbiome/animation/myplots/gLV10_stab_div.png")
		gLV10.scale(0.5)
		gLV10.to_edge(LEFT, buff=0.25)

		self.play(FadeIn(gLV5, shift=RIGHT))
		self.wait(3)
		self.play(FadeIn(OD5_CL1, shift=LEFT))
		self.wait(3)

		self.play(FadeOut(gLV5, shift=DOWN), FadeOut(OD5_CL1, shift=DOWN), FadeIn(gLV10, shift=RIGHT), FadeIn(OD10_CL1, shift=LEFT))
		self.wait(3)

		self.play(Unwrite(title, reverse=True), FadeOut(gLV10, shift=DOWN), FadeOut(OD10_CL1, shift=DOWN))
		self.wait(3)

class eigvalDemo(Scene):
	def construct(self):
		line1 = Tex(r"$ \text{Re}(\lambda_i) < 0 $")
		line2 = Tex(r"$\text{for all } i \in \{1,\cdots,N\}$")
		group = VGroup(line1,line2)
		self.add(group)

		line2.next_to(line1, DOWN)
		# self.play(Write(line1), Write(line2))
		self.play(Write(group))
		self.wait(1)
		self.play(FadeOut(group, shift=DOWN*4))
		# self.play(FadeOut(line1), FadeOut(line2))
		
		self.wait(3)

# class test(Scene):
# 	def construct(self):
# 		glvSys = Tex(r"$\dot{S_i} = r_{i} S_{i} (1-\frac{S_{i}}{k_{i}}) + S_{i} \sum_{j=1, j\neq i}^{N} \a_{i,j} S_{j}.$")
# 		self.play(Write(glvSys))