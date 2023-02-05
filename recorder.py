import tkinter as tk
import threading
import pyaudio
import wave
import pygame
import os

pygame.mixer.init()

class App():
    chunk = 1024 
    sample_format = pyaudio.paInt16 
    channels = 2
    fs = 44100  
    
    frames = []  
    def __init__(self, master):
        self.isrecording = False
        self.button1 = tk.Button(main, text='rec',command=self.startrecording)
        self.button2 = tk.Button(main, text='stop',command=self.stoprecording)
        
      
        self.button1.pack()
        self.button2.pack()
       
    

    def startrecording(self):
        self.frames = [] 
        self.p = pyaudio.PyAudio()  
        self.stream = self.p.open(format=self.sample_format,channels=self.channels,rate=self.fs,frames_per_buffer=self.chunk,input=True)
        self.isrecording = True
        
        print('Recording')
        t = threading.Thread(target=self.record)
        t.start()

    def stoprecording(self):
        self.isrecording = False
        print('recording complete')
        self.filename='attempt'
        self.filename = self.filename+".wav"
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        # main.destroy()
        

    

    def record(self):
        
        while self.isrecording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)
		

main = tk.Tk()
main.title('recorder')
main.geometry('200x100')
app = App(main)


def playrecording():
        pygame.mixer.music.set_volume(.6)
        pygame.mixer.music.load('attempt.wav')
        pygame.mixer.music.play(loops=0)

        # filename = 'attempt.wav'

        # # Defines a chunk size of 1024 samples per data frame.
        # chunk = 1024  

        # # Open sound file  in read binary form.
        # file = wave.open(filename, 'rb')

        # # Initialize PyAudio
        # p = pyaudio.PyAudio()

        # # Creates a Stream to which the wav file is written to.
        # # Setting output to "True" makes the sound be "played" rather than recorded
        # stream = p.open(format = p.get_format_from_width(file.getsampwidth()),
        #                 channels = file.getnchannels(),
        #                 rate = file.getframerate(),
        #                 output = True)

        # # Read data in chunks
        # data = file.readframes(chunk)

        # # Play the sound by writing the audio data to the stream
        # while data != '':
        #     stream.write(data)
        #     data = file.readframes(chunk)

        # # Stop, Close and terminate the stream
        # stream.stop_stream()
        # stream.close()
        # p.terminate()

button3 = tk.Button(main, text='play',command=playrecording)
button3.pack()

main.mainloop()