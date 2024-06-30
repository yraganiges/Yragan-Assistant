#-1
import YraganVoice as yv
import speech_recognition as sr
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import tkinter.ttk as ttk
from threading import Thread as th 
import pygame, time, random #modules
import config #files

class App:
    def __init__(self):
        #variables
        self.root = Tk()
        self.root.title(config.win_title)
        self.root.geometry(config.win_size)
        self.root['bg'] = config.win_bg
        self.root.resizable(0, 0)
        try: self.root.iconbitmap(config.win_icon)
        except: pass 
        
        #Text-Welcome
        txt_welcome = Label(self.root, text = 'The final steps...', bg = config.win_bg, fg = 'white', font = (config.default_font, 20))
        txt_welcome.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        
        #Choice-country
        choice_country = Combobox(font = ('Bahnschrift SemiBold', 12), width = 30, justify = CENTER, foreground = 'red')
        choice_country['values'] = ('Choice-country...', 'Russia-ru', 'Ukraine-ua', 'USA/British-en', 'Espanol-es', 
                                    'China-zh', 'Italy(OsmanyDauni)-it')
        choice_country.current(0)
        choice_country.place(relx = 0.5, rely = 0.2, anchor = CENTER)
        
        #font: Bauhaus 93
        
        #Choice mode VoiceActing
        choice_mode_VoiceActing = Combobox(font = ('Bahnschrift SemiBold', 12), width = 30, justify = CENTER, foreground = 'red')
        choice_mode_VoiceActing['values'] = ('Choice mode-VoiceActing...', '_(Recommend)_ Voice-Bot', 'Voice-Artem', 'Voice-Daima')
        choice_mode_VoiceActing.current(0)
        choice_mode_VoiceActing.place(relx = 0.5, rely = 0.3, anchor = CENTER)
        
        #Style-Combobox
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", foreground="red", background = 'gray')
        
        self.root.mainloop()
        
    # def Record
        
if __name__ == '__main__':
    App()