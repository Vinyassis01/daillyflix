class Pessoa :
	def __init__ (self,nome,idade):
		self.nome = nome
		self.idade = idade
		self.exp = []
 
	def experiencia(self,cargo):
		return self.exp.append(cargo)

p1 = Pessoa('vinycius',22)
p1.experiencia('dev')
print(p1.nome)
print(p1.exp)
