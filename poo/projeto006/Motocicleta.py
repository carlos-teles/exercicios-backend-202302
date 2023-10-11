import Veiculo
class Motocicleta( Veiculo.Veiculo ):
    def __init__(self, chassi, marca, modelo, ano, cilindrada, numero_rodas ):
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("Motocicleta")
        self.cilindrada = cilindrada
        self.numero_rodas = numero_rodas
        self.marcha = 1
    def ligar( self ):
        return self.marcha
    def desligar( self ):
        self.marcha = 1
""" Aqui comeca o teste """
Moto = Motocicleta('5AZKG01Z12A339037', 'Honda', 'CG', '2015', 1200, 2)
print(Moto.get_tipo())
print(Moto.numero_rodas)
print(Moto.marca)
print(Moto.ligar())