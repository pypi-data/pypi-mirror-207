from lattice import Graph
from lattice import Node
from lattice import VisualEdge as Edge

graph1 = Graph()
graph1.add_nodes(**{'1': Node(1, label='1'), '2': Node(2, label='2'), '3': Node(3, label='3')})
graph1.get_node('1').add_edge(Edge(), graph1.get_node('2'))
graph1.get_node('2').add_edge(Edge(), graph1.get_node('1'))
graph1.get_node('2').add_edge(Edge(label='second'), graph1.get_node('3'))

print(graph1)
