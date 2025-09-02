import pygame, sys
from src.menu import menu_inicial
from src.game import jogar
from src.score import tela_score
from src.utils import tocar_musica

pygame.init()
LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Cosmic Cat")
fonte = pygame.font.Font(None, 50)

# música inicial
tocar_musica("./assets/Menu.wav")


# loop com try/except para mostrar erros
try:
    while True:
        menu_inicial(TELA, LARGURA, ALTURA, fonte)
        fase, tempo, venceu = jogar(TELA, LARGURA, ALTURA, fonte)
        tela_score(TELA, LARGURA, ALTURA, fonte, fase, tempo, venceu)
except Exception as e:
    import traceback
    print("ERRO NO JOGO:", e)
    traceback.print_exc()
    pygame.quit()
