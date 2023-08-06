"""
Basic Node
"""
from __future__ import annotations
import uuid

from lattice.edge.edge import Edge


class Node:
    _successors: set
    _predecessors: set
    _label: str
    _fingerprint: uuid.UUID

    def __init__(self, pointer, label=None):
        self.pointer = pointer
        self._predecessors = set()
        self._successors = set()
        self._label = label
        self._fingerprint = uuid.uuid4()

    def copy(self, label=None):
        return Node(self.pointer, label)

    @property
    def data(self):
        return self.pointer

    @property
    def successors(self):
        return self._successors

    @property
    def predecessors(self):
        return self._predecessors

    def add_edge(self, edge: Edge, node:Node):
        self._add_successor(edge, node)
        node._add_predecessor(edge, self)

    def _add_successor(self, edge: Edge, node: Node):
        self._successors.add((edge, node))

    def _add_predecessor(self, edge: Edge, node: Node):
        self._predecessors.add((edge, node))

    def get_label(self):
        return self._label

    def __repr__(self):
        return str(self._fingerprint)
