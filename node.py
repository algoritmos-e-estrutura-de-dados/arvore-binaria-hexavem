class Node:
	def __init__(self, value, direita = None, esquerda = None):
		self.value = value
		self.direita = direita
		self.esquerda = esquerda

	def __str__(self):
		return f"Node(value: {self.value}, esquerda: {self.esquerda}, direita: {self.direita})"

	def __repr__(self):
		valor = ''
		if (self.esquerda):
			valor += f"{repr(self.esquerda)} <- "
		valor += f"{self.value}"
		if (self.direita):
			valor += f" -> {repr(self.direita)}"
		
		return valor

