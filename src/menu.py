
import pygame, sys
from src.utils import carregar_imagem 

def menu_inicial(tela, largura, altura, fonte):
    #imagem do menu
    imagem_menu = carregar_imagem("./assets/menubg.jpg", largura, altura)

    while True:
        tela.blit(imagem_menu, (0, 0))

        titulo = fonte.render("Cosmic Cat", True, (255, 245, 145))
        jogar_texto = fonte.render("Pressione ENTER para Jogar", True, (250, 38, 160))
        sair_texto = fonte.render("Pressione ESC para Sair", True, (250, 38, 160))

        tela.blit(titulo, (largura//2 - titulo.get_width()//2, 150))
        tela.blit(jogar_texto, (largura//2 - jogar_texto.get_width()//2, 300))
        tela.blit(sair_texto, (largura//2 - sair_texto.get_width()//2, 400))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return  # inicia o jogo
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
