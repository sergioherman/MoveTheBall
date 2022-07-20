from Modulos.Funcoes import *
# from Modulos.Fase01 import *


janela = Window(1320, 660)
mouse = Window.get_mouse()
cursor = mouse.get_position()

numdafase = 1
maxfasedesbloq = 6

clicouNovoJogo = False
clicouCarregarJogo = False
clicouSairJogo = False


backgroundMenuInicial = GameImage("../Imagens/MenuInicial/CenarioMenuInicial3.png")

txtBtNovoJogo = GameImage("../Imagens/MenuInicial/Jogar.png")
fundoPretoBtNovoJogo = GameImage("../Imagens/MenuInicial/Fundo2BotoesMenuIniciar.png")
fundoDestaqueBtNovoJogo = GameImage("../Imagens/MenuInicial/Fundo5BotoesMenuIniciar.png")
txtBtNovoJogo.x = 19*janela.width/20 - txtBtNovoJogo.width
fundoPretoBtNovoJogo.x = 19*janela.width/20 - fundoPretoBtNovoJogo.width
fundoDestaqueBtNovoJogo.x = 19 * janela.width / 20 - fundoDestaqueBtNovoJogo.width
txtBtNovoJogo.y = 19*janela.height/20 - 3 * txtBtNovoJogo.height
fundoPretoBtNovoJogo.y = 19*janela.height/20 - 3 * fundoPretoBtNovoJogo.height
fundoDestaqueBtNovoJogo.y = 19 * janela.height / 20 - 3 * fundoDestaqueBtNovoJogo.height

txtBtCarregarJogo = GameImage("../Imagens/MenuInicial/SelecionarFase.png")
fundoPretoBtCarregarJogo = GameImage("../Imagens/MenuInicial/Fundo3BotoesMenuIniciar.png")
fundoDestaqueBtCarregarJogo = GameImage("../Imagens/MenuInicial/Fundo5BotoesMenuIniciar.png")
txtBtCarregarJogo.x = 19*janela.width/20 - txtBtCarregarJogo.width
fundoPretoBtCarregarJogo.x = 19*janela.width/20 - fundoPretoBtCarregarJogo.width
fundoDestaqueBtCarregarJogo.x = 19 * janela.width / 20 - fundoDestaqueBtCarregarJogo.width
txtBtCarregarJogo.y = 19*janela.height/20 - 2 * txtBtCarregarJogo.height
fundoPretoBtCarregarJogo.y = 19*janela.height/20 - 2 * fundoPretoBtCarregarJogo.height
fundoDestaqueBtCarregarJogo.y = 19 * janela.height / 20 - 2 * fundoDestaqueBtCarregarJogo.height

txtBtSairJogo = GameImage("../Imagens/MenuInicial/SairBotoesMenuIniciar.png")
fundoPretoBtSairJogo = GameImage("../Imagens/MenuInicial/Fundo4BotoesMenuIniciar.png")
fundoDestaqueBtSairJogo = GameImage("../Imagens/MenuInicial/Fundo5BotoesMenuIniciar.png")
txtBtSairJogo.x = 19*janela.width/20 - txtBtSairJogo.width
fundoPretoBtSairJogo.x = 19*janela.width/20 - fundoPretoBtSairJogo.width
fundoDestaqueBtSairJogo.x = 19 * janela.width / 20 - fundoDestaqueBtSairJogo.width
txtBtSairJogo.y = 19*janela.height/20 - 1.0 * txtBtSairJogo.height
fundoPretoBtSairJogo.y = 19*janela.height/20 - 1.0 * fundoPretoBtSairJogo.height
fundoDestaqueBtSairJogo.y = 19 * janela.height / 20 - 1.0 * fundoDestaqueBtSairJogo.height

txtBtNovoJogo.image.set_alpha(100)
txtBtCarregarJogo.image.set_alpha(100)
txtBtSairJogo.image.set_alpha(100)

dentroBtNovoJogo = False
if fundoPretoBtNovoJogo.x < cursor[0] < fundoPretoBtNovoJogo.x + fundoPretoBtNovoJogo.width and fundoPretoBtNovoJogo.y < \
        cursor[1] < fundoPretoBtNovoJogo.y + fundoPretoBtNovoJogo.height:
    dentroBtNovoJogo = True

