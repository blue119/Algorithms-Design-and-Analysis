from graph_tool.all import *

g = load_graph("mincut-example.xml.gz")
weight = g.edge_properties["weight"]
mc, part = min_cut(g, weight)
print part
print(mc)

pos = g.vertex_properties["pos"]
graph_draw(g, pos=pos, edge_pen_width=weight, vertex_fill_color=part,
              output="example-min-cut.png")
