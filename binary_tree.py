class BinaryTree:

	def __init__(self):
		self.root = None

	def ordenar(self):
		target = self.root
		while True:
			if target is None:
				break

			if target.value is None:
				if (target.esquerda is not None and target.esquerda.value is not None):
					self.adicionar(target.esquerda)
					target.esquerda.value = None
					target = target.esquerda
					continue
				if (target.direita is not None and target.direita.value is not None):
					self.adicionar(target.direita)
					target.direita.value = None
					target = target.direita
					continue
				break

			if (target.esquerda is not None and target.esquerda.value is None):
				target = target.esquerda
				continue

			if (target.direita is not None and target.direita.value is None):
				target = target.direita
				continue
			break

	def adicionar(self, node):
		if (self.root == None):
			self.root = node
			return

		target = self.root
		while True:
			if (target.value is not None and target.value == node.value):
				break

			if target.value is None:
				target.value = node.value
				break

			if (node.value > target.value):
				if (target.direita is None):
					target.setDireita(node)
					break

				target = target.direita

			else:
				if (target.esquerda is None):
					target.setEsquerda(node)
					break

				target = target.esquerda

	def remover(self, node):
		target = self.root.esquerda
		switch = False

		while True:
			if target.direita is None and target.esquerda is None:
				if (not switch):
					switch = not switch
					target = self.root.direita
					continue
				break

			if (node.value == target.value):
				target.value = None
				break

			if (target.direita is not None):
				target = target.direita
				continue

			if (target.esquerda is not None):
				target = target.esquerda
				continue

		self.ordenar()

	def preOrdem(self, node):
		if node is not None:
			print(node.value)
			self.preOrdem(node.esquerda)
			self.preOrdem(node.direita)

	def posOrdem(self, node):
		if node is not None:
			self.posOrdem(node.esquerda)
			self.posOrdem(node.direita)
			print(node.value)

	def __str__(self):
		return f"{self.root}"

	def emOrdem(self):
		valor = ''
		if (self.root.esquerda):
			valor += f"{repr(self.root.esquerda)} <- "
		valor += f"| {self.root.value} |"
		if (self.root.direita):
			valor += f" -> {repr(self.root.direita)}"
		return valor

	def __repr__(self):
		valor = ''
		if (self.root.esquerda):
			valor += f"{repr(self.root.esquerda)} <- "
		valor += f"| {self.root.value} |"
		if (self.root.direita):
			valor += f" -> {repr(self.root.direita)}"
		return valor
