import pygame, random, sys
from src.utils import carregar_imagem, tocar_musica

def jogar(tela, largura, altura, fonte):

    player_size = 64
    gatinho = carregar_imagem("./assets/Player1.png", player_size, player_size)
    bg1 = carregar_imagem("./assets/bg.png", largura, altura)
    bg2 = carregar_imagem("./assets/bg.png", largura, altura)

    # carrega aliens de cores diferentes
    aliens_imgs = [
        carregar_imagem("./assets/Enemy1.png", 64, 64),  
        carregar_imagem("./assets/Enemy2.png", 64, 64),  
        carregar_imagem("./assets/Enemy3.png", 64, 64), 
        carregar_imagem("./assets/Enemy4.png", 64, 64), 
    ]

    player_x = largura//2
    player_y = altura - player_size - 20
    velocidade = 12

    # Inimigos
    def criar_inimigos(qtd, vel):
        inimigos = []
        for _ in range(qtd):
            x = random.randint(0, largura-64)
            y = -64
            tipo = random.randint(0, len(aliens_imgs)-1)  # cor aleatória
            inimigos.append([x, y, tipo])
        return inimigos, vel

    inimigos, inimigo_vel = criar_inimigos(5, 5)

    fase = 1
    tempo_fase = 0
    tempo_limite = 15  # segundos para passar
    rodando = True


    tocar_musica("./assets/Level1.wav")

    clock = pygame.time.Clock()

    while rodando:
        dt = clock.tick(60) / 1000  
        tempo_fase += dt


        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        # jogador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and player_x > 0: player_x -= velocidade
        if teclas[pygame.K_RIGHT] and player_x < largura-player_size: player_x += velocidade
        if teclas[pygame.K_UP] and player_y > 0: player_y -= velocidade
        if teclas[pygame.K_DOWN] and player_y < altura-player_size: player_y += velocidade

        # inimigos
        for inimigo in inimigos:
            inimigo[1] += inimigo_vel
            if inimigo[1] > altura:
                inimigo[0] = random.randint(0, largura-64)
                inimigo[1] = -64
                inimigo[2] = random.randint(0, len(aliens_imgs)-1)

            # toque
            if (player_x < inimigo[0] + 64 and player_x + 64 > inimigo[0] and
                player_y < inimigo[1] + 64 and player_y + 64 > inimigo[1]):
                return fase, int(tempo_fase), False

        # troca de fase
        if tempo_fase >= tempo_limite:
            if fase == 1:
                fase = 2
                tempo_fase = 0
                inimigos, inimigo_vel = criar_inimigos(7, 8) 
                tocar_musica("./assets/Level2.wav")  # música fase 2
            else:
                return fase, int(tempo_fase), True

        
        tela.blit(bg1 if fase == 1 else bg2, (0, 0))
        tela.blit(gatinho, (player_x, player_y))
        for inimigo in inimigos:
            tipo = inimigo[2]
            tela.blit(aliens_imgs[tipo], (inimigo[0], inimigo[1]))

        txt = fonte.render(f"Tempo: {int(tempo_fase)}s", True, (255,255,255))
        fase_txt = fonte.render(f"Fase {fase}", True, (255,255,255))
        tela.blit(txt, (10,10))
        tela.blit(fase_txt, (largura-150,10))

        pygame.display.update()
