from random_walk import RandomWalk
import pygal

rw = RandomWalk()
rw.fill_walk()

rw = RandomWalk()
rw.fill_walk()

xy_graph = pygal.XY(stroke=False)
xy_graph.title = 'Random walk'
xy_graph.add('One position', [(rw.x_values[i], rw.y_values[i]) for i in range(0, rw.num_points)])
xy_graph.render_to_file('Random_Walk.svg')

