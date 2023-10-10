import Veiculo
class Carro ( Veiculo.Veiculo ):
    def __init__(self, chassi, marca, modelo, ano, potencia, tipoCarro ):
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("Carro")
        self.potencia = potencia
        self.tipoCarro = tipoCarro
""" Aqui comeca o teste """
CarroNovo = Carro('8885AZKG01Z12A33921312', 'JAC', 'J3', '2022', 2.0, 'HATCH')
print(CarroNovo.get_tipo())
print(CarroNovo.potencia)
print(CarroNovo.tipoCarro)