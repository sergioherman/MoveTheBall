from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
import random
import math

# Para iniciar a fase correta
def escolherfase(nfase):
    global entrar
    entrar = True
    while entrar:
        global numdafase, deltat
        numdafase = nfase
        if nfase == 1:
            iniciarfase01()
        elif nfase == 2:
            iniciarfase02()
        elif nfase == 3:
            iniciarfase03()
        elif nfase == 4:
            iniciarfase04()
        elif nfase == 5:
            iniciarfase05()
        elif nfase == 6:  # Fase 6 em construção
             iniciarfase06()

        else:
            numdafase -= 1
            entrar = False
    return numdafase


# Construir função para montagem das fases separadamente
# Fazer plataformas moveis
# Bug na plataforma movel quando há colisão lateral com a bola (independente de outra colisão simultanea com outra plataforma)
# Fazer Inimigos Móveis

# Fases
# Fase 6 em construção
def iniciarfase06():  # Em construção
    global jogando, passoudefase, gameover, numdafase, acseta
    configuracoesiniciaisfases()
#### Montar fase aqui
    colocarplataformamovel(3,14)
    montarchaointeiro()
    for i in range (5,14,2):
        for j in range (5,14):
            colocarsetaverde(i,j,'cima')
            colocarsetaverde(i+1,j,'baixo')

    colocarportal(31,3)

### Fim montar fase aqui

    while jogando:
        telajogo()
    if gameover:
        telagameover()
    if passoudefase:
        telapassoudefase()
        numdafase += 1
        escolherfase(numdafase)

def iniciarfase05():
    global jogando, passoudefase, gameover, numdafase, acseta
    configuracoesiniciaisfases()
#### Montar fase aqui
    for i in range (5,14):
        for j in range (5,14):
            colocarsetaverde(i,j,'cima')

    colocarportal(31,3)

### Fim montar fase aqui

    while jogando:
        telajogo()
    if gameover:
        telagameover()
    if passoudefase:
        telapassoudefase()
        numdafase += 1
        escolherfase(numdafase)

def iniciarfase04():
    global jogando, passoudefase, gameover, numdafase, acseta
    configuracoesiniciaisfases()
#### Montar fase aqui
    montarchaocomburacos([10,11,12,13,14,15])
    colocarinimigo(29,6)
    colocarinimigo(29,4)
    colocarinimigo(29,5)
    colocarportal(31,3)
    for i in range (3,15):
        colocarplataforma(5,i)
    for i in range (13,15):
        colocarsetaverde(1,i,'baixo')
        colocarsetaverde(2, i, 'baixo')
        colocarsetaverde(3, i, 'baixo')
    for i in range(3,11):
        colocarsetaverde(1,i,'baixo')
        colocarsetaverde(2,i,'cima')
        colocarsetaverde(3,i,'cima')
        colocarsetaverde(4,i,'baixo')

    colocarsetaverde(3,12,'esq')
    colocarsetaverde(2,12,'esq')
    colocarsetaverde(1,12,'esq')
    colocarsetaverde(3,11,'esq')
    colocarsetaverde(2,11,'esq')
    colocarsetaverde(1,11,'esq')
    for i in range(10,15):
        colocarsetaverde(i,5,'dir')
    for i in range(7,10):
        colocarsetaverde(10,i,'cima')
    colocarsetaverde(12,8,'baixo')
### Fim montar fase aqui

    while jogando:
        telajogo()
    if gameover:
        telagameover()
    if passoudefase:
        telapassoudefase()
        numdafase += 1
        escolherfase(numdafase)

def iniciarfase03():
    global jogando, passoudefase, gameover, numdafase, acseta
    configuracoesiniciaisfases()
    for i in range (1,4):
        colocarplataforma(i,4)
    for i in range(4,7):
        colocarsetaverde(i,15,'cima')
        colocarsetaverde(i, 14, 'cima')
        colocarsetaverde(i, 13, 'cima')
    for i in range(8,20):
        colocarsetaverde(i,15,'cima')
    for i in range(4,14):
        colocarsetaverde(18,i,'cima')
    for i in range(4, 14):
        colocarsetaverde(30, i, 'cima')
        colocarsetaverde(31, i, 'cima')
        colocarsetaverde(29, i, 'cima')

    colocarportal(31,1)

    while jogando:
        telajogo()
    if gameover:
        telagameover()
    if passoudefase:
        telapassoudefase()
        numdafase += 1
        escolherfase(numdafase)

