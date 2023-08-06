from lattice import Graph
from lattice import Node
from lattice import VisualEdge as Edge

graph = Graph()
graph.add_nodes(**{'1': Node(1), '2': Node(2), '3': Node(3)})
graph.get_node('1').add_edge(Edge(), graph.get_node('2'))
graph.get_node('2').add_edge(Edge(), graph.get_node('1'))
graph.get_node('2').add_edge(Edge('second'), graph.get_node('3'))


print(graph)
