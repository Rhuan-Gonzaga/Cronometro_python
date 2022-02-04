
from glob import glob
from tkinter import *

#CORES
cor1 = "#0a0a0a" #preta 
cor2 = "#fafcff" #branca
cor3 = "#21c25c" #verde
cor4 = "#eb463b" #vermelha
cor5 = "#dedcdc" #cinza
cor6 = "#3080f0" #azul



#FUNÇOES DOS BOTOES
global tempo
global rodar
global contador 
global limitador 

limitador = 59

tempo = "00:00:00"
rodar = False
contador = -5

#FUNCAO INICIAR
def iniciar():
    global tempo
    global contador
    global rodar 
    global limitador 
    

    if rodar:
        #ANTES DO CRONOMETRO COMEÇAR
        if contador <= -1:
            inicio = "Começando em " + str(contador)
            label_tempo["text"] = inicio
            label_tempo["font"] = "Arial 10"
        
        #RODANDO O CRONOMETRO
        else:
            label_tempo["font"] = "Times 50 bold"
            temporario = str(tempo)
            h,m,s = map(int,temporario.split(":"))
            h = int(h)
            m = int(m)
            s = int(contador)

            if s >= limitador:
               contador = 0
               m =+ 1
            
            s = str(0)+str(s)
            m = str(0)+str(m)
            h = str(0)+str(h)

            #ATUALIZANDO OS VALORES ATUAIS
            temporario = str(h[-2:]) + ":" + str(m[-2:]) + ":" + str(s[-2:])
            label_tempo["text"] = temporario
            tempo = temporario

        label_tempo.after(1000, iniciar)
        contador += 1 

#FUNCAO START
def start():
    global rodar
    rodar = True
    iniciar()

#FUNCAO PAUSAR
def pausar():
    global rodar
    rodar = False

#FUNCAO REINIICAR
def reiniciar():
    global contador
    global tempo

    #REINICIANDO O TEMPO E CONTADOR
    contador = 0 
    tempo = "00:00:00"
    label_tempo["text"] = tempo
    pausar()

#CONFIGURANDO A JANELA
janela = Tk()
janela.title("Cronômetro")
janela.geometry("300x180")
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)

#CRIANDO O LABEL TEMPO
label_tempo = Label(janela,text=tempo,fon=("Times 50 bold"),bg=cor1,fg=cor3)
label_tempo.place(x=20,y=30)

#CRIANDO BOTOES
botao_iniciar = Button(janela,command=start,text="Iniciar",fon=("Ivy 8 bold"),bg=cor1,fg=cor2,width=10,height=2,relief="raised",overrelief="ridge")
botao_iniciar.place(x=18,y=125)

botao_pausar = Button(janela,command=pausar,text="Pausar",fon=("Ivy 8 bold"),bg=cor1,fg=cor2,width=10,height=2,relief="raised",overrelief="ridge")
botao_pausar.place(x=113,y=125)

botao_reiniciar = Button(janela,command=reiniciar,text="Reiniciar",fon=("Ivy 8 bold"),bg=cor1,fg=cor2,width=10,height=2,relief="raised",overrelief="ridge")
botao_reiniciar.place(x=207,y=125)



janela.mainloop()


