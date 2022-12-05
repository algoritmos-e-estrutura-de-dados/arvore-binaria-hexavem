from binary_tree import BinaryTree
from node import Node

bin = BinaryTree()  
bin.adicionar(Node(30))
bin.adicionar(Node(7))
bin.adicionar(Node(3))
bin.adicionar(Node(3))
bin.adicionar(Node(8))
bin.adicionar(Node(20))
bin.adicionar(Node(553))
bin.adicionar(Node(36))

print(repr(bin))

bin.remover(Node(7))
print(repr(bin))

bin.remover(Node(3))
print(repr(bin))

bin.remover(Node(553))
print(repr(bin))
