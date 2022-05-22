#Assistente virtual com interface gráfica Python (Glauber)

# Our main file.

from tkinter import

def ia():

 import speech_recognition as sr
 import sounddevice as sd
 import wavio as wv
 import pyttsx3
 import webbrowser
 import random
 import os
 import time
 //
    import datetime
    import speech_recognition as sr
    import sounddevice as sd
    import wavio as wv
    import wikipedia
    import webbrowser
    import random
    from gtts import gTTS
    from playsound import playsound
    import pywhatkit
    import bs4
    import requests
    import joblib


 def iafala(fala):
    engine = pyttsx3.init()
    engine.say(fala)
    engine.runAndWait()
    iafala('olá a todos!')


 def grava():
    freq = 48000 
    Duração = 5
    gravacao = sd.rec(int(duration *freq)),
                     samplerate=freq, channels=2)
    print('fale!')
    sd.wait()
    wv.write('minhavoz.wav', gravacao, freq, sampleidth=2)
    print('ok, processaando...')

 While True:
   def pesquisaggl():
       frase = fala
       search = frase.replace('pesquisar', '' )
       search2 = search.replace('pesquisar', '')
       webbrowser.open('https://www.google.com/search?q={search2}')
    grava()
    r = sr.Recognizer
    filename = 'minhavoz.wav'
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        texto = r.recognize_google(audio_data, language='pt-br')
        print('Você disse:' + texto)
    fala = texto

    if fala == 'bom dia':
        iafala('bom dia para você')
        elif fala == 'Boa noite':
            iafala ('Boa noite para você!')

        word = 'pesquisar'
        word4 = 'Pesquisar'
        word2 = 'Abrir google'
        word5 = 'abrir google'
        word6 = 'liga o google'
        word3 = 'Liga o google'

        if word or word2 in fala:
            pesquisaggl()

        if fala == 'Youtube':
            webbrowser.open('https://youtube.com/')
        elif fala == 'WhatsApp':
            webbrowser.open('https:web.whatsapp.com/')

        if fala == 'Abrir Google' or fala == 'google':
        

    global nome, link

    lista1 = ['de nada', 'por nada', 'a seu dispor', 'até logo']
    lista1 = random.choice(lista1)

    meusites = [['whatsapp', 'https://whatsapp.com/'], ['youtube', 'https://youtube.com/'], ['instagram', 'https://instagram.com/']]

    filename = 'minhavoz.wav'
    falala = 'falala.mp3'

    global says

    def fala(text):
        tts = gTTS(text, 'lang-pt-br')
        tts.save('falala.mp3')
        tts.save('falala.mp3')
    playsound('falala.mp3')

    def grava():
        freq = 48000  # Altere a frequência se achar necessário
        duration = 5  # Altere a duração de cada gravação
        recording = sd.rec(int(duration * freq),
                        samplerate=freq, channels=2)
            print('Fale agora!')
        sd.wait()
        wv.write("minhavoz.wav", recording, freq, sampwidth=2)
        print('Ok! Processando')

    def addsite():
        snone = input('Qual o nome do site?')
        slink = input('Qual link do site?')
        listabase = [snone, slink]
        meusite.append(listabase)
    while True:
    grava()

    r = sr.Recognizer
    try:
        with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        says = r.recognize_google(audio_data, language='pt-BR')
        print('você disse: ' + says.lower())
        texto = says.lower()

        f = open('shutdown.txt', 'r')
        fec = f.read()
        if texto in fec
        fala ('ok, desligando...')
        janela.destroy()
        break

    elif 'horas' in texto or 'hora' in texto:

        hora = datatime.datatime.now(). strftime('%H:%H')
        fala('Agora são' + hora)

        elif 'procurar por' in texto:

            procurar = texto.replace('procurar por', '')
            wikipedia.set_lang('pt')
            resultado: wikipedia.summary(procurar, 2)
            fala(resultado)

        elif 'toque' in texto or 'tocar' in texto:

            tocar = texto.replace('toque, '')
            toque = 'texto.replace('tocar', '')
            fala('OK, tocando música!')
            resultado = pywhatkit.playonyt(toque)

        elif 'abrir site' in texto:
            site = texto.replace('abrir site', '')
            mysite = joblib.load('meusite..obj')

            for i in mysites:
                if i[0] in site:
                    webnrowser.open(i[1])

        elif 'adicionar site' in texto:

            addsite()
            joblib.dump(meusites, 'meusite..obj')

        elif 'valor hoje' in texto:
            coin = texto.replace('valor hoje', '')
            get_price_crypto(coin)

        elif 'bom dia' in texto:
            fala ('bom dia!')
        elif 'boa tarde!' in texto
        fala ('boa tarde!') 
        elif 'boa noite!' in texto
        fala ('boa noite!')
    except:
        print('ocorreu algum erro, tente novamente.')

def Assistente Virtual ():

 janela = Tk()
 janela.iconbitmap("favicon.ico")
 janela.title('Assistente Virtual em python - Dev')

 label_l = Label(janela, text='Assistente Virtual Python', font='Arial 35')
 label_l.place(x=200, y=200)

 label2_l + Label(janela, text='By Kaue caires, Font='Calibri 10' , )

 botao_l = Button(janela, height=4, width=67, text=)

 janela.geometry('890x500+0+0')
 janela.mainloop()
