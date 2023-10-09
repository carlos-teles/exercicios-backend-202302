import JogandoDados as Dado
import Lutador
import Arena

""" Aqui inicia o programa """
#Exemplo 01
jogar = Dado.JogandoDados()
jogar.set_numeroDeLados(10)
Mago = Lutador.Lutador("Merlin", 155, 159, 100, 20, 10, jogar)
Guerreiro = Lutador.Lutador("Sombra", 49, 185, 60, 18, 15, jogar)
#Luta
Luta01 = Arena.Arena(Mago, Guerreiro, jogar)
Luta01.lutar()