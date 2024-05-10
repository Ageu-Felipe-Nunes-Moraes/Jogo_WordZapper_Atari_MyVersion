
import os # Módulo para Sistema Operacional

import pygame # Módulo para jogo
    
import random # Módulo para aleatoriedade

# Inicia o pygame
pygame.init()

# Caminho atual dos arquivos
caminho_atual = os.path.abspath(os.path.dirname(__file__))

# VARIÁVEIS PARA A TELA INICIAL
tela_inicial = pygame.display.set_mode((1260, 700))
caminho_relativo_imagem_inicial = os.path.join(caminho_atual, "Recursos_Jogo/imagemFundoZapperDesfocada.png")
imagem_inicial = pygame.image.load(caminho_relativo_imagem_inicial)
imagem_inicial_jogo = pygame.transform.scale(imagem_inicial, (1260, 700))
janela_inicial_aberta = True

# VARIÁVEIS PARA O JOGO
# Todos os caminhos relativos dos arquivos do jogo
caminho_relativo_som_fundo = os.path.join(caminho_atual, 'Recursos_Jogo/SomFudoParaJogo.mp3')
caminho_relativo_efeito_tiro = os.path.join(caminho_atual, 'Recursos_Jogo/efeitoSonoroTiroLazer.mp3')
caminho_relativo_colisao = os.path.join(caminho_atual, 'Recursos_Jogo/colisãoSom.mp3')
caminho_relativo_imagem_fundo = os.path.join(caminho_atual, "Recursos_Jogo/imagemFundoZapper.png")
caminho_relativo_jogador = os.path.join(caminho_atual, "Recursos_Jogo/jogadorZapper.png")
caminho_relativo_inimigo = os.path.join(caminho_atual, "Recursos_Jogo/inimigoAsteristico.png")

pygame.mixer.music.load(caminho_relativo_som_fundo)
pygame.mixer.music.play(loops=-1)

efeito_sonoro_tiro = pygame.mixer.Sound(caminho_relativo_efeito_tiro)
efeito_sonoro_colisao_inimiga = pygame.mixer.Sound(caminho_relativo_colisao)

# Dimensões de tela de jogo
largura_tela = 1260
altura_tela = 700

# AJusta o modo do tamanho da janela
janela = pygame.display.set_mode((largura_tela, altura_tela))

# Traz a imagem de fundo do jogo para dentro do python
imagem_fundo = pygame.image.load(caminho_relativo_imagem_fundo)
# Coloca a imagem como tela de fundo do jogo
imagem_fundo_jogo = pygame.transform.scale(imagem_fundo, (largura_tela, altura_tela))

# Traz a imagem da nave do jogador para dentro do jogo
imagem_jogador = pygame.image.load(caminho_relativo_jogador)

# Chamando a imagem inimiga em formato de asterisco, para a tela
inimigo_asteristico = pygame.image.load(caminho_relativo_inimigo)

# Variáveis que definem a posição da nave
jogador_posicao_x = 380
jogador_posicao_y = 460
# Variável para a velocidade
jogador_velocidade = 25

# Nascimento inimigo à direita
posicao_inimiga_direita_x1 = 2500
posicao_inimiga_direita_x2 = 2500
posicao_inimiga_direita_x3 = 2500
posicao_inimiga_direita_x4 = 2500
posicao_inimiga_direita_x5 = 2500
posicao_inimiga_direita_x6 = 2500

# Nascimento inimigo à esquerda
posicao_inimiga_esquerda_x1 = -100
posicao_inimiga_esquerda_x2 = -100
posicao_inimiga_esquerda_x3 = -100
posicao_inimiga_esquerda_x4 = -100
posicao_inimiga_esquerda_x5 = -100
posicao_inimiga_esquerda_x6 = -100

inimigo_posicao_y = 450

# Velocidades disponíveis ao inimigo
velocidades_inimiga = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Escolha da velocidade de maneira aleatória
velocidades_inimiga_escolha1 = random.choice(velocidades_inimiga)
velocidades_inimiga_escolha2 = random.choice(velocidades_inimiga)
velocidades_inimiga_escolha3 = random.choice(velocidades_inimiga)
velocidades_inimiga_escolha4 = random.choice(velocidades_inimiga)
velocidades_inimiga_escolha5 = random.choice(velocidades_inimiga)
velocidades_inimiga_escolha6 = random.choice(velocidades_inimiga)
velocidades_inimiga_escolha7 = random.choice(velocidades_inimiga)
velocidades_inimiga_escolha8 = random.choice(velocidades_inimiga)
velocidades_inimiga_escolha9 = random.choice(velocidades_inimiga)
velocidades_inimiga_escolha10 = random.choice(velocidades_inimiga)
velocidades_inimiga_escolha11 = random.choice(velocidades_inimiga)
velocidades_inimiga_escolha12 = random.choice(velocidades_inimiga)

# Coloca o título do jogo
pygame.display.set_caption("Word Zapper")

# Variável de controle boleana verdadeira
janela_aberta = True

# Comprimento do lazer do jogador
lazer_jogador_x = 28
lazer_jogador_y = 465

# Posições x das letras
posicao_letras_A_x, posicao_letras_B_x, posicao_letras_C_x, posicao_letras_D_x = 1260, 1350, 1435, 1520
posicao_letras_E_x, posicao_letras_F_x, posicao_letras_G_x, posicao_letras_H_x = 1605, 1690, 1770, 1860
posicao_letras_I_x, posicao_letras_J_x, posicao_letras_K_x, posicao_letras_L_x = 1944, 2005, 2085, 2175
posicao_letras_M_x, posicao_letras_N_x, posicao_letras_O_x, posicao_letras_P_x = 2255, 2357, 2447, 2535
posicao_letras_Q_x, posicao_letras_R_x, posicao_letras_S_x, posicao_letras_T_x = 2619, 2705, 2790, 2875
posicao_letras_U_x, posicao_letras_V_x, posicao_letras_W_x, posicaoLetrasX_x = 2960, 3040, 3120, 3212
posicao_letras_Y_x, posicaoLetrasZ_x, posicao_caractere_x = 3293, 3377, 3462

# Posição y das letras
posicao_letras_A_y, posicao_letras_B_y, posicao_letras_C_y, posicao_letras_D_y = 114, 114, 114, 114
posicao_letras_E_y, posicao_letras_F_y, posicao_letras_G_y, posicao_letras_H_y = 114, 114, 114, 114
posicao_letras_I_y, posicao_letras_J_y, posicao_letras_K_y, posicao_letras_L_y = 114, 114, 114, 114
posicao_letras_M_y, posicao_letras_N_y, posicao_letras_O_y, posicao_letras_P_y = 114, 114, 114, 114
posicao_letras_Q_y, posicao_letras_R_y, posicao_letras_S_y, posicao_letras_T_y = 114, 114, 114, 114
posicao_letras_U_y, posicao_letras_V_y, posicao_letras_W_y, posicao_letras_X_y = 114, 114, 114, 114
posicao_letras_Y_y, posicaoLetrasZ_y, posicao_caractere_y = 114, 114, 114

# Velocidades em que as letras se movimentão
velocidade_letras = 10

# Coordenada onde as letras chegam antes de voltar para a coordenada inicial
coordenada_final = -1000
# VariáveL que irá resetar
resetar_x = 1260

# Determina a posição das interrogações
pos_interrogacao_x = 432
pos_interrogacao_y = 570
distancia_interrogacoes = 70

# Tamanho padrão dos retângulos para os inimigos
rect_inimigo_alt = 30
rect_inimigo_larg = 32

# Posição e tamanho médio dos retângulos para cada letra
reduz_pos_x = 10
rect_larg_letra = 49
rect_alt_letra = 68.5

# Tempo total antes de começar e após começar o jogo
tempo_total = 104
# Será usado como unidade de medida de conversão para minutos
contador_tempo = 0

# Esse "subTempo" é apenas um contador simbólico que irá ser usado dentro de uma condicional
sub_tempo = 0

# Contador de soma, variável de controle booleana e duração do tempo. Serão usados para a exibição de uma mensagem
tempo_perda = 0
exibir_perda = False
duracao_perda = 1000