dentroBtCarregarJogo = False
if fundoPretoBtCarregarJogo.x < cursor[0] < fundoPretoBtCarregarJogo.x + fundoPretoBtCarregarJogo.width and fundoPretoBtCarregarJogo.y < \
        cursor[1] < fundoPretoBtCarregarJogo.y + fundoPretoBtCarregarJogo.height:
    dentroBtCarregarJogo = True

dentroBtSairJogo = False
if fundoPretoBtSairJogo.x < cursor[0] < fundoPretoBtSairJogo.x + fundoPretoBtSairJogo.width and fundoPretoBtSairJogo.y < \
        cursor[1] < fundoPretoBtSairJogo.y + fundoPretoBtSairJogo.height:
    dentroBtSairJogo = True

while True:
    cursor = mouse.get_position()

    if fundoPretoBtNovoJogo.x < cursor[0] < fundoPretoBtNovoJogo.x + fundoPretoBtNovoJogo.width and fundoPretoBtNovoJogo.y < \
            cursor[1] < fundoPretoBtNovoJogo.y + fundoPretoBtNovoJogo.height:
        if not dentroBtNovoJogo:
            dentroBtNovoJogo = True
            txtBtNovoJogo.image.set_alpha(255)
    else:
        if dentroBtNovoJogo:
            dentroBtNovoJogo = False
            txtBtNovoJogo.image.set_alpha(100)

    if fundoPretoBtCarregarJogo.x < \
            cursor[0] < fundoPretoBtCarregarJogo.x + fundoPretoBtCarregarJogo.width and fundoPretoBtCarregarJogo.y < \
            cursor[1] < fundoPretoBtCarregarJogo.y + fundoPretoBtCarregarJogo.height:
        if not dentroBtCarregarJogo:
            dentroBtCarregarJogo = True
            txtBtCarregarJogo.image.set_alpha(255)
    else:
        if dentroBtCarregarJogo:
            dentroBtCarregarJogo = False
            txtBtCarregarJogo.image.set_alpha(100)

    if fundoPretoBtSairJogo.x < cursor[0] < fundoPretoBtSairJogo.x + fundoPretoBtSairJogo.width and fundoPretoBtSairJogo.y < \
            cursor[1] < fundoPretoBtSairJogo.y + fundoPretoBtSairJogo.height:
        if not dentroBtSairJogo:
            dentroBtSairJogo = True
            txtBtSairJogo.image.set_alpha(255)
    else:
        if dentroBtSairJogo:
            dentroBtSairJogo = False
            txtBtSairJogo.image.set_alpha(100)

    if dentroBtNovoJogo and mouse.is_button_pressed(BUTTON_LEFT):
        clicouNovoJogo = True
    else:
        if clicouNovoJogo and dentroBtNovoJogo:
            print("Novo Jogo")
            numdafase = escolherfase(numdafase)
        clicouNovoJogo = False

    if dentroBtCarregarJogo and mouse.is_button_pressed(BUTTON_LEFT):
        clicouCarregarJogo = True
    else:
        if clicouCarregarJogo and dentroBtCarregarJogo:
            print("Carregar Jogo")
            numdafase = telaselecaofases(maxfasedesbloq)
            numdafase = escolherfase(numdafase)
        clicouCarregarJogo = False

    if dentroBtSairJogo and mouse.is_button_pressed(BUTTON_LEFT):
        clicouSairJogo = True
    else:
        if clicouSairJogo and dentroBtSairJogo:
            print("Sair")
            janela.close()
        clicouSairJogo = False

    backgroundMenuInicial.draw()

    if dentroBtNovoJogo:
        fundoDestaqueBtNovoJogo.draw()
    fundoPretoBtNovoJogo.draw()
    txtBtNovoJogo.draw()

    if dentroBtCarregarJogo:
        fundoDestaqueBtCarregarJogo.draw()
    fundoPretoBtCarregarJogo.draw()
    txtBtCarregarJogo.draw()

    if dentroBtSairJogo:
        fundoDestaqueBtSairJogo.draw()
    fundoPretoBtSairJogo.draw()
    txtBtSairJogo.draw()

    if numdafase > maxfasedesbloq:
        maxfasedesbloq = numdafase
    # janela.draw_text(str(maxfasedesbloq),20,10,30,(255,255,255),"Calibri",True)
    janela.update()
