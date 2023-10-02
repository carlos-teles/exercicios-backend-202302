class Apresentar:
    def __init__( self, nomeCompleto ):
        self.nomeCompleto = nomeCompleto
    def apresenta01( self ):
        """Aqui estou declarando método apresenta01"""
        return "Ola estou me apresentando"
    def apresenta( self, nome ):
        """Aqui estou declarando método apresenta"""
        return "Ola eu sou {0}".format(nome)
    def apresentaComAtrib( self ):
        """Aqui estou declarando método apresentaComAtrib"""
        return "Ola eu sou {0} com atributo".format(self.nomeCompleto)
""" Aqui inicia nosso programa """
meApresento = Apresentar("Neymar Jr")
print(meApresento.apresenta("Carlos Teles"))
print(meApresento.apresenta01())
print(meApresento.apresentaComAtrib())
meApresento.nomeCompleto = "Albert Einstein"
print(meApresento.apresentaComAtrib())
