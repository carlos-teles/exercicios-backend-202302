class Veiculo:
    def __init__( self, chassi, marca, modelo, ano ):
        self.__tipo = None
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def get_tipo(self):
        return self.__tipo
    def set_tipo(self,tipo):
        self.__tipo = tipo
    """ Interfaces """
    def ligar( self ):
        pass
    def desligar( self ):
        pass