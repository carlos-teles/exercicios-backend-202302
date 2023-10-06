import JogandoDados as Dado
import Lutador

""" Aqui inicia o programa """
#Exemplo 01
jogar = Dado.JogandoDados()
jogar.set_numeroDeLados(10)
#print(jogar.get_numeroDeLados())
#print(jogar.jogarDado(), end=" ")
Mago = Lutador.Lutador("Merlin", 155, 159, 100, 20, 10, jogar)
print(" Saude: {0}".format( Mago.barraDeSaude() ))
"""print(" Lutador: {0}".format(Mago))
print(" Esta vivo: {0}".format( Mago.estaVivo() ))
Mago.ataque(Mago)
print(" Saude após ataque: {0}".format( Mago.barraDeSaude() ))"""

Guerreiro = Lutador.Lutador("Sombra", 49, 185, 60, 18, 15, jogar)
Guerreiro.ataque(Mago)
print(Guerreiro.get_mensagem())
print(Mago.get_mensagem())
print(" Saude: {0}".format( Mago.barraDeSaude() ))