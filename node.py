class Node:
	def __init__(self, value, direita = None, esquerda = None):
		self.value = value
		self.direita = direita
		self.esquerda = esquerda

	def setDireita(self, node):
		self.direita = node

	def setEsquerda(self, node):
		self.esquerda = node

	def __str__(self):
		return f"Node(value: {self.value}, esquerda: {self.esquerda}, direita: {self.direita})"

	def __repr__(self):
		valor = ''
		if (self.esquerda and self.esquerda.value is not None):
			valor += f"{repr(self.esquerda)} <- "
		if (self.value is not None):
			valor += f"{self.value}"
		if (self.direita and self.direita.value is not None):
			valor += f" -> {repr(self.direita)}"
		
		return valor