def iniciarfase02():
    global jogando, passoudefase, gameover, numdafase
    configuracoesiniciaisfases()

    # montarchaoburacosrandom(3)
    # montarchaointeiro()
    montarchaocomburacos([13, 14, 15, 16, 17, 18, 19, 20 ,21, 22, 23, 24, 25, 26, 27, 28, 29, 30])  # vetor com a posição dos buracos no chao

    colocarplataforma(13,14) # posição da plataforma

    for i in range (1,14):
        colocarplataforma(i,10)
    for i in range (3,12):
        colocarplataforma(14,i)
    colocarportal(2,12)

    while jogando:
        telajogo()
    if gameover:
        telagameover()
    if passoudefase:
        telapassoudefase()
        numdafase += 1
        escolherfase(numdafase)

def iniciarfase01():
    global jogando, passoudefase, gameover, numdafase
    configuracoesiniciaisfases()

    # montarchaoburacosrandom(3)
    # montarchaointeiro()
    montarchaocomburacos([13, 14, 15, 16, 17, 18, 19, 20 ,21, 22, 23, 24, 25, 26, 27, 28, 29, 30])  # vetor com a posição dos buracos no chao
    for i in range (4,15):
        colocarsetaverde(1,i,'cima')
    colocarportal(31,1)

    while jogando:
        telajogo()
    if gameover:
        telagameover()
    if passoudefase:
        telapassoudefase()
        numdafase += 1
        escolherfase(numdafase)



# Montagem das fases
def montarchaoburacosrandom(buracosnochao):
    global numplatchao
    for i in range(0, numplatchao):
        plataforma = GameImage("../Imagens/Fases/plataforma.png")
        vetplatchao.append(plataforma)

    # Posicionar chao
    for i in range(0, numplatchao):
        vetplatchao[i].x = 20 + 40 * i
        vetplatchao[i].y = 570

    # Remover algumas plataformas
    minrandrange = 0
    for i in range(0, buracosnochao):
        randomgerado = random.randrange(minrandrange, numplatchao)
        vetplatchao.remove(vetplatchao[randomgerado])
        numplatchao -= 1

def montarchaointeiro():
    global numplatchao
    for i in range(0, numplatchao):
        plataforma = GameImage("../Imagens/Fases/plataforma.png")
        vetplatchao.append(plataforma)

    # Posicionar chao
    for i in range(0, numplatchao):
        vetplatchao[i].x = 20 + 40 * i
        vetplatchao[i].y = 570

def montarchaocomburacos(vetburacos):
    global numplatchao
    for i in range(0, numplatchao):
        plataforma = GameImage("../Imagens/Fases/plataforma.png")
        vetplatchao.append(plataforma)

    # Posicionar chao
    for i in range(0, numplatchao):
        vetplatchao[i].x = 20 + 40 * i
        vetplatchao[i].y = 570

    vetburacos.sort(reverse=True)
    for i in range(len(vetburacos)):
        vetplatchao.remove(vetplatchao[vetburacos[i]])
        numplatchao -= 1

def colocarplataforma(x,y):
    global vetplat
    plataforma = GameImage("../Imagens/Fases/plataforma.png")
    plataforma.x = 20 + 40 * (x - 1)
    plataforma.y = 10 + 40 * (y - 1)
    vetplat.append(plataforma)

def colocarinimigo(x,y):
    global vetinimigos
    inimigo = GameImage("../Imagens/Fases/inimigo.png")
    inimigo.x = 20 + (x - 1) * 40
    inimigo.y = 10 + (y - 1) * 40
    vetinimigos.append(inimigo)

