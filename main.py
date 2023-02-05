from tkinter import *
from dictionary import compound_finals_and_nasal_finals
import pygame
import threading
import pyaudio
import wave




root =  Tk()
root.geometry('1200x800')
root.config(bg='grey')

frame = Frame(root, bg='#ccffcc')
frame.grid()

pygame.mixer.init()

def play(args):
    
    print(args)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.load(f'audio/{args}.mp3') 
    pygame.mixer.music.play(loops=0)

main_one = LabelFrame(frame,  text='Simple Finals', bd=5, relief=RIDGE)
main_one.grid(pady=5, row=0, column=0, padx=10)

a = Button(main_one , text="a", padx=10, pady=10, command=lambda: play("a")).grid(padx=10, pady=10, row=0, column=0)
o = Button(main_one , text="o", padx=10, pady=10, command=lambda: play("o")).grid(padx=10, pady=10, row=0, column=1)
e = Button(main_one , text="e", padx=10, pady=10,command=lambda: play("e")).grid(padx=10, pady=10, row=0, column=2)
i = Button(main_one , text="i\n(yi)", padx=10, pady=10,command=lambda: play("i")).grid(padx=10, pady=10, row=0, column=3)
u = Button(main_one , text="u\n(wu)", padx=10, pady=10,command=lambda: play("u")).grid(padx=10, pady=10, row=0, column=4)
ü = Button(main_one , text="ü\n(yu)", padx=10, pady=10,command=lambda: play("ü")).grid(padx=10, pady=10, row=0, column=5)

initials = LabelFrame(frame,  text='21 Pinyin Initials', bd=5, relief=RIDGE)
initials.grid(pady=5, row=1, column=0)

b = Button(initials , text="b", padx=10, pady=10, command=lambda: play("b")).grid(padx=10, pady=10, row=0, column=0)
p = Button(initials , text="p", padx=10, pady=10, command=lambda: play("p")).grid(padx=10, pady=10, row=0, column=1)
m = Button(initials , text="m", padx=10, pady=10,command=lambda: play("m")).grid(padx=10, pady=10, row=0, column=2)
f = Button(initials , text="f", padx=10, pady=10,command=lambda: play("f")).grid(padx=10, pady=10, row=0, column=3)
d = Button(initials, text="d", padx=10, pady=10,command=lambda: play("d")).grid(padx=10, pady=10, row=1, column=0)
t = Button(initials , text="t", padx=10, pady=10,command=lambda: play("t")).grid(padx=10, pady=10, row=1, column=1)
n_initial = Button(initials , text="n", padx=10, pady=10, command=lambda: play("n_initial")).grid(padx=10, pady=10, row=1, column=2)
l = Button(initials , text="l", padx=10, pady=10, command=lambda: play("l")).grid(padx=10, pady=10, row=1, column=3)
g = Button(initials , text="g", padx=10, pady=10,command=lambda: play("g")).grid(padx=10, pady=10, row=2, column=0)
k = Button(initials , text="k", padx=10, pady=10,command=lambda: play("k")).grid(padx=10, pady=10, row=2, column=1)
h = Button(initials, text="h", padx=10, pady=10,command=lambda: play("h")).grid(padx=10, pady=10, row=2, column=3)
j = Button(initials , text="j", padx=10, pady=10,command=lambda: play("j")).grid(padx=10, pady=10, row=3, column=0)
q = Button(initials , text="q", padx=10, pady=10, command=lambda: play("q")).grid(padx=10, pady=10, row=3, column=1)
x = Button(initials , text="x", padx=10, pady=10, command=lambda: play("x")).grid(padx=10, pady=10, row=3, column=3)
z = Button(initials , text="z\n(zi)", padx=10, pady=10,command=lambda: play("z")).grid(padx=10, pady=10, row=4, column=0)
c = Button(initials , text="c\n(ci)", padx=10, pady=10,command=lambda: play("c")).grid(padx=10, pady=10, row=4, column=1)
S = Button(initials, text="s\n(si)", padx=10, pady=10,command=lambda: play("s")).grid(padx=10, pady=10, row=4, column=3)
zh = Button(initials , text="zh\n(zhi)", padx=10, pady=10,command=lambda: play("zh")).grid(padx=10, pady=10, row=5, column=0)
ch= Button(initials , text="ch\n(chi)", padx=10, pady=10,command=lambda: play("ch")).grid(padx=10, pady=10, row=5, column=1)
sh= Button(initials, text="sh\n(shi)", padx=10, pady=10,command=lambda: play("sh")).grid(padx=10, pady=10, row=5, column=3)
r= Button(initials , text="r\n(ri)", padx=10, pady=10,command=lambda: play("r")).grid(padx=10, pady=10, row=5, column=4)

