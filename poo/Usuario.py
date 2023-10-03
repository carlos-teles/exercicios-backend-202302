class Usuario:
    def __init__(self, nome, idade, cep):
        self.nome = nome
        self.idade = idade
        self.cep = cep
    def __str__(self):
        return str(self.nome),self.idade,self.cep
""" Aqui inicia nosso programa """
usuario01 = Usuario("Cristiano Ronaldo", 36, 2000000)
print(usuario01.__str__())

usuario02 = Usuario("Lionel Messi", 35, 2220000)
print(usuario02.__str__())
