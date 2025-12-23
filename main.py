
import pygame
import random

pygame.init()
pygame.display.set_caption("Jogo da Cobrinha em Python")
largura, altura = 1200, 800
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# Define cores
preto = (0, 0, 0)
branco = (255, 255, 255)
azul = (0, 0, 255)
verde = (0, 255, 0)

# Definir parametros
tamanho_quadrado = 15
velocidade_jogo = 15

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branco, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render("Pontos: {pontuacao}", True, verde)
    tela.blit(texto, [1, 1])

def rodar_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2 

    velocidade_x = 0
    velocidade_y = 0


    tamanho_cobra = 1
    pixels_cobra = []

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        tela.fill(preto)    

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True

#Desenhar_Comida

        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

#Desenhar_Cobra

        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

            desenhar_cobra(tamanho_quadrado, pixels)
            desenhar_pontuacao(tamanho_cobra - 1)

        fonte = pygame.font.SysFont(None, 55)
        mensagem = fonte.render("Jogo da Cobrinha em Python", True, branco)
        tela.blit(mensagem, [largura / 6, altura / 3])


#Atualizar_Tela

    pygame.display.update()
    relogio.tick(velocidade_jogo)