initials = LabelFrame(frame,  text='Compound Finals and Nasal Finals Groups 1 & 2', bd=5, relief=RIDGE)
initials.grid(pady=5, row=0, column=1)

ai = Button(initials , text="ai", padx=10, pady=10, command=lambda: play("ai")).grid(padx=10, pady=10, row=0, column=0)
ei = Button(initials , text="ei", padx=10, pady=10, command=lambda: play("ei")).grid(padx=10, pady=10, row=1, column=0)
ao = Button(initials , text="ao", padx=10, pady=10,command=lambda: play("ao")).grid(padx=10, pady=10, row=2, column=0)
ou = Button(initials , text="ou", padx=10, pady=10,command=lambda: play("ou")).grid(padx=10, pady=10, row=3, column=0)
an = Button(initials, text="an", padx=10, pady=10,command=lambda: play("an")).grid(padx=10, pady=10, row=0, column=2)
en = Button(initials , text="en", padx=10, pady=10,command=lambda: play("en")).grid(padx=10, pady=10, row=0, column=3)
ang = Button(initials , text="ang", padx=10, pady=10, command=lambda: play("ang")).grid(padx=10, pady=10, row=1, column=2)
eng = Button(initials , text="eng", padx=10, pady=10, command=lambda: play("eng")).grid(padx=10, pady=10, row=1, column=3)
ong = Button(initials , text="ong\n(weng)", padx=10, pady=10,command=lambda: play("ong")).grid(padx=10, pady=10, row=2, column=2)

main = LabelFrame(frame,  text='Compound Finals and Nasal Finals Groups 3 & 4', bd=5, relief=RIDGE)
main.grid(pady=5,row=1, column=1)

ia = Button(main , text="ia\n(ya)", padx=10, pady=10, command=lambda: play("ia")).grid(padx=10, pady=10, row=0, column=0)
ian = Button(main , text="ian\n(yan)", padx=10, pady=10, command=lambda: play("ian")).grid(padx=10, pady=10, row=1, column=2)
iang = Button(main , text="iang\n(yang)", padx=10, pady=10,command=lambda: play("iang")).grid(padx=10, pady=10, row=1, column=3)
iao = Button(main , text="iao\n(yao)", padx=10, pady=10,command=lambda: play("iao")).grid(padx=10, pady=10, row=0, column=2)
ie = Button(main , text="ie\n(ye)", padx=10, pady=10,command=lambda: play("ie")).grid(padx=10, pady=10, row=0, column=1)
in_ = Button(main , text="in\n(yin)", padx=10, pady=10,command=lambda: play("in")).grid(padx=10, pady=10, row=1, column=0)
ing = Button(main , text="ing\n(ying)", padx=10, pady=10,command=lambda: play("ing")).grid(padx=10, pady=10, row=1, column=1)
iong = Button(main , text="iong\n(yong)", padx=10, pady=10,command=lambda: play("iong")).grid(padx=10, pady=10, row=1, column=4)
iu_iou = Button(main , text="iu\n(iou)\n(you)", padx=10, pady=2,command=lambda: play("iu(iou)")).grid(padx=10, pady=10, row=0, column=3)
#n = Button(main , text="n", padx=10, pady=10,command=lambda: play("n")).grid(padx=10, pady=10, row=0, column=9)
#ng = Button(main , text="ng", padx=10, pady=10,command=lambda: play("ng")).grid(padx=10, pady=10, row=0, column=10)


