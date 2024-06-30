from tkinter import *
from PIL import Image, ImageTk
import config

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title(f'{config.NAME} skils --ДЛЯ ПРОДОЛЖЕНИЯ ЗАКРОЙТЕ ЭТО ОКНО--')
        self.root.geometry('500x550')
        self.root.config(bg = 'gray12')
        self.root.resizable(0, 0)
        try: self.root.iconbitmap(config.win_icon)
        except: pass
        
        self.skils_image = Image.open('assets\\images\\yragan_skils.png')
        self.skils_image = self.skils_image.resize((500, 550))
        self.skils_image_tk = ImageTk.PhotoImage(self.skils_image)
        
        lbl = Label(self.root, image=self.skils_image_tk, bd=0)
        lbl.place(x=0)
        
        self.root.mainloop()
        
if __name__ == '__main__':
    App()
    