exibir_ganho = False
contador_tempo_ganho = 0

reiniciar = False

# Quantidade de tempo antes que a palavra que eu tenho que encontrar suma da tela e que o jogo seja resetado
tempo_pausa = 3

# Lista vazia onde será armazenada o tempo do jogo quando uma certa condicional for executada
lista_tempo_para_pausa = []

# Lista vazia onde será armazenada o tempo do jogo quando uma certa condicional for executada
lista_tempo_para_erro = []

arquivo_txt_relativo = os.path.join(caminho_atual, 'Recursos_Jogo/WordZapper.txt')

# 'Puxa' o arquivo txt com as palavras para o jogo
with open(arquivo_txt_relativo) as arquivo:
    todas_palavras = arquivo.readlines()

# Retira a quebra de linha das palavras
lista_palavras = [linha.rstrip() for linha in todas_palavras]

# Determinando o significado de cada variável
interrogacao_letra1, interrogacao_letra2, interrogacao_letra3, interrogacao_letra4 = '?', '?', '?', '?'
interrogacao_letra5, interrogacao_letra6 = '?', '?'

# Dicionário com todas as posições Y das letras
posicao_letras_y = {
    'A': posicao_letras_A_y,
    'B': posicao_letras_B_y,
    'C': posicao_letras_C_y,
    'D': posicao_letras_D_y,
    'E': posicao_letras_E_y,
    'F': posicao_letras_F_y,
    'G': posicao_letras_G_y,
    'H': posicao_letras_H_y,
    'I': posicao_letras_I_y,
    'J': posicao_letras_J_y,
    'K': posicao_letras_K_y,
    'L': posicao_letras_L_y,
    'M': posicao_letras_M_y,
    'N': posicao_letras_N_y,
    'O': posicao_letras_O_y,
    'P': posicao_letras_P_y,
    'Q': posicao_letras_Q_y,
    'R': posicao_letras_R_y,
    'S': posicao_letras_S_y,
    'T': posicao_letras_T_y,
    'U': posicao_letras_U_y,
    'V': posicao_letras_V_y,
    'W': posicao_letras_W_y,
    'X': posicao_letras_X_y,
    'Y': posicao_letras_Y_y,
    'Z': posicaoLetrasZ_y,
    '*': posicao_caractere_y
}

# Pontuação do jogador
pontuacao_jogador = 0


# Some com as letras da tela, até completar o ciclo
def sumir_letras(letra_dicionario, nova_posicao):

    global posicao_letras_y
    posicao_letras_y[letra_dicionario] = nova_posicao


# Verifica as letras atingidas pelo lazer do jogador e coloca na tela se forem corretas
def verificacao_letra(rect_letra, letra):
    # Traz uma variável de fora, para dentro da função através de uma "global"
    global interrogacao_letra1, interrogacao_letra2, interrogacao_letra3, interrogacao_letra4, interrogacao_letra5, \
        interrogacao_letra6, palavra_sorteada, lista_palavra_sorteada, pontuacao_jogador, formatacao_perda, exibir_perda, \
        tempo_perda, perda, tempo_total

    # Transforma a palavra sorteada em uma lista
    lista_palavra_sorteada = list(palavra_sorteada)

    # Condicionais que determinam a mudança das interrogações na tela para as letras da palavra sorteada
    if len(palavra_sorteada) >= 1:

        # identifica colisão com o retângulo
        if rect_letra.colide_retangulo(disparo_lazer_jogador) and letra == palavra_sorteada[0]:

            interrogacao_letra1 = letra
            sumir_letras(letra, -1500)
            if tempo_total < 95:
                tempo_total += 5
            elif tempo_total >= 95:
                tempo_total = 99

    if len(palavra_sorteada) >= 2:

        if rect_letra.colide_retangulo(disparo_lazer_jogador) and letra == palavra_sorteada[1] and\
                interrogacao_letra1 != "?":

            interrogacao_letra2 = letra
            sumir_letras(letra, -1500)
            if tempo_total < 95:
                tempo_total += 5
            elif tempo_total >= 95:
                tempo_total = 99

    if len(palavra_sorteada) >= 3:

        if rect_letra.colide_retangulo(disparo_lazer_jogador) and letra == palavra_sorteada[2] and\
                interrogacao_letra2 != "?":

            interrogacao_letra3 = letra
            sumir_letras(letra, -1500)
            if tempo_total < 95:
                tempo_total += 5
            elif tempo_total >= 95:
                tempo_total = 99

    if len(palavra_sorteada) >= 4:

        if rect_letra.colide_retangulo(disparo_lazer_jogador) and letra == palavra_sorteada[3] and\
                interrogacao_letra3 != "?":

            interrogacao_letra4 = letra
            sumir_letras(letra, -1500)
            if tempo_total < 95:
                tempo_total += 5
            elif tempo_total >= 95:
                tempo_total = 99

    if len(palavra_sorteada) >= 5:

        if rect_letra.colide_retangulo(disparo_lazer_jogador) and letra == palavra_sorteada[4] and\
                interrogacao_letra4 != "?":

            interrogacao_letra5 = letra
            sumir_letras(letra, -1500)

            if tempo_total < 95:
                tempo_total += 5
            elif tempo_total >= 95:
                tempo_total = 99

    if len(palavra_sorteada) == 6:

        if rect_letra.colide_retangulo(disparo_lazer_jogador) and letra == palavra_sorteada[5] and\
                interrogacao_letra5 != "?":

            interrogacao_letra6 = letra
            sumir_letras(letra, -1500)

            if tempo_total < 95:
                tempo_total += 5
            elif tempo_total >= 95:
                tempo_total = 99

    if rect_letra.colide_retangulo(disparo_lazer_jogador):
        sumir_letras(letra, -1500)
        if letra not in palavra_sorteada:
            # Mostra a mensagem de perda de pontuação na tela
            perda = 15
            string_perda = str(f" - {15} PONTOS")
            pontuacao_jogador -= perda
            fonte_perda_pontos = pygame.font.Font(None, 70)
            formatacao_perda = fonte_perda_pontos.render(string_perda, True, (255, 0, 0), (48, 15, 158, 255))
            exibir_perda = True
            if pontuacao_jogador < 0:
                pontuacao_jogador = 0
            # Obtém o tempo atual em milissegundos
            tempo_perda = pygame.time.get_ticks()


# Classe para criar inimigos
class Inimigo:
    def __init__(self, x, y):
        janela.blit(inimigo_asteristico, (x, y))


# Classe para criar retângulos
class Retangulo:
    def __init__(self, x, y, largura, altura):
        pygame.draw.rect(janela, (0, 0, 0), (x, y, largura, altura))


# Classe para criar retângulos que serão sobrepostos por personagens do jogo para capitar as colisões
class Retangulo_Colisao:
    def __init__(self, r, g, b, a, x, y, largura, altura):
        pygame.draw.rect(janela, (r, g, b, a), (x, y, largura, altura))
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

    # Função para verificar colisão entre retângulos
    def colide_retangulo(self, outro_retangulo):
        # Verifica a colisão entre as duas coordenadas horizontais e entre as duas coordenadas verticais
        if self.x < outro_retangulo.x + outro_retangulo.largura and \
                self.x + self.largura > outro_retangulo.x and \
                self.y < outro_retangulo.y + outro_retangulo.altura and \
                self.y + self.altura > outro_retangulo.y:
            efeito_sonoro_colisao_inimiga.play()
            return True
        return False


# Classe para criar letras
class Letras:
    def __init__(self, letra):
        fonte = pygame.font.Font(None, 100)
        self.formatacao = fonte.render(letra, True, (235, 235, 234, 255), (48, 15, 158, 255,))

    # Função para posicionar letras criadas pela classe
    def posicao_letra(self, x, y):
        janela.blit(self.formatacao, (x, y))


# Classe para criar interrogações com a mesma formatação e editar a posição delas
class Interrogacao:
    def __init__(self, letra):
        fonte = pygame.font.Font(None, 100)
        self.formatacao = fonte.render(letra, True, (182, 201, 96, 255), (0, 0, 0, 25))
        self.letra = letra

    def posicao_interrogacao(self, x, y):
        janela.blit(self.formatacao, (x, y))