üe = Button(main , text="üe\n(ue)\n(yue)", padx=10, pady=2,command=lambda: play("üe(ue)")).grid(padx=10, pady=10, row=2, column=0)
üan = Button(main , text="üan\n(uan)\n(yuan)", padx=10, pady=2,command=lambda: play("üan(uan)")).grid(padx=10, pady=10, row=2, column=1)
ün = Button(main , text="ün\n(un)\n(yun)", padx=10, pady=2,command=lambda: play("ün(un)")).grid(padx=10, pady=10, row=2, column=2)
rule = Label(main, text="Drop the dots when writing or typing 'J', 'Q' or 'X'").grid(padx=10, pady=10, row=3, column=0, columnspan=5)

main = LabelFrame(frame,  text='Compound Finals and Nasal Finals Groups 5 & 6', bd=5, relief=RIDGE)
main.grid(pady=5, row=0, column=2, padx=10)

ua = Button(main , text="ua\n(wa)", padx=10, pady=10, command=lambda: play("ua")).grid(padx=10, pady=10, row=0, column=0)
uo = Button(main , text="uo\n(wo)", padx=10, pady=10, command=lambda: play("uo")).grid(padx=10, pady=10, row=0, column=1)
uai = Button(main , text="uai\n(wai)", padx=10, pady=10,command=lambda: play("uai")).grid(padx=10, pady=10, row=1, column=0)
ui = Button(main , text="ui\n(wei)", padx=10, pady=10,command=lambda: play("ui")).grid(padx=10, pady=10, row=1, column=1)
uan = Button(main , text="uan\n(wan)", padx=10, pady=10,command=lambda: play("uan")).grid(padx=10, pady=10, row=2, column=0)
uang = Button(main , text="uang\n(wang)", padx=10, pady=10,command=lambda: play("uang")).grid(padx=10, pady=10, row=2, column=1)
un = Button(main , text="un(uen)\n(wen)", padx=10, pady=10,command=lambda: play("un(uen)")).grid(padx=10, pady=10, row=3, column=0)
ueng = Button(main , text="ueng\n(weng)", padx=10, pady=10,command=lambda: play("ueng")).grid(padx=10, pady=10, row=3, column=1)
er = Button(main , text="er", padx=10, pady=10,command=lambda: play("er")).grid(padx=10, pady=10, row=0, column=3)

audio_frame = LabelFrame(frame, text='Voice Recorder', bd=5, relief=RIDGE)
audio_frame.grid(row=1, column=2)

###audio player

chunk = 1024 
sample_format = pyaudio.paInt16 
channels = 2
fs = 44100  

frames = [] 

isrecording = False

def startrecording():
    global frames, stream, isrecording, sample_format, p
    frames = [] 
    p = pyaudio.PyAudio()  
    stream = p.open(format=sample_format,channels=channels,rate=fs,frames_per_buffer=chunk,input=True)
    isrecording = True
    
    print('Recording')
    t = threading.Thread(target=record)
    t.start()

def stoprecording():
    global isrecording
    isrecording = False
    print('recording complete')
    filename='attempt'
    filename = filename+".wav"
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    # main.destroy()
        

    

def record():
    while isrecording:
        data = stream.read(chunk)
        frames.append(data)


def playrecording():
    pygame.mixer.music.set_volume(.8)
    pygame.mixer.music.load('attempt.wav')
    pygame.mixer.music.play(loops=0)



button1 = Button(audio_frame, text='rec',command=startrecording)
button2 = Button(audio_frame, text='stop',command=stoprecording)
button3 = Button(audio_frame, text='play',command=playrecording)
button1.grid(row=0, column=0, padx=5, pady=8)
button2.grid(row=0, column=1, padx=5, pady=8)
button3.grid(row=0, column=2, padx=5, pady=8)

root.mainloop()