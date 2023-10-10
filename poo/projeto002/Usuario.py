class Usuario:
    def __init__(self, nome, idade, cep):
        self.nome = nome
        self.idade = idade
        self.cep = cep
        self.msgSistema = None
    def salvarDados(self):
        if self.msgSistema == None:
            arq = open("./Usuario.txt", "a")
            arq.write( str(self.__str__())+"\n" )
            arq.close()
        self.msgSistema = "Dados salvos"
        self.nome = None
        self.idade = None
        self.cep = None
        return self.msgSistema
    def __str__(self):
        return str(self.nome),self.idade,self.cep,self.msgSistema
""" Aqui inicia nosso programa """
usuario01 = Usuario("Cristiano Ronaldo", 36, 2000000)
print(usuario01.__str__())
print(usuario01.salvarDados())
print(usuario01.__str__())
usuario01.nome="Neymar JR"
usuario01.idade = 33
usuario01.cep = 23000000
usuario01.msgSistema = None
print(usuario01.__str__())
print(usuario01.salvarDados())
print(usuario01.__str__())
#usuario02 = Usuario("Lionel Messi", 35, 2220000)
#print(usuario02.__str__())