def colocarsetaverde(x,y,dir):
    global vetsetacima, vetsetadir, vetsetabaixo, vetsetaesq
    if dir == 'cima':
        seta = GameImage("../Imagens/Fases/setaverdecima.png")
        seta.x = 20 + (x - 1) * 40
        seta.y = 10 + (y - 1) * 40
        vetsetacima.append(seta)
    if dir == 'baixo':
        seta = GameImage("../Imagens/Fases/setaverdebaixo.png")
        seta.x = 20 + (x - 1) * 40
        seta.y = 10 + (y - 1) * 40
        vetsetabaixo.append(seta)

    if dir == 'dir':
        seta = GameImage("../Imagens/Fases/setaverdedireita.png")
        seta.x = 20 + (x - 1) * 40
        seta.y = 10 + (y - 1) * 40
        vetsetadir.append(seta)
    if dir == 'esq':
        seta = GameImage("../Imagens/Fases/setaverdeesq.png")
        seta.x = 20 + (x - 1) * 40
        seta.y = 10 + (y - 1) * 40
        vetsetaesq.append(seta)

def colocarportal(x,y):
    global portal
    portal = GameImage("../Imagens/Fases/PortalGrande.png")
    portal.x = 20 + (x - 1) * 40
    portal.y = 10 + (y - 1) * 40

def colocarplataformamovel(x,y):
    global vetplatmovel
    plataforma = GameImage("../Imagens/Fases/plataformamovel.png")
    plataforma.x = 20 + 40 * (x - 1)
    plataforma.y = 22 + 40 * (y - 1)
    vetplatmovel.append(plataforma)



# Telas
def telaselecaofases(maxfasesdesbloq):
    janela = Window(1320, 660)
    teclado = janela.get_keyboard()
    mouse = Window.get_mouse()
    fundo = GameImage("../Imagens/MenuInicial/CenarioMenuInicial3.png")
    fundo.image.set_alpha(4)
    vetfases = []
    yquadfases = 300
    cont = 0
    for i in range(0, maxfasesdesbloq):
        quadfases = GameImage("../Imagens/Fases/plataforma.png")
        quadfases.x = 700 + 60 * cont
        quadfases.y = yquadfases
        quadfases.image.set_alpha(5)
        cont += 1
        if (i + 1) % 9 == 0:
            yquadfases += 60
            cont = 0
        vetfases.append(quadfases)
    while not teclado.key_pressed("esc"):
        cursor = mouse.get_position()
        cont = 0
        for quad in vetfases:
            cont += 1
            quad.image.set_alpha(5)
            if quad.x < cursor[0] < quad.x + quad.width and quad.y < cursor[1] < quad.y + quad.height:
                quad.image.set_alpha(255)
                if mouse.is_button_pressed(BUTTON_LEFT):
                    return cont
        fundo.draw()
        cont = 0
        for quad in vetfases:
            quad.draw()
            cont += 1
            if cont < 10:
                janela.draw_text('0'+str(cont),quad.x+10,quad.y+8,20,(0,0,0),"Calibri",True)
            else:
                janela.draw_text(str(cont),quad.x+8,quad.y+8,20,(0,0,0),"Calibri",True)
        janela.update()
    return 1

def telajogo():
    configuracoesdeloop()
    colisaocomseta()
    moverbolavert()
    moverbolahori()
    moverplataformamovel()
    colisaocomchao()
    colisaocomplataforma()
    colisaocomparedes()
    colisaocomteto()
    colisaocomplataformamovel()
    pular()
    segundopulo()
    configuracoesdesenho()
    verificagameover()
    verificapassoufase()
    fazerrastro()
    desenhar()  # separar em desenhar estatico e desenhar dinamico
    janela.update()

def telagameover():
    global janela, bola, vetinimigos, bateunoinimigo, tempoesperagameover, indiceinimigo
    contatempo = 0

    while tempoesperagameover > contatempo:
        contatempo += janela.delta_time()

        if bateunoinimigo:
            inimigosugabola()

        desenhar()
        janela.draw_text('Game Over',600,270,30,(255,255,255),"Calibri",True)

        janela.update()

def telapassoudefase():
    global janela, tempoesperapassoufase
    contatempo = 0
    while tempoesperapassoufase > contatempo:
        contatempo += janela.delta_time()
        moverbolahori()
        moverbolavert()
        colisaocomchao()
        colisaocomplataforma()
        colisaocomteto()
        colisaocomparedes()
        portalsugabola()
        desenhar()
        janela.draw_text('Parabéns!',600,270,30,(255,255,255),"Calibri",True)
        janela.update()



