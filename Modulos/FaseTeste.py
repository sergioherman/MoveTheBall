from PPlay.gameimage import GameImage
from PPlay.sprite import *
from PPlay.window import *

def iniciarfase05():
    janela = Window(1320, 630)
    teclado = Window.get_keyboard()
    fundo = GameImage("../Imagens/Fundo.png")
    bola = Sprite("../Imagens/BolaVermelha.png")
    chao = GameImage("../Imagens/Chao.png")
    quadrado = GameImage("../Imagens/quadrado3.png")
    quadrado.x = 1262
    quadrado.y = 52
    iconepuloduplo = GameImage("../Imagens/IconePuloDuplo.png")
    iconepuloduplo.x = 1200
    iconepuloduplo.y = 590

    setacima = GameImage("../Imagens/setacima.png")
    setacima.x = 20
    setacima.y = 530

    bola.x = janela.width/2 - bola.width/2
    bola.y = 150
    chao.y = 570

    vbolax = 150
    vbolay = -300

    acelerax = 2
    vpulo = 700

    gravidade = 900
    amortecimentoy = 1.003
    amortecimentox = 1.0015

    podepular = False
    podeDarSegundoPulo = False
    deuSegundoPulo = False
    quicou = True

    vminsegundopulo = 100

    debug = True
    esperaInicial = True
    tempoEsperaInicial = 2

    contaquique = 0
    alturamaxima = 0

    tempo = 0
    tempolooprastro = 0
    tempointervalorastros = 0.04
    numrastros = 50
    opacidaderastro = 0.3
    colocarrastro = False
    vetrastro = []



    while True:

        #Espera Inicial
        contEsperaInicial = 0
        while esperaInicial:
            contEsperaInicial += janela.delta_time()
            if contEsperaInicial > tempoEsperaInicial:
                esperaInicial = False
            fundo.draw()
            chao.draw()
            janela.draw_text(str(int(1+(tempoEsperaInicial-contEsperaInicial)*1.5)), janela.width / 2, 200, 70, (255, 255, 255), "Calibri", True)
            janela.update()

        deltat = janela.delta_time()
        tempo += deltat
        tempolooprastro += deltat
        colocarrastro = False
        if tempolooprastro > tempointervalorastros:
            tempolooprastro = 0
            colocarrastro = True
        if colocarrastro:
            rastro = GameImage("../Imagens/rastro.png")
            rastro.x = bola.x + bola.width/2 - rastro.width/2
            rastro.y = bola.y + bola.height/2 - rastro.height/2
            vetrastro.append(rastro)
        if len(vetrastro)>numrastros:
            vetrastro.remove(vetrastro[0])
        for i in range(len(vetrastro)):
            vetrastro[i].image.set_alpha((255 - 255 * (numrastros - i) / numrastros)*opacidaderastro)

        iconepuloduplo.image.set_alpha(40)
        vbolayanterior = vbolay
        vbolay = (vbolay/amortecimentoy) + gravidade * deltat
        vbolax = (vbolax/amortecimentox)

        bola.x += vbolax * deltat
        bola.y += vbolay * deltat

        # amortecimentox = 1 + vbolax/100000
        # amortecimentoy = 1 + abs(vbolay/100000)

        if vbolayanterior * vbolay < 0:  # inversão do sinal da velocidade y
            alturamaxima = bola.y

        if bola.collided(chao):
            bola.x -= vbolax * deltat
            bola.y -= vbolay * deltat
            if abs(alturamaxima - bola.y) < 30 and vbolay > 12: #  Amortecimento potencializado
                vbolay = vbolay * 0.5
            vbolay = -vbolay
            if abs(alturamaxima - bola.y) > 0.5 and abs(vbolay) > 0:  # quando a altura maxima e a altura da colisão é menor que meio pixel
                contaquique = contaquique + 1
                quicou = True
                if debug:
                    print("Quicou ", contaquique)

        #  Movimento da bola
        if teclado.key_pressed("right"):
            vbolax = vbolax + acelerax
        if teclado.key_pressed("left"):
            vbolax = vbolax - acelerax

        # Pulo da Bola
        if abs(bola.y + bola.height - chao.y) < 5: # Se a bola tem apoio:
            podepular = True
        else:
            podepular = False
        if teclado.key_pressed("space") and podepular:
            vbolay = -vpulo
            contaquique = 0
            quicou = False
            deuSegundoPulo = False

        # Segundo Pulo da bola
        if vbolay > -vminsegundopulo and not quicou and not deuSegundoPulo:
            podeDarSegundoPulo = True
        else:
            podeDarSegundoPulo = False
        if teclado.key_pressed("space") and podeDarSegundoPulo:
            vbolay = - vpulo
            podeDarSegundoPulo = False
            deuSegundoPulo = True
            contaquique = 0


        # Paredes e teto
        if bola.x < 20:
            vbolax = abs(vbolax)
        if bola.x > 1300 - bola.width:
            vbolax = -abs(vbolax)
        if bola.y < 20:
            vbolay = abs(vbolay)

        # Seta de aceleração - melhorar limites
        if 15 < bola.x < 40 and 110 < bola.y < 570 :
            vbolay -= 10

        # Icone de segundo pulo
        if podeDarSegundoPulo:
            iconepuloduplo.image.set_alpha(255)
            bola.image.set_alpha(150)
        else:
            iconepuloduplo.image.set_alpha(40)
            bola.image.set_alpha(255)


        if bola.collided(quadrado):
            bola.x -= vbolax * deltat
            bola.y -= vbolay * deltat
            if bola.y >= quadrado.y - quadrado.height:
                vbolax = -vbolax
            if bola.x >= quadrado.x - quadrado.width:
                vbolay = -vbolay


        # Desenho
        fundo.draw()
        for i in vetrastro:
            i.draw()
        setacima.draw()
        quadrado.draw()
        bola.draw()
        chao.draw()
        iconepuloduplo.draw()

        janela.draw_text('Tempo: ' + str(int(tempo)),20,590,15,(255,255,255),"Calibri",True)
        janela.update()


    #  Buracos para Game Over e setas verder ao bater no quadrado
    #  Passa de fase ao subir em alguma fenda no teto
    #  bola muda de cor quando for permitido salto duplo
    #  efeito de poeira na base da bola ao saltar
    #  melhorar seta (colocar verde)
    #  fazer tutorial de sprite https://www.youtube.com/watch?v=svt2PuSM74Y
    #  Melhorar exibição do tempo
    #  Programar Game Over
    #  Fazer rastro