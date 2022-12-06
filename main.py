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

print(bin.emOrdem())
print()

print("INICIO :: Pre Ordem:")
print(bin.preOrdem(bin.root))
print("FIM :: Pre Ordem:")

print()

print("INICIO :: Pos Ordem:")
print(bin.posOrdem(bin.root))
print("FIM :: Pos Ordem:")