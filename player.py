from tkinter import *
from tkinter import messagebox as msg
from threading import Thread as th
import config, YraganVoice as yv, assistant_module as am
import os, pygame, subprocess, pydub as pd, pyttsx3 as tts, pyperclip
from PIL import Image, ImageTk

class App:
    def __init__(self):
        #window
        self.root = Tk()
        self.root.title(config.win_title)
        self.root.geometry('700x800')
        self.root['bg'] = config.win_bg
        self.root.resizable(1, 1)
        try: self.root.iconbitmap(config.win_icon)
        except: pass
        
        #variables
        self.txt_req = None
        self.player_status: str = None
        
        #objects
        self.engine = tts.init()
        self.sound = pygame.mixer
        self.sound.init()
        
        #Background
        try:
            self.skils_image = Image.open('assets\\images\\background_3.png')
            self.skils_image = self.skils_image.resize((700, 800)) #TODO: 
            self.skils_image_tk = ImageTk.PhotoImage(self.skils_image) 
            
            self.background = Label(self.root, image=self.skils_image_tk, bd=0)
            self.background.place(x = 0)
        except: pass 
        
        #layout
        field = Label(self.root, width = 500, height = 5, bg = 'gray8')
        field.place(x = 0, y = -20)
        
        field = Label(self.root, width = 500, height = 5, bg = 'gray10')
        field.place(relx = 0.1, rely = 0.95, anchor = CENTER)
        
        self.txt = Label(self.root, text = 'List-requests', bg = 'gray8', fg='white',  font=('Futura-Medium', 20))
        self.txt.place(x = 10, y = 10)
        
        #player-button
        self.btn_player = Button(self.root, width = 9, height = 4, bd = 0,  bg = 'gray20', fg = 'red', text = '🔴')
        self.btn_player.place(relx = 0.5, rely = 0.95, anchor = CENTER)
        
        #player
        def open_text_window(file_path: str):
            win_txt = Tk()
            win_txt.title(config.win_title)
            win_txt.geometry(f'{config.num_for_indentation * 10 ** 2 - 100}x{config.max_limit_lenght_request - 100}')
            win_txt['bg'] = config.win_bg
            win_txt.resizable(1, 1)
            try: win_txt.iconbitmap(config.win_icon)
            except: pass
            
            with open(file_path, 'r') as file:
                txt = Label(win_txt, text = am.Request().Processing_indentation(text = file.read(), num_for_indentation = config.num_for_indentation), bg = config.win_bg, fg = 'white', font = (config.default_font, 12), justify = LEFT)
                txt.grid()
                txt.bind('<Button - 1>', lambda event: pyperclip.copy(event.widget['text']))
                txt.bind('<Enter>', lambda event: event.widget.configure(fg = config.pre_default_bg))
                txt.bind('<Leave>', lambda event: event.widget.configure(fg = 'white'))
            
        def voiceActing_text(text):
            if config.VoiceActing_mode.lower() == 'bot':
                try:
                    self.engine.say(text)
                    self.engine.runAndWait()
                except:
                    msg.showerror('Error!', 'Bot cant voice-acting text')
                    
            elif config.VoiceActing_mode.lower() == 'artem':
                yv.ArtemVoice(text)
            elif config.VoiceActing_mode.lower() == 'daima':
                yv.DaimaVoice(text)
        
        def stoping_player(): self.sound.music.stop()
        def pause_player(): self.sound.music.pause()
        def unpause_player(): self.sound.music.unpause()
        
        #Add files 
        def list_request():
            y = 70
            count = 0

            for file in os.listdir(config.path_requests):
                print('>>', file)
                if file.endswith('.mp3') and count <= 40:
                    self.txt_req = Label(self.root, text=file[0:len(file) - 4], bg=config.win_bg, fg='white', font=(config.default_font, 12))
                    self.txt_req.place(x=10, y=y)
                    self.txt_req.bind('<Enter>', lambda event: event.widget.configure(fg = 'red', bg = 'gray22'))
                    self.txt_req.bind('<Leave>', lambda event: event.widget.configure(fg = 'white', bg = config.win_bg))
                    self.txt_req.bind('<Button - 1>', lambda event: open_text_window(file_path = f'data\\user_data\\requests\\{event.widget["text"]}.txt'))
                    
                    #convert files, to hes must playing in player
                    try:
                        audio = pd.AudioSegment.from_file(f'{config.path_requests}\\{file}', format = 'mp3')
                        audio.export(f'{config.path_requests}\\{file}', format="mp3")
                    except: pass

                    y += 23
                    count += 1

        #Run-functions
        th(daemon = True, target = list_request).start()
        
        self.root.mainloop()

if __name__ == '__main__':
    App()
    