#Configurações
def configuracoesiniciaisfases():
    global vetplatchao, vetplat, fundo, janela, bola, teclado, numplatchao, velbolay, deltat, gravidade
    global velbolax, acelerax, amortecimento, amortecimentovert, amortecimentocolisao
    global xbolaant, ybolaant, velpulo, podepular, podedarsegundopulo, velsegundopulo, pulou
    global velativasegundopulo, jogando, passoudefase, gameover, tempo
    global freqbrilhoportal, brilhomaxportal, brilhominportal, alphaportal, tempoesperapassoufase
    global vetsetacima, vetsetadir, vetsetabaixo, vetsetaesq, acseta, vetinimigos, bateunoinimigo
    global tempoesperagameover, alphabola, temporastro, dtrastro, vetrastro, numrastros, opacidaderastros
    global vetplatmovel
    teclado = Window.get_keyboard()
    janela = Window(1320, 630)
    vetplatchao = []
    vetplat = []
    vetsetacima = []
    vetsetadir = []
    vetsetabaixo = []
    vetsetaesq = []
    vetinimigos = []
    vetplatmovel = []
    acseta = 2
    fundo = GameImage("../Imagens/Fases/Fundo.png")
    bola = Sprite("../Imagens/Fases/BolaVermelha.png")
    bola.x = 100
    bola.y = 60  # janela.height / 2 - bola.height / 2
    numplatchao = 32
    velbolay = 400
    deltat = 0
    gravidade = 900
    velbolax = 0
    acelerax = 2
    amortecimento = 1.0015
    amortecimentocolisao = 1.5
    amortecimentovert = 1.0015
    xbolaant = bola.x
    ybolaant = bola.y
    velpulo = 700
    velsegundopulo = 500
    podepular = False
    podedarsegundopulo = False
    velativasegundopulo = -100
    pulou = False
    jogando = True
    passoudefase = False
    gameover = False
    bateunoinimigo = False
    tempo = 0
    freqbrilhoportal = 3
    brilhomaxportal = 170
    brilhominportal = 70
    alphaportal = brilhominportal
    tempoesperapassoufase = 3
    tempoesperagameover = 1.5
    alphabola = 255
    temporastro = 0.04
    dtrastro = 0
    vetrastro = []
    numrastros = 50
    opacidaderastros = 0.3

def configuracoesdeloop():
    global podepular, podedarsegundopulo, deltat, tempo
    podepular = False
    deltat = janela.delta_time()
    if deltat > 0.1:
        deltat = 0
    tempo += deltat

def configuracoesdesenho():
    global podedarsegundopulo, bola, portal, tempo, brilhomaxportal, brilhominportal, freqbrilhoportal
    global alphaportal
    alphaportal = brilhominportal + abs( (brilhomaxportal - brilhominportal) * math.sin(tempo*freqbrilhoportal))
    portal.image.set_alpha(alphaportal)
    if podedarsegundopulo:
        bola.image.set_alpha(100)
    else:
        bola.image.set_alpha(255)



# Verificações
def verificagameover():
    global jogando, teclado, bola, janela, gameover, vetinimigos, bateunoinimigo, indiceinimigo, entrar
    if teclado.key_pressed("esc"):
        jogando = False
        entrar = False
    if bola.y > janela.height:
        jogando = False
        gameover = True

    indiceinimigo = 0
    for i in range(len(vetinimigos)):
        if bola.collided(vetinimigos[i]):
            indiceinimigo = i
            jogando = False
            gameover = True
            bateunoinimigo = True
            break

def verificapassoufase():
    global bola, portal, passoudefase, jogando
    if bola.collided(portal):
        passoudefase = True
        jogando = False



# Efeitos
def portalsugabola():
    global velbolax, velbolay, gravidade, bola, alphaportal, deltat, tempoesperapassoufase
    velbolax /= 1.01
    velbolay /= 1.01
    gravidade = 0

    xfinal = (portal.x + portal.width / 2) - bola.width / 2
    yfinal = (portal.y + portal.height / 2) - bola.height / 2

    bola.x = (100 * bola.x + xfinal)/101
    bola.y = (100 * bola.y + yfinal)/101

    alphaportal += (255/tempoesperapassoufase) * deltat
    portal.image.set_alpha(alphaportal)

