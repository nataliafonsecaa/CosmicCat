import pygame, sys
from src.utils import carregar_imagem

def tela_score(tela, largura, altura, fonte, fase, tempo, venceu):
    # Carrega imagem de fundo do score
    bg_score = carregar_imagem("./assets/ScoreBg.jpg", largura, altura)

    rodando = True
    while rodando:
        # Desenha o fundo
        tela.blit(bg_score, (0, 0))

        # mensagem de vitória ou derrota
        if venceu:
            msg = f"Você venceu! Fase {fase} em {tempo}s"
        else:
            msg = f"Game Over! Sobreviveu {tempo}s na fase {fase}"

        texto = fonte.render(msg, True, (250, 38, 160))
        tela.blit(texto, (largura//2 - texto.get_width()//2, altura//2))

        info = fonte.render("Pressione ENTER para voltar ao menu", True, (250, 38, 160))
        tela.blit(info, (largura//2 - info.get_width()//2, altura//2 + 80))

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                rodando = False  # volta para o menu