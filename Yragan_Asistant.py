from threading import Thread as th
from tkinter import *
from PIL import Image, ImageTk
import config, main, window_skils, time
        
def main_func():
    window_skils.App()
    main.App()

if __name__ == '__main__':
    main_func()
        
    