def inimigosugabola():
    global velbolax, velbolay, gravidade, bola, deltat, indiceinimigo, vetinimigos, alphabola, tempoesperagameover
    velbolax /= 1.01
    velbolay /= 1.01
    gravidade = 0

    # bola.x = vetinimigos[indice].x
    # bola.y = vetinimigos[indice].y
    xfinal = (vetinimigos[indiceinimigo].x + vetinimigos[indiceinimigo].width / 2) - bola.width / 2
    yfinal = (vetinimigos[indiceinimigo].y + vetinimigos[indiceinimigo].height / 2) - bola.height / 2

    bola.x = (100 * bola.x + xfinal)/101
    bola.y = (100 * bola.y + yfinal)/101

    alphabola -= (255/tempoesperagameover) * deltat
    bola.image.set_alpha(alphabola)

def fazerrastro():
    global deltat, temporastro, dtrastro, vetrastro, bola, numrastros, opacidaderastros
    dtrastro += deltat
    if dtrastro > temporastro:
        rastro = GameImage("../Imagens/Fases/rastro.png")
        rastro.x = bola.x + bola.width / 2 - rastro.width / 2
        rastro.y = bola.y + bola.height / 2 - rastro.height / 2
        vetrastro.append(rastro)
        dtrastro = 0
    if len(vetrastro)>numrastros:
        vetrastro.remove(vetrastro[0])
    for i in range(len(vetrastro)):
        vetrastro[i].image.set_alpha((255 - 255 * (numrastros - i) / numrastros) * opacidaderastros)



# Movimento Bola
def moverbolahori():
    global velbolax, acelerax, deltat, amortecimento, xbolaant
    xbolaant = bola.x
    if teclado.key_pressed("right"):
        velbolax += acelerax
    if teclado.key_pressed("left"):
        velbolax -= acelerax
    velbolax /= amortecimento
    bola.x += velbolax * deltat

def moverbolavert():
    global velbolay, gravidade, deltat, amortecimentovert,ybolaant
    ybolaant = bola.y
    velbolay += gravidade * deltat
    velbolay /= amortecimentovert
    bola.y += velbolay * deltat

def pular():
    global teclado, velpulo, velbolay, podepular, pulou
    if teclado.key_pressed("space") and podepular:
        velbolay = - abs(velpulo)
        podepular = False
        pulou = True

def segundopulo():
    global teclado, velsegundopulo, velbolay, podedarsegundopulo, pulou, velativasegundopulo, bola
    if pulou and velbolay > velativasegundopulo:
        podedarsegundopulo = True
        if teclado.key_pressed("space"):
            velbolay = -abs(velsegundopulo)
            podedarsegundopulo = False
            pulou = False



# Movimento Elementos
def moverplataformamovel():
    global vetplatmovel, bola, tempo
    for plataforma in vetplatmovel:
        plataforma.x += math.cos(tempo*3)



# Colisões
def colisaocomparedes():
    global bola, velbolax, amortecimentocolisao, xbolaant
    if 20 > bola.x or bola.x > 1260:
        bola.x = xbolaant
        velbolax = - velbolax / amortecimentocolisao

def colisaocomteto():
    global bola, velbolay, amortecimentocolisao, ybolaant, podedarsegundopulo
    if bola.y < 20:
        bola.y = ybolaant
        velbolay = - velbolay / amortecimentocolisao
        podedarsegundopulo = False

def colisaocomchao():
    global vetplatchao, velbolax, velbolay, deltat, amortecimentocolisao, xbolaant, ybolaant, podepular, pulou
    global podedarsegundopulo
    for plataforma in vetplatchao:
        #  se a bola está ocupando o mesmo lugar que a plataforma:
        if plataforma.y - bola.height < bola.y < plataforma.y + plataforma.height and plataforma.x - bola.width < bola.x < plataforma.x + plataforma.width:
            # se o x anterior estava na faixa de x que a plataforma ocupa:
            if plataforma.x - bola.width < xbolaant < plataforma.x + plataforma.width:
                if plataforma.y - bola.height < bola.y:
                    podepular = True
                    pulou = False
                    podedarsegundopulo = False
                # dar um passo atrás na direção y
                bola.y -= velbolay * deltat
                velbolay = - velbolay / amortecimentocolisao
                bola.y += velbolay * deltat

            # se o y anterior da bola estava na faixa de ys que a plataforma ocupa:
            if plataforma.y - bola.height < ybolaant < plataforma.y + plataforma.height:
                # dar um passo atrás na direção x
                bola.x = xbolaant
                velbolax = - velbolax / amortecimentocolisao
                bola.x += velbolax * deltat

