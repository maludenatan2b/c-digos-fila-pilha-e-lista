import pygame # type: ignore
import sys

# Inicializa o Pygame
pygame.init()

# Define as dimensões da janela
largura = 800
altura = 600

# Define a cor do retângulo e do fundo
cor_retangulo = (255, 0, 128)  # Verde
cor_fundo = (0, 0, 0)         # Preto

# Cria a janela do jogo
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Programa Simples em Pygame')

# Define a posição e tamanho do retângulo
retangulo_x = largura // 2
retangulo_y = altura // 2
retangulo_largura = 100
retangulo_altura = 50
velocidade = 5

# Loop principal do jogo
while True:
    # Processa os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Captura as teclas pressionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        retangulo_x -= velocidade
    if teclas[pygame.K_RIGHT]:
        retangulo_x += velocidade
    if teclas[pygame.K_UP]:
        retangulo_y -= velocidade
    if teclas[pygame.K_DOWN]:
        retangulo_y += velocidade

    # Atualiza a tela
    tela.fill(cor_fundo)
    pygame.draw.rect(tela, cor_retangulo, (retangulo_x, retangulo_y, retangulo_largura, retangulo_altura))
    pygame.display.flip()

    # Define a taxa de atualização do jogo
    pygame.time.Clock().tick(60)

    import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Define a tela
screen = pygame.display.set_mode((800, 600))

# Configura o relógio
clock = pygame.time.Clock()

# Define uma taxa constante de 60 FPS
FPS = 60

# Definindo a posição inicial do círculo
x_position = 400
y_position = 300
speed = 300  # velocidade em pixels por segundo

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Obtém o tempo passado desde o último frame em segundos
    delta_time = clock.tick(FPS) / 1000.0
    
    # Atualiza a lógica do jogo aqui usando delta_time para velocidade constante
    x_position += speed * delta_time
    
    # Reverte a direção ao atingir as bordas da tela
    if x_position > 800 or x_position < 0:
        speed = -speed
    
    # Desenha na tela aqui
    screen.fill((0, 0, 0))  # Limpa a tela com a cor preta
    pygame.draw.circle(screen, (0, 255, 0), (int(x_position), y_position), 30)  # Desenha um círculo vermelho
    
    # Atualiza o display
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()
sys.exit()