import JogandoDados as Dado
import Lutador

""" Aqui inicia o programa """
#Exemplo 01
jogar = Dado.JogandoDados()
jogar.set_numeroDeLados(10)
#print(jogar.get_numeroDeLados())
#print(jogar.jogarDado(), end=" ")
Mago = Lutador.Lutador("Merlin", 155, 159, 100, 20, 10, jogar)
print(" Lutador: {0}".format(Mago))
print(" Saude: {0}".format( Mago.barraDeSaude() ))
print(" Esta vivo: {0}".format( Mago.estaVivo() ))
Mago.ataque(Mago)
print(" Saude após ataque: {0}".format( Mago.barraDeSaude() ))