# Classe para criar letras
class Regras:
    def __init__(self, letra):
        fonte = pygame.font.Font(None, 30)
        self.formatacao = fonte.render(letra, True, (235, 235, 234, 255), (48, 15, 158, 255,))

    # Função para posicionar letras criadas pela classe
    def posicao_regras(self, x, y):
        janela.blit(self.formatacao, (x, y))


# Estrutura de repetição controlada pela variável boleana
while janela_inicial_aberta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            janela_inicial_aberta = False
            janela_aberta = False

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_RETURN] or comandos[pygame.K_KP_ENTER]:
            janela_inicial_aberta = False

    tela_inicial.blit(imagem_inicial_jogo, (0, 0))
    # Cria a letra
    fonte_tempo = pygame.font.Font(None, 100)
    formatacao_nome_jogo = fonte_tempo.render('Como Jogar:', True, (118, 225, 115, 255), (48, 15, 158, 255))
    janela.blit(formatacao_nome_jogo, (420, 30))

    regra1 = Regras(" - Você precisa montar todas as palavras que aparecerem na tela")
    regra2 = Regras(" - As palavras devem ser montadas na ordem correta")
    regra3 = Regras(" - Elas surgem apenas por um curto período de tempo")
    regra4 = Regras(" - Desvie de todos os inimigos que emergem das laterais da tela")
    regra5 = Regras(" - Se houver um choque inimigo, você perderá alguns segundos")
    regra6 = Regras(" - Para toda letra acertada você ganha +5 segundos de tempo")
    regra7 = Regras(" - As teclas 'espaço'(atira) e 'setas'(Movimentam o jogador)")
    regra8 = Regras(" - Quando você montar a palavra envie ela atirando no '*'")
    regra9 = Regras(" - Monte o maior número de palavras, antes que o jogo acabe")
    regra10 = Regras(" - O jogo só acaba quando o temporizador chegar a zero")

    Regras.posicao_regras(regra1, 300, 200)
    Regras.posicao_regras(regra2, 300, 230)
    Regras.posicao_regras(regra3, 300, 260)
    Regras.posicao_regras(regra4, 300, 290)
    Regras.posicao_regras(regra5, 300, 320)
    Regras.posicao_regras(regra6, 300, 350)
    Regras.posicao_regras(regra7, 300, 380)
    Regras.posicao_regras(regra8, 300, 410)
    Regras.posicao_regras(regra9, 300, 440)
    Regras.posicao_regras(regra10, 300, 470)

    fonte_interrogacao = pygame.font.Font(None, 70)
    mensagem_instrucao = "Pressione a tecla 'Enter' para iniciar o jogo!"
    formatacao_instrucao = fonte_interrogacao.render(mensagem_instrucao, True, (182, 201, 96, 255), (0, 0, 0, 25))
    tela_inicial.blit(formatacao_instrucao, (115, 600))

    pygame.display.update()


