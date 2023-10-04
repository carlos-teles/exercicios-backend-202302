class Lutador:
    """
    Esta classe representa a arena do Lutador
    """
    def __init__(self, nome, idade, altura, saude, dano, defesa, valorDoDado ):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
        self.__saude = saude
        self.__max_saude = saude
        self.__dano = dano
        self.__defesa = defesa
        self.__valorDoDado = valorDoDado
        self.__mensagem = ""
    def __str__ (self):
        return str(self.nome),self.saude
    def estaVivo( self ):
        return self.__saude > 0
    def barraDeSaude ( self ):
        total = 20
        contador = int(self.__saude / self.__max_saude * total )
        if ( contador == 0 and self.estaVivo() ):
            contador = 1
        return "[{0}{1}".format("#" * contador, " "*(total - contador))
