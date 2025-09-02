
import pygame

def carregar_imagem(path, largura=None, altura=None):
    img = pygame.image.load(path)
    if largura and altura:
        img = pygame.transform.scale(img, (largura, altura))
    return img

def tocar_musica(path, loop=True):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1 if loop else 0)