def colisaocomplataforma():
    global vetplat, velbolax, velbolay, deltat, amortecimentocolisao, xbolaant, ybolaant, podepular, pulou
    global podedarsegundopulo, vetplatmovel
    for plataforma in vetplat:
        #  se a bola está ocupando o mesmo lugar que a plataforma:
        if plataforma.y - bola.height < bola.y < plataforma.y + plataforma.height and plataforma.x - bola.width < bola.x < plataforma.x + plataforma.width:
            print("colidiu")
            # se o x anterior estava na faixa de x que a plataforma ocupa:
            if plataforma.x - bola.width < xbolaant < plataforma.x + plataforma.width:
                # permitir pulo somente em colisão de cima para baixo
                if plataforma.y + plataforma.height > ybolaant:
                    podepular = True
                    pulou = False
                    podedarsegundopulo = False

                # dar um passo atrás na direção y
                bola.y -= velbolay * deltat
                velbolay = - velbolay / amortecimentocolisao
                bola.y += velbolay * deltat

            # se o y anterior da bola estava na faixa de ys que a plataforma ocupa:
            if plataforma.y - bola.height < ybolaant < plataforma.y + plataforma.height:
                # dar um passo atrás na direção x
                bola.x = xbolaant
                velbolax = - velbolax / amortecimentocolisao
                bola.x += velbolax * deltat

def colisaocomplataformamovel():
    global vetplatmovel, velbolax, velbolay, deltat, amortecimentocolisao, xbolaant, ybolaant, podepular, pulou
    global podedarsegundopulo
    for plataforma in vetplatmovel:
        #  se a bola está ocupando o mesmo lugar que a plataforma:
        if plataforma.y - bola.height < bola.y < plataforma.y + plataforma.height and plataforma.x - bola.width < bola.x < plataforma.x + plataforma.width:
            print("colidiu")
            # se o x anterior estava na faixa de x que a plataforma ocupa:
            if plataforma.x - bola.width < xbolaant < plataforma.x + plataforma.width:
                # permitir pulo somente em colisão de cima para baixo
                if plataforma.y + plataforma.height > ybolaant:
                    podepular = True
                    pulou = False
                    podedarsegundopulo = False

                # dar um passo atrás na direção y
                bola.y -= velbolay * deltat
                velbolay = - velbolay / amortecimentocolisao
                bola.y += velbolay * deltat

            # se o y anterior da bola estava na faixa de ys que a plataforma ocupa:
            if plataforma.y - bola.height < ybolaant < plataforma.y + plataforma.height:
                # dar um passo atrás na direção x
                bola.x = xbolaant
                velbolax = - velbolax / amortecimentocolisao
                bola.x += velbolax * deltat





def colisaocomseta():
    global bola, vetsetacima, velbolay, velbolax, acseta, vetsetadir, vetsetabaixo, vetsetaesq
    for seta in vetsetacima:
        if bola.collided(seta):
            velbolay -= acseta
    for seta in vetsetabaixo:
        if bola.collided(seta):
            velbolay += acseta
    for seta in vetsetaesq:
        if bola.collided(seta):
            velbolax -= acseta
    for seta in vetsetadir:
        if bola.collided(seta):
            velbolax += acseta



# Desenho
def desenhar():
    global janela, vetplat, vetplatchao, tempo, vetsetacima, vetsetabaixo, vetsetadir, vetsetaesq
    global vetinimigos, vetrastro, vetplatmovel
    fundo.draw()
    for plataforma in vetplatchao:
        plataforma.draw()
    for plataforma in vetplat:
        plataforma.draw()
    for pltm in vetplatmovel:
        pltm.draw()
    for seta in vetsetacima:
        seta.draw()
    for seta in vetsetadir:
        seta.draw()
    for seta in vetsetabaixo:
        seta.draw()
    for seta in vetsetaesq:
        seta.draw()
    for inimigo in vetinimigos:
        inimigo.draw()
    for rastro in vetrastro:
        rastro.draw()
    bola.draw()
    portal.draw()