# Estrutura de repetição controlada pela variável boleana
while janela_aberta:
    # Executa delay de 30 mílisegundo
    delay = pygame.time.delay(30)

    # Para cada evento que ocorre no pygame ele cria uma iteração de verificação
    for evento in pygame.event.get():
        # Condicional que verifica se o tipo do evento é igual a sair do jogo
        if evento.type == pygame.QUIT:
            # Variável de controle boleana falsa que resulta no fim da iteração
            janela_aberta = False

    # Lê as teclas pressionadas pelo usuario
    comandos = pygame.key.get_pressed()

    if tempo_total <= 102:
        # Condicionais que determinam o movimento da nave através do teclado
        if comandos[pygame.K_UP] and jogador_posicao_y > 200:
            jogador_posicao_y -= jogador_velocidade
        if comandos[pygame.K_DOWN] and jogador_posicao_y < 460:
            jogador_posicao_y += jogador_velocidade
        if comandos[pygame.K_LEFT] and jogador_posicao_x > 220:
            jogador_posicao_x -= jogador_velocidade
        if comandos[pygame.K_RIGHT] and jogador_posicao_x < 940:
            jogador_posicao_x += jogador_velocidade

    # Se tempo for igual a 104 ele vai escolher uma palavra
    if tempo_total == 104:
        # Escolhe uma palavra aleatóriamente
        palavra_escolhida = random.choice(lista_palavras)
        palavra_sorteada = palavra_escolhida.upper()
        pontuacao_jogador = 0
        perda = 0

    # Traz a imagem de fundo para a tela e posiciona ela nas coordenadas do canto superior esquerdo da tela
    janela.blit(imagem_fundo_jogo, (0, 0))

    # Condicional que verifica constantemente o tipo booleano da variável para ser executada
    if exibir_perda:  # Quando não tem nenhuma igualdade, a variável só é verificada se ela for verdadeira
        # Obtém o tempo atual em milissegundos
        tempo_atual = pygame.time.get_ticks()
        # Se a conta do tempo registrado anteriormente com o tempo atual for maior que o tempo de duração, executará
        if tempo_atual - tempo_perda >= duracao_perda:
            exibir_perda = False  # Desativa a exibição da mensagem

        # Desenha a mensagem na tela
        janela.blit(formatacao_perda, (450, 300))

    # Criando retângulo de colisão do jogador
    rect_jogador = Retangulo_Colisao(48, 15, 158, 255, jogador_posicao_x, jogador_posicao_y, 96, 38)

    # Criando retângulo de colisão inimgo
    rect_inimigo_direita1 = Retangulo_Colisao(
        48, 15, 158, 255, posicao_inimiga_direita_x1, inimigo_posicao_y, rect_inimigo_alt, rect_inimigo_larg)
    rect_inimigo_direita2 = Retangulo_Colisao(
        48, 15, 158, 255, posicao_inimiga_direita_x2, inimigo_posicao_y - 50, rect_inimigo_alt, rect_inimigo_larg)
    rect_inimigo_direita3 = Retangulo_Colisao(
        48, 15, 158, 255, posicao_inimiga_direita_x3, inimigo_posicao_y - 100, rect_inimigo_alt, rect_inimigo_larg)
    rect_inimigo_direita4 = Retangulo_Colisao(
        48, 15, 158, 255, posicao_inimiga_direita_x4, inimigo_posicao_y - 150, rect_inimigo_alt, rect_inimigo_larg)
    rect_inimigo_direita5 = Retangulo_Colisao(
        48, 15, 158, 255, posicao_inimiga_direita_x5, inimigo_posicao_y - 200, rect_inimigo_alt, rect_inimigo_larg)
    rect_inimigo_direita6 = Retangulo_Colisao(
        48, 15, 158, 255, posicao_inimiga_direita_x6, inimigo_posicao_y - 250, rect_inimigo_alt, rect_inimigo_larg)

    rect_inimigo_esquerda1 = Retangulo_Colisao(
        48, 15, 158, 255, posicao_inimiga_esquerda_x1, inimigo_posicao_y, rect_inimigo_alt, rect_inimigo_larg)
    rect_inimigo_esquerda2 = Retangulo_Colisao(
        48, 15, 158, 255, posicao_inimiga_esquerda_x2, inimigo_posicao_y - 50, rect_inimigo_alt, rect_inimigo_larg)
    rect_inimigo_esquerda3 = Retangulo_Colisao(
        48, 15, 158, 255, posicao_inimiga_esquerda_x3, inimigo_posicao_y - 100, rect_inimigo_alt, rect_inimigo_larg)
    rect_inimigo_esquerda4 = Retangulo_Colisao(
        48, 15, 158, 255, posicao_inimiga_esquerda_x4, inimigo_posicao_y - 150, rect_inimigo_alt, rect_inimigo_larg)
    rect_inimigo_esquerda5 = Retangulo_Colisao(
        48, 15, 158, 255, posicao_inimiga_esquerda_x5, inimigo_posicao_y - 200, rect_inimigo_alt, rect_inimigo_larg)
    rect_inimigo_esquerda6 = Retangulo_Colisao(
        48, 15, 158, 255, posicao_inimiga_esquerda_x6, inimigo_posicao_y - 250, rect_inimigo_alt, rect_inimigo_larg)

    # Criando retângulo de colisão das letras
    rect_letra_A = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_A_x - reduz_pos_x, posicao_letras_y['A'], rect_larg_letra, rect_alt_letra)
    rect_letra_B = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_B_x - reduz_pos_x, posicao_letras_y['B'], rect_larg_letra, rect_alt_letra)
    rect_letra_C = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_C_x - reduz_pos_x, posicao_letras_y['C'], rect_larg_letra, rect_alt_letra)
    rect_letra_D = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_D_x - reduz_pos_x, posicao_letras_y['D'], rect_larg_letra, rect_alt_letra)
    rect_letra_E = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_E_x - reduz_pos_x, posicao_letras_y['E'], rect_larg_letra - 4, rect_alt_letra)
    rect_letra_F = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_F_x - reduz_pos_x, posicao_letras_y['F'], rect_larg_letra - 7, rect_alt_letra)
    rect_letra_G = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_G_x - reduz_pos_x, posicao_letras_y['G'], rect_larg_letra + 4, rect_alt_letra)
    rect_letra_H = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_H_x - reduz_pos_x, posicao_letras_y['H'], rect_larg_letra, rect_alt_letra)
    rect_letra_I = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_I_x - reduz_pos_x, posicao_letras_y['I'], rect_larg_letra - 30, rect_alt_letra)
    rect_letra_J = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_J_x - reduz_pos_x, posicao_letras_y['J'], rect_larg_letra - 11, rect_alt_letra)
    rect_letra_K = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_K_x - reduz_pos_x, posicao_letras_y['K'], rect_larg_letra, rect_alt_letra)
    rect_letra_L = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_L_x - reduz_pos_x, posicao_letras_y['L'], rect_larg_letra - 7, rect_alt_letra)
    rect_letra_M = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_M_x - reduz_pos_x, posicao_letras_y['M'], rect_larg_letra + 8, rect_alt_letra)
    rect_letra_N = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_N_x - reduz_pos_x, posicao_letras_y['N'], rect_larg_letra, rect_alt_letra)
    rect_letra_O = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_O_x - reduz_pos_x, posicao_letras_y['O'], rect_larg_letra + 4, rect_alt_letra)
    rect_letra_P = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_P_x - reduz_pos_x, posicao_letras_y['P'], rect_larg_letra - 4, rect_alt_letra)
    rect_letra_Q = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_Q_x - reduz_pos_x, posicao_letras_y['Q'], rect_larg_letra + 4, rect_alt_letra)
    rect_letra_R = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_R_x - reduz_pos_x, posicao_letras_y['R'], rect_larg_letra, rect_alt_letra)
    rect_letra_S = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_S_x - reduz_pos_x, posicao_letras_y['S'], rect_larg_letra - 4, rect_alt_letra)
    rect_letra_T = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_T_x - reduz_pos_x, posicao_letras_y['T'], rect_larg_letra - 7, rect_alt_letra)
    rect_letra_U = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_U_x - reduz_pos_x, posicao_letras_y['U'], rect_larg_letra, rect_alt_letra)
    rect_letra_V = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_V_x - reduz_pos_x, posicao_letras_y['V'], rect_larg_letra - 4, rect_alt_letra)
    rect_letra_W = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_W_x - reduz_pos_x, posicao_letras_y['W'], rect_larg_letra + 15, rect_alt_letra)
    rect_letra_X = Retangulo_Colisao(
        48, 15, 158, 255, posicaoLetrasX_x - reduz_pos_x, posicao_letras_y['X'], rect_larg_letra - 4, rect_alt_letra)
    rect_letra_Y = Retangulo_Colisao(
        48, 15, 158, 255, posicao_letras_Y_x - reduz_pos_x, posicao_letras_y['Y'], rect_larg_letra - 4, rect_alt_letra)
    rect_letra_Z = Retangulo_Colisao(
        48, 15, 158, 255, posicaoLetrasZ_x - reduz_pos_x, posicao_letras_y['Z'], rect_larg_letra - 7, rect_alt_letra)
    rect_caractere = Retangulo_Colisao(
        48, 15, 158, 255, posicao_caractere_x - reduz_pos_x, posicao_letras_y['*'] + 2, rect_larg_letra - 23, rect_alt_letra)

    # Se o tempo for menor que 100 segundo ele executará o comando abaixo
    if tempo_total < 100:
        # Se o jogador colidir com qualquer retângulo ele perderá 2 segundo do seu tempo; isso crescerá exponencialmente
        if rect_jogador.colide_retangulo(rect_inimigo_direita1) or rect_jogador.colide_retangulo(rect_inimigo_direita2) or \
                rect_jogador.colide_retangulo(rect_inimigo_direita3) or rect_jogador.colide_retangulo(
              rect_inimigo_direita4) or \
                rect_jogador.colide_retangulo(rect_inimigo_direita5) or rect_jogador.colide_retangulo(
              rect_inimigo_direita6) or \
                rect_jogador.colide_retangulo(rect_inimigo_esquerda1) or rect_jogador.colide_retangulo(
              rect_inimigo_esquerda2) or \
                rect_jogador.colide_retangulo(rect_inimigo_esquerda3) or rect_jogador.colide_retangulo(
              rect_inimigo_esquerda4) or \
                rect_jogador.colide_retangulo(rect_inimigo_esquerda5) or rect_jogador.colide_retangulo(
              rect_inimigo_esquerda6):
            tempo_total -= 2

    # Unidade de medida para contar o tempo em segundos
    contador_tempo += 52.635
    # Condicional que simular um temporizador, subtraindo 1 segundo a cada 1000 de 'contadorTempo'
    if contador_tempo >= 1000:
        contador_tempo = 0
        tempo_total -= 1

    # Transforma o 'tempoTotal' de inteiro para string
    tempo_total_string = str(tempo_total)

    # Cria a letra
    fonte_tempo = pygame.font.Font(None, 100)
    # Formata e escreve a mensagem
    formatacao_tempo = fonte_tempo.render(tempo_total_string, True, (118, 225, 115, 255), (48, 15, 158, 255,))
    # Condicional que irá mostrar o tempo na tela apenas quando ele começar a contar valendo no jogo
    if tempo_total <= 99:
        janela.blit(formatacao_tempo, (590, 30))

    # Condicional que irá mostrar por pouco tempo o nome do jogo na tela
    if tempo_total > 102:
        formatacao_nome_jogo = fonte_tempo.render('W  O  R  D', True, (118, 225, 115, 255), (48, 15, 158, 255))
        janela.blit(formatacao_nome_jogo, (470, 30))

        nome_jogo = Letras('Z  A  P  P  E  R')
        Letras.posicao_letra(nome_jogo, 400, 114)

    # Condicional que irá resetar o jogador e todas as posições das letras do jogo
    if tempo_total <= 0:
        tempo_total = 108

        exibir_ganho = False

        jogador_posicao_x = 380
        jogador_posicao_y = 460

        # Posições x das letras
        posicao_letras_A_x, posicao_letras_B_x, posicao_letras_C_x, posicao_letras_D_x = 1260, 1350, 1435, 1520
        posicao_letras_E_x, posicao_letras_F_x, posicao_letras_G_x, posicao_letras_H_x = 1605, 1690, 1770, 1860
        posicao_letras_I_x, posicao_letras_J_x, posicao_letras_K_x, posicao_letras_L_x = 1944, 2005, 2085, 2175
        posicao_letras_M_x, posicao_letras_N_x, posicao_letras_O_x, posicao_letras_P_x = 2255, 2357, 2447, 2535
        posicao_letras_Q_x, posicao_letras_R_x, posicao_letras_S_x, posicao_letras_T_x = 2619, 2705, 2790, 2875
        posicao_letras_U_x, posicao_letras_V_x, posicao_letras_W_x, posicaoLetrasX_x = 2960, 3040, 3120, 3212
        posicao_letras_Y_x, posicaoLetrasZ_x, posicao_caractere_x = 3293, 3377, 3462

        posicao_letras_y['A'] = 114
        posicao_letras_y['B'] = 114
        posicao_letras_y['C'] = 114
        posicao_letras_y['D'] = 114
        posicao_letras_y['E'] = 114
        posicao_letras_y['F'] = 114
        posicao_letras_y['G'] = 114
        posicao_letras_y['H'] = 114
        posicao_letras_y['I'] = 114
        posicao_letras_y['J'] = 114
        posicao_letras_y['K'] = 114
        posicao_letras_y['L'] = 114
        posicao_letras_y['M'] = 114
        posicao_letras_y['N'] = 114
        posicao_letras_y['O'] = 114
        posicao_letras_y['P'] = 114
        posicao_letras_y['Q'] = 114
        posicao_letras_y['R'] = 114
        posicao_letras_y['S'] = 114
        posicao_letras_y['T'] = 114
        posicao_letras_y['U'] = 114
        posicao_letras_y['V'] = 114
        posicao_letras_y['W'] = 114
        posicao_letras_y['X'] = 114
        posicao_letras_y['Y'] = 114
        posicao_letras_y['Z'] = 114
        posicao_letras_y['*'] = 114

    # Condicionais que fazem a letra voltar para o começo após utrapassar a coordenada demarcada
    if posicao_letras_A_x < coordenada_final:
        posicao_letras_A_x = resetar_x
        posicao_letras_y['A'] = 114

    if posicao_letras_B_x < coordenada_final:
        posicao_letras_B_x = resetar_x
        posicao_letras_y['B'] = 114

    if posicao_letras_C_x < coordenada_final:
        posicao_letras_C_x = resetar_x
        posicao_letras_y['C'] = 114

    if posicao_letras_D_x < coordenada_final:
        posicao_letras_D_x = resetar_x
        posicao_letras_y['D'] = 114

    if posicao_letras_E_x < coordenada_final:
        posicao_letras_E_x = resetar_x
        posicao_letras_y['E'] = 114

    if posicao_letras_F_x < coordenada_final:
        posicao_letras_F_x = resetar_x
        posicao_letras_y['F'] = 114

    if posicao_letras_G_x < coordenada_final:
        posicao_letras_G_x = resetar_x
        posicao_letras_y['G'] = 114

    if posicao_letras_H_x < coordenada_final:
        posicao_letras_H_x = resetar_x
        posicao_letras_y['H'] = 114

    if posicao_letras_I_x < coordenada_final:
        posicao_letras_I_x = resetar_x
        posicao_letras_y['I'] = 114

    if posicao_letras_J_x < coordenada_final:
        posicao_letras_J_x = resetar_x
        posicao_letras_y['J'] = 114

    if posicao_letras_K_x < coordenada_final:
        posicao_letras_K_x = resetar_x
        posicao_letras_y['K'] = 114

    if posicao_letras_L_x < coordenada_final:
        posicao_letras_L_x = resetar_x
        posicao_letras_y['L'] = 114

    if posicao_letras_M_x < coordenada_final:
        posicao_letras_M_x = resetar_x
        posicao_letras_y['M'] = 114

    if posicao_letras_N_x < coordenada_final:
        posicao_letras_N_x = resetar_x
        posicao_letras_y['N'] = 114

    if posicao_letras_O_x < coordenada_final:
        posicao_letras_O_x = resetar_x
        posicao_letras_y['O'] = 114

    if posicao_letras_P_x < coordenada_final:
        posicao_letras_P_x = resetar_x
        posicao_letras_y['P'] = 114

    if posicao_letras_Q_x < coordenada_final:
        posicao_letras_Q_x = resetar_x
        posicao_letras_y['Q'] = 114

    if posicao_letras_R_x < coordenada_final:
        posicao_letras_R_x = resetar_x
        posicao_letras_y['R'] = 114

    if posicao_letras_S_x < coordenada_final:
        posicao_letras_S_x = resetar_x
        posicao_letras_y['S'] = 114

    if posicao_letras_T_x < coordenada_final:
        posicao_letras_T_x = resetar_x
        posicao_letras_y['T'] = 114

    if posicao_letras_U_x < coordenada_final:
        posicao_letras_U_x = resetar_x
        posicao_letras_y['U'] = 114

    if posicao_letras_V_x < coordenada_final:
        posicao_letras_V_x = resetar_x
        posicao_letras_y['V'] = 114

    if posicao_letras_W_x < coordenada_final:
        posicao_letras_W_x = resetar_x
        posicao_letras_y['W'] = 114

    if posicaoLetrasX_x < coordenada_final:
        posicaoLetrasX_x = resetar_x
        posicao_letras_y['X'] = 114

    if posicao_letras_Y_x < coordenada_final:
        posicao_letras_Y_x = resetar_x
        posicao_letras_y['Y'] = 114

    if posicaoLetrasZ_x < coordenada_final:
        posicaoLetrasZ_x = resetar_x
        posicao_letras_y['Z'] = 114

    if posicao_caractere_x < coordenada_final:
        posicao_caractere_x = resetar_x
        posicao_letras_y['*'] = 114

    # Aplicando a classe de Letra para criar as letras do alfabeto
    letra_A, letra_B, letra_C, letra_D = Letras('A'), Letras('B'), Letras('C'), Letras('D')
    letra_E, letra_F, letra_G, letra_H = Letras('E'), Letras('F'), Letras('G'), Letras('H')
    letra_I, letra_J, letra_K, letra_L = Letras('I'), Letras('J'), Letras('K'), Letras('L')
    letra_M, letra_N, letra_O, letra_P = Letras('M'), Letras('N'), Letras('O'), Letras('P')
    letra_Q, letra_R, letra_S, letra_T = Letras('Q'), Letras('R'), Letras('S'), Letras('T')
    letra_U, letra_V, letra_W, letra_X = Letras('U'), Letras('V'), Letras('W'), Letras('X')
    letra_Y, letra_Z, caractere = Letras('Y'), Letras('Z'), Letras('*')

    if tempo_total <= 104:
        # Atribuindo velocidade igual nas letras
        posicao_letras_A_x -= velocidade_letras
        posicao_letras_B_x -= velocidade_letras
        posicao_letras_C_x -= velocidade_letras
        posicao_letras_D_x -= velocidade_letras
        posicao_letras_E_x -= velocidade_letras
        posicao_letras_F_x -= velocidade_letras
        posicao_letras_G_x -= velocidade_letras
        posicao_letras_H_x -= velocidade_letras
        posicao_letras_I_x -= velocidade_letras
        posicao_letras_J_x -= velocidade_letras
        posicao_letras_K_x -= velocidade_letras
        posicao_letras_L_x -= velocidade_letras
        posicao_letras_M_x -= velocidade_letras
        posicao_letras_N_x -= velocidade_letras
        posicao_letras_O_x -= velocidade_letras
        posicao_letras_P_x -= velocidade_letras
        posicao_letras_Q_x -= velocidade_letras
        posicao_letras_R_x -= velocidade_letras
        posicao_letras_S_x -= velocidade_letras
        posicao_letras_T_x -= velocidade_letras
        posicao_letras_U_x -= velocidade_letras
        posicao_letras_V_x -= velocidade_letras
        posicao_letras_W_x -= velocidade_letras
        posicaoLetrasX_x -= velocidade_letras
        posicao_letras_Y_x -= velocidade_letras
        posicaoLetrasZ_x -= velocidade_letras
        posicao_caractere_x -= velocidade_letras

    # Usando uma subfunção ou metódo para, posicionar as letras na tela
    Letras.posicao_letra(letra_A, posicao_letras_A_x, posicao_letras_y['A'])
    Letras.posicao_letra(letra_B, posicao_letras_B_x, posicao_letras_y['B'])
    Letras.posicao_letra(letra_C, posicao_letras_C_x, posicao_letras_y['C'])
    Letras.posicao_letra(letra_D, posicao_letras_D_x, posicao_letras_y['D'])
    Letras.posicao_letra(letra_E, posicao_letras_E_x, posicao_letras_y['E'])
    Letras.posicao_letra(letra_F, posicao_letras_F_x, posicao_letras_y['F'])
    Letras.posicao_letra(letra_G, posicao_letras_G_x, posicao_letras_y['G'])
    Letras.posicao_letra(letra_H, posicao_letras_H_x, posicao_letras_y['H'])
    Letras.posicao_letra(letra_I, posicao_letras_I_x, posicao_letras_y['I'])
    Letras.posicao_letra(letra_J, posicao_letras_J_x, posicao_letras_y['J'])
    Letras.posicao_letra(letra_K, posicao_letras_K_x, posicao_letras_y['K'])
    Letras.posicao_letra(letra_L, posicao_letras_L_x, posicao_letras_y['L'])
    Letras.posicao_letra(letra_M, posicao_letras_M_x, posicao_letras_y['M'])
    Letras.posicao_letra(letra_N, posicao_letras_N_x, posicao_letras_y['N'])
    Letras.posicao_letra(letra_O, posicao_letras_O_x, posicao_letras_y['O'])
    Letras.posicao_letra(letra_P, posicao_letras_P_x, posicao_letras_y['P'])
    Letras.posicao_letra(letra_Q, posicao_letras_Q_x, posicao_letras_y['Q'])
    Letras.posicao_letra(letra_R, posicao_letras_R_x, posicao_letras_y['R'])
    Letras.posicao_letra(letra_S, posicao_letras_S_x, posicao_letras_y['S'])
    Letras.posicao_letra(letra_T, posicao_letras_T_x, posicao_letras_y['T'])
    Letras.posicao_letra(letra_U, posicao_letras_U_x, posicao_letras_y['U'])
    Letras.posicao_letra(letra_V, posicao_letras_V_x, posicao_letras_y['V'])
    Letras.posicao_letra(letra_W, posicao_letras_W_x, posicao_letras_y['W'])
    Letras.posicao_letra(letra_X, posicaoLetrasX_x, posicao_letras_y['X'])
    Letras.posicao_letra(letra_Y, posicao_letras_Y_x, posicao_letras_y['Y'])
    Letras.posicao_letra(letra_Z, posicaoLetrasZ_x, posicao_letras_y['Z'])
    Letras.posicao_letra(caractere, posicao_caractere_x, posicao_letras_y['*'] + 2)

    # Usando a classe Interrogações para criar variáveis com a quantidade de interrogações necessária
    interrogacao1, interrogacao2, interrogacao3, interrogacao4, interrogacao5, \
        interrogacao6 = Interrogacao(interrogacao_letra1), Interrogacao(interrogacao_letra2), \
        Interrogacao(interrogacao_letra3), Interrogacao(interrogacao_letra4), Interrogacao(interrogacao_letra5), \
        Interrogacao(interrogacao_letra6)

    # Posiciona as interrogações na tela
    Interrogacao.posicao_interrogacao(interrogacao1, pos_interrogacao_x, pos_interrogacao_y)
    Interrogacao.posicao_interrogacao(interrogacao2, pos_interrogacao_x + distancia_interrogacoes, pos_interrogacao_y)
    Interrogacao.posicao_interrogacao(interrogacao3, pos_interrogacao_x + distancia_interrogacoes * 2, pos_interrogacao_y)
    Interrogacao.posicao_interrogacao(interrogacao4, pos_interrogacao_x + distancia_interrogacoes * 3, pos_interrogacao_y)
    Interrogacao.posicao_interrogacao(interrogacao5, pos_interrogacao_x + distancia_interrogacoes * 4, pos_interrogacao_y)
    Interrogacao.posicao_interrogacao(interrogacao6, pos_interrogacao_x + distancia_interrogacoes * 5, pos_interrogacao_y)

    # Só permite o inimigo aparecer na tela após a contagem do tempo começar a aparecer na tela
    if tempo_total < 102:
        # Posiciona o inimigo na tela através de variáveis
        inimigo_direita1 = Inimigo(posicao_inimiga_direita_x1, inimigo_posicao_y)
        inimigo_direita2 = Inimigo(posicao_inimiga_direita_x2, inimigo_posicao_y - 50)
        inimigo_direita3 = Inimigo(posicao_inimiga_direita_x3, inimigo_posicao_y - 100)
        inimigo_direita4 = Inimigo(posicao_inimiga_direita_x4, inimigo_posicao_y - 150)
        inimigo_direita5 = Inimigo(posicao_inimiga_direita_x5, inimigo_posicao_y - 200)
        inimigo_direita6 = Inimigo(posicao_inimiga_direita_x6, inimigo_posicao_y - 250)

        # Posiciona o inimigo na tela através de variáveis
        inimigo_esquerda1 = Inimigo(posicao_inimiga_esquerda_x1, inimigo_posicao_y)
        inimigo_esquerda2 = Inimigo(posicao_inimiga_esquerda_x2, inimigo_posicao_y - 50)
        inimigo_esquerda3 = Inimigo(posicao_inimiga_esquerda_x3, inimigo_posicao_y - 100)
        inimigo_esquerda4 = Inimigo(posicao_inimiga_esquerda_x4, inimigo_posicao_y - 150)
        inimigo_esquerda5 = Inimigo(posicao_inimiga_esquerda_x5, inimigo_posicao_y - 200)
        inimigo_esquerda6 = Inimigo(posicao_inimiga_esquerda_x6, inimigo_posicao_y - 250)

        # Atribuindo velocidades diferentes para cada inimigo, indo e voltando
        posicao_inimiga_direita_x1 -= velocidades_inimiga_escolha1
        posicao_inimiga_direita_x2 -= velocidades_inimiga_escolha2
        posicao_inimiga_direita_x3 -= velocidades_inimiga_escolha3
        posicao_inimiga_direita_x4 -= velocidades_inimiga_escolha4
        posicao_inimiga_direita_x5 -= velocidades_inimiga_escolha5
        posicao_inimiga_direita_x6 -= velocidades_inimiga_escolha6

        posicao_inimiga_esquerda_x1 += velocidades_inimiga_escolha7
        posicao_inimiga_esquerda_x2 += velocidades_inimiga_escolha8
        posicao_inimiga_esquerda_x3 += velocidades_inimiga_escolha9
        posicao_inimiga_esquerda_x4 += velocidades_inimiga_escolha10
        posicao_inimiga_esquerda_x5 += velocidades_inimiga_escolha11
        posicao_inimiga_esquerda_x6 += velocidades_inimiga_escolha12

    # O inimigo da esquerda se movimentará para a direita, até que o da direita atinja -100 e ele então possa voltar
    if posicao_inimiga_esquerda_x1 > 1300:
        posicao_inimiga_direita_x1 = 1300
        velocidades_inimiga_escolha1 = random.choice(velocidades_inimiga)

    if posicao_inimiga_esquerda_x2 > 1300:
        posicao_inimiga_direita_x2 = 1300
        velocidades_inimiga_escolha2 = random.choice(velocidades_inimiga)

    if posicao_inimiga_esquerda_x3 > 1300:
        posicao_inimiga_direita_x3 = 1300
        velocidades_inimiga_escolha3 = random.choice(velocidades_inimiga)

    if posicao_inimiga_esquerda_x4 > 1300:
        posicao_inimiga_direita_x4 = 1300
        velocidades_inimiga_escolha4 = random.choice(velocidades_inimiga)

    if posicao_inimiga_esquerda_x5 > 1300:
        posicao_inimiga_direita_x5 = 1300
        velocidades_inimiga_escolha5 = random.choice(velocidades_inimiga)

    if posicao_inimiga_esquerda_x6 > 1300:
        posicao_inimiga_direita_x6 = 1300
        velocidades_inimiga_escolha6 = random.choice(velocidades_inimiga)

    # Em quanto o inimigo da direita tiver a posição maior que -100, o inimigo da esquerda se manterá na posição -100
    if posicao_inimiga_direita_x1 > -100:
        posicao_inimiga_esquerda_x1 = -100
        velocidades_inimiga_escolha7 = random.choice(velocidades_inimiga)

    if posicao_inimiga_direita_x2 > -100:
        posicao_inimiga_esquerda_x2 = -100
        velocidades_inimiga_escolha8 = random.choice(velocidades_inimiga)

    if posicao_inimiga_direita_x3 > -100:
        posicao_inimiga_esquerda_x3 = -100
        velocidades_inimiga_escolha9 = random.choice(velocidades_inimiga)

    if posicao_inimiga_direita_x4 > -100:
        posicao_inimiga_esquerda_x4 = -100
        velocidades_inimiga_escolha10 = random.choice(velocidades_inimiga)

    if posicao_inimiga_direita_x5 > -100:
        posicao_inimiga_esquerda_x5 = -100
        velocidades_inimiga_escolha11 = random.choice(velocidades_inimiga)

    if posicao_inimiga_direita_x6 > -100:
        posicao_inimiga_esquerda_x6 = -100
        velocidades_inimiga_escolha12 = random.choice(velocidades_inimiga)

    # Garante que não tenha nenhum erro com a escolha da palavra, e quando escolhe outra palavra, coloca a sobra exata
    # de interrogações
    if tempo_total == 103 or tempo_total == 102:
        if len(palavra_sorteada) == 6:
            interrogacao_letra1, interrogacao_letra2, interrogacao_letra3, interrogacao_letra4, interrogacao_letra5, \
                interrogacao_letra6 = palavra_sorteada[0], palavra_sorteada[1], palavra_sorteada[2], palavra_sorteada[3], \
                palavra_sorteada[4], palavra_sorteada[5]

        elif len(palavra_sorteada) == 5:
            interrogacao_letra1, interrogacao_letra2, interrogacao_letra3, interrogacao_letra4, \
                interrogacao_letra5 = palavra_sorteada[0], palavra_sorteada[1], palavra_sorteada[2], palavra_sorteada[3], \
                palavra_sorteada[4]
            interrogacao_letra6 = '?'

        elif len(palavra_sorteada) == 4:
            interrogacao_letra1, interrogacao_letra2, interrogacao_letra3, interrogacao_letra4 = palavra_sorteada[0], \
                palavra_sorteada[1], palavra_sorteada[2], palavra_sorteada[3]
            interrogacao_letra6, interrogacao_letra5 = '?', '?'

        elif len(palavra_sorteada) == 3:
            interrogacao_letra1, interrogacao_letra2, interrogacao_letra3 = palavra_sorteada[0], palavra_sorteada[1], \
                palavra_sorteada[2]
            interrogacao_letra6, interrogacao_letra5, interrogacao_letra4 = '?', '?', '?'

        elif len(palavra_sorteada) == 2:
            interrogacao_letra1, interrogacao_letra2 = palavra_sorteada[0], palavra_sorteada[1]
            interrogacao_letra6, interrogacao_letra5, interrogacao_letra4, interrogacao_letra3 = '?', '?', '?', '?'

    # Faz a palavra "sumir" da tela
    elif tempo_total == 101:
        interrogacao_letra1, interrogacao_letra2, interrogacao_letra3, interrogacao_letra4, interrogacao_letra5, \
            interrogacao_letra6 = '?', '?', '?', '?', '?', '?'

    # Verifica se o jogador acertou a letra correta
    else:
        if tempo_total <= 102:
            # Tecla de disparo lazer
            if comandos[pygame.K_SPACE]:
                disparo_lazer_jogador = Retangulo_Colisao(
                    249, 255, 87, 255, jogador_posicao_x + 34, jogador_posicao_y - 460, lazer_jogador_x, lazer_jogador_y)

                efeito_sonoro_tiro.play()

                verificacao_letra(rect_letra_A, "A")
                verificacao_letra(rect_letra_B, "B")
                verificacao_letra(rect_letra_C, "C")
                verificacao_letra(rect_letra_D, "D")
                verificacao_letra(rect_letra_E, "E")
                verificacao_letra(rect_letra_F, "F")
                verificacao_letra(rect_letra_G, "G")
                verificacao_letra(rect_letra_H, "H")
                verificacao_letra(rect_letra_I, "I")
                verificacao_letra(rect_letra_J, "J")
                verificacao_letra(rect_letra_K, "K")
                verificacao_letra(rect_letra_L, "L")
                verificacao_letra(rect_letra_M, "M")
                verificacao_letra(rect_letra_N, "N")
                verificacao_letra(rect_letra_O, "O")
                verificacao_letra(rect_letra_P, "P")
                verificacao_letra(rect_letra_Q, "Q")
                verificacao_letra(rect_letra_R, "R")
                verificacao_letra(rect_letra_S, "S")
                verificacao_letra(rect_letra_T, "T")
                verificacao_letra(rect_letra_U, "U")
                verificacao_letra(rect_letra_V, "V")
                verificacao_letra(rect_letra_W, "W")
                verificacao_letra(rect_letra_X, "X")
                verificacao_letra(rect_letra_Y, "Y")
                verificacao_letra(rect_letra_Z, "Z")

                # Se a pessoa pensa que terminou a palavra, ela pode enviar a mesma, como concluída, pelo asterisco
                if rect_caractere.colide_retangulo(disparo_lazer_jogador):

                    # Lista com todas as icógnitas e não icógnitas na tela
                    lista_formada6 = [interrogacao_letra1, interrogacao_letra2, interrogacao_letra3, interrogacao_letra4,
                                     interrogacao_letra5, interrogacao_letra6]

                    # Filtrador de interrogações
                    lista_formada_sem_interrogacoes = list(filter(lambda x: x != '?', lista_formada6))
                    # Junta as palavras
                    palavra_formada = "".join(lista_formada_sem_interrogacoes)

                    # Transforma todas as palavras da listaPalavras, para maiúsculas
                    lista_palavras_maiusculas = [palavra.upper() for palavra in lista_palavras]

                    if palavra_formada in lista_palavras_maiusculas:
                        exibir_ganho = True

                    if palavra_formada not in lista_palavras_maiusculas:
                        reiniciar = True

                    posicao_letras_y['A'] = 114
                    posicao_letras_y['B'] = 114
                    posicao_letras_y['C'] = 114
                    posicao_letras_y['D'] = 114
                    posicao_letras_y['E'] = 114
                    posicao_letras_y['F'] = 114
                    posicao_letras_y['G'] = 114
                    posicao_letras_y['H'] = 114
                    posicao_letras_y['I'] = 114
                    posicao_letras_y['J'] = 114
                    posicao_letras_y['K'] = 114
                    posicao_letras_y['L'] = 114
                    posicao_letras_y['M'] = 114
                    posicao_letras_y['N'] = 114
                    posicao_letras_y['O'] = 114
                    posicao_letras_y['P'] = 114
                    posicao_letras_y['Q'] = 114
                    posicao_letras_y['R'] = 114
                    posicao_letras_y['S'] = 114
                    posicao_letras_y['T'] = 114
                    posicao_letras_y['U'] = 114
                    posicao_letras_y['V'] = 114
                    posicao_letras_y['W'] = 114
                    posicao_letras_y['X'] = 114
                    posicao_letras_y['Y'] = 114
                    posicao_letras_y['Z'] = 114
                    posicao_letras_y['*'] = 114

                    # O subTempo inicia em 0, por isso que ao rodar o código de hierarquia acima, obrigatoriamente o
                    # de baixo irá rodar
                    if sub_tempo == 0:
                        # Somando 1 ao subtempo para controlar quantas vezes esse código pode ser executado por vez
                        sub_tempo += 1
                        # Acrescenta o tempo atual de jogo dentro de uma lista vazia
                        lista_tempo_para_pausa.append(tempo_total)

    if exibir_ganho:

        # Lista com todas as icógnitas e não icógnitas na tela
        lista_formada6 = [interrogacao_letra1, interrogacao_letra2, interrogacao_letra3, interrogacao_letra4,
                            interrogacao_letra5, interrogacao_letra6]

        # Filtrador de interrogações
        lista_formada_sem_interrogacoes = list(filter(lambda x: x != '?', lista_formada6))
        # Junta as palavras
        palavra_formada = "".join(lista_formada_sem_interrogacoes)

        # Transforma todas as palavras da listaPalavras, para maiúsculas
        lista_palavras_maiusculas = [palavra.upper() for palavra in lista_palavras]
        
        # Verifica se a palavra montada pertence a minha lista
        # Se sim, a mensagem de pontuação será apresentada
        if palavra_formada in lista_palavras_maiusculas:
            contador_tempo_ganho += 1
            # Mostra a mensagem de ganho de pontuação na tela
            ganho = 75
            string_ganho = (f'+ {ganho} PONTOS')
            fonte_ganho_pontos = pygame.font.Font(None, 70)
            formatacao_ganho = fonte_ganho_pontos.render(string_ganho, True, (0, 255, 0), (48, 15, 158, 255))
            janela.blit(formatacao_ganho, (450, 300))
            if contador_tempo_ganho == 1:
                pontuacao_jogador += ganho

            if contador_tempo_ganho == 2:
                reiniciar = True

            if contador_tempo_ganho == 25:
                exibir_ganho = False
                contador_tempo_ganho = 0

    if reiniciar:
        # posicionamento do jogador
        jogador_posicao_x = 380
        jogador_posicao_y = 460

        # Posições x das letras
        posicao_letras_A_x, posicao_letras_B_x, posicao_letras_C_x, posicao_letras_D_x = 1260, 1350, 1435, 1520
        posicao_letras_E_x, posicao_letras_F_x, posicao_letras_G_x, posicao_letras_H_x = 1605, 1690, 1770, 1860
        posicao_letras_I_x, posicao_letras_J_x, posicao_letras_K_x, posicao_letras_L_x = 1944, 2005, 2085, 2175
        posicao_letras_M_x, posicao_letras_N_x, posicao_letras_O_x, posicao_letras_P_x = 2255, 2357, 2447, 2535
        posicao_letras_Q_x, posicao_letras_R_x, posicao_letras_S_x, posicao_letras_T_x = 2619, 2705, 2790, 2875
        posicao_letras_U_x, posicao_letras_V_x, posicao_letras_W_x, posicaoLetrasX_x = 2960, 3040, 3120, 3212
        posicao_letras_Y_x, posicaoLetrasZ_x, posicao_caractere_x = 3293, 3377, 3462

        # Nascimento inimigo à direita
        posicao_inimiga_direita_x1 = 2500
        posicao_inimiga_direita_x2 = 2500
        posicao_inimiga_direita_x3 = 2500
        posicao_inimiga_direita_x4 = 2500
        posicao_inimiga_direita_x5 = 2500
        posicao_inimiga_direita_x6 = 2500

        # Nascimento inimigo à esquerda
        posicao_inimiga_esquerda_x1 = -100
        posicao_inimiga_esquerda_x2 = -100
        posicao_inimiga_esquerda_x3 = -100
        posicao_inimiga_esquerda_x4 = -100
        posicao_inimiga_esquerda_x5 = -100
        posicao_inimiga_esquerda_x6 = -100

        # Escolhe uma palavra aleatóriamente
        palavra_escolhida = random.choice(lista_palavras)
        palavra_sorteada = palavra_escolhida.upper()

        # Garante que não tenha nenhum erro com a escolha da palavra, e quando escolhe outra palavra,
        # coloca a sobra exata de interrogações
        if len(palavra_sorteada) == 6:
            interrogacao_letra1, interrogacao_letra2, interrogacao_letra3, interrogacao_letra4, \
                interrogacao_letra5, interrogacao_letra6 = palavra_sorteada[0], palavra_sorteada[1], \
                palavra_sorteada[2], palavra_sorteada[3], palavra_sorteada[4], palavra_sorteada[5]

        elif len(palavra_sorteada) == 5:
            interrogacao_letra1, interrogacao_letra2, interrogacao_letra3, interrogacao_letra4, \
                interrogacao_letra5 = palavra_sorteada[0], palavra_sorteada[1], palavra_sorteada[2], \
                palavra_sorteada[3], palavra_sorteada[4]
            interrogacao_letra6 = '?'

        elif len(palavra_sorteada) == 4:
            interrogacao_letra1, interrogacao_letra2, interrogacao_letra3, interrogacao_letra4 = \
                palavra_sorteada[0], palavra_sorteada[1], palavra_sorteada[2], palavra_sorteada[3]
            interrogacao_letra6, interrogacao_letra5 = '?', '?'

        elif len(palavra_sorteada) == 3:
            interrogacao_letra1, interrogacao_letra2, interrogacao_letra3 = palavra_sorteada[0], \
                palavra_sorteada[1], palavra_sorteada[2]
            interrogacao_letra6, interrogacao_letra5, interrogacao_letra4 = '?', '?', '?'

        elif len(palavra_sorteada) == 2:
            interrogacao_letra1, interrogacao_letra2 = palavra_sorteada[0], palavra_sorteada[1]
            interrogacao_letra6, interrogacao_letra5, interrogacao_letra4, interrogacao_letra3 = '?', '?', \
                '?', '?'
        reiniciar = False

    # Condicional que será executada apenas se a lista onde foi armazenada o tempo atual do jogo estiver diferente de
    # vazia
    if len(lista_tempo_para_pausa) != 0:
        # Esconde o tempo de verdade no fundo do tempo parado falso
        rect_pausa_tempo = pygame.draw.rect(janela, (48, 15, 158, 255,), (585, 25, 90, 80))

        # Transformando o tempo pausado em um texto
        tempo_parado_string = str(lista_tempo_para_pausa[0])
        # Formata e escreve a mensagem
        formatacao_tempo_parado = fonte_tempo.render(tempo_parado_string, True, (118, 225, 115, 255), (48, 15, 158, 255,))
        # Irá mostrar como se o tempo estivesse parado
        janela.blit(formatacao_tempo_parado, (590, 30))

        # Reseta o subTempo
        sub_tempo = 0

        # Faz uma conta baseada no tempo do jogo armazenado na lista vazia subtraído pela quantidade de tempo que eu
        # quero de "pausa", que nesse caso, é dois
        calculo_pausa_tempo = lista_tempo_para_pausa[0] - tempo_pausa

        # Se o tempo total do jogo for o mesmo da conta feita acima, ele reinicia as posições e ajusta as interrogações
        # para a aparecerem na tela no lugar da icógnita. Se o tempo Total for menor ou igual a 1, a condicional também
        # executará
        if tempo_total == calculo_pausa_tempo or tempo_total <= 1:
            tempo_total = lista_tempo_para_pausa[0]

            # Limpando as listas, para quando a ação for repetida não ocorrerem erros
            lista_tempo_para_pausa.clear()
            lista_palavra_sorteada.clear()

            # Transformando as letras em icógnitas para com interrogações
            interrogacao_letra1, interrogacao_letra2, interrogacao_letra3, interrogacao_letra4, interrogacao_letra5, \
                interrogacao_letra6 = '?', '?', '?', '?', '?', '?'

    # São os retângulos laterais 'invisíveis' pintados de preto de onde partirão os inimigos
    retangulo_direito = Retangulo(1058, 185, 202, 350)
    retangulo_esquerdo = Retangulo(0, 185, 204, 350)
    retangulo_esquerdo_cima = Retangulo(0, 110, 370, 74)
    retangulo_direito_cima = Retangulo(891, 110, 370, 74)

    # Condicional que apresenta a pontuação final do jogador
    if tempo_total > 104:
        fonte_vitoria = pygame.font.Font(None, 65)
        pontuacao_jogador_string = str(f"PONTUAÇÃO TOTAL: {pontuacao_jogador}")
        formatacao_pontuacao = fonte_vitoria.render(pontuacao_jogador_string, True, (182, 201, 96, 255),
                                                  (48, 15, 158, 255))
        janela.blit(formatacao_pontuacao, (378, 300))

    # Posiciona o jogador nas coordenadas das variáveis
    janela.blit(imagem_jogador, (jogador_posicao_x, jogador_posicao_y))

    # Atualiza a tela períodicamente
    pygame.display.update()

pygame.mixer.music.stop()
# Saindo do jogo e finalizando o programa
pygame.quit()
