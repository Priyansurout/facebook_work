# Graph Implementation in Python

This repository contains a simple implementation of a graph using Python classes. It defines classes to represent nodes and graphs.

## Node Class

The `Node` class represents a node in the graph. It has attributes such as `main`, `edge`, and `next`. The constructor initializes these attributes when creating a new node.

### Constructor

```python
def __init__(self, main, edge=None, next=None):
    self.main = main
    self.next = next
    self.edge = edge

