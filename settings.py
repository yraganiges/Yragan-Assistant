from tkinter import *
from threading import Thread as th
from tkinter.ttk import Combobox
from tkinter import messagebox as msg
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import config, pickle as pick, main

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title('Settings')
        self.root.geometry('600x700')
        self.root.config(bg = config.win_bg, bd = 0)
        try: self.root.iconbitmap(config.win_icon)
        except: pass
        
        def reset_settings():
            global txt
            path_to_settings_folder = 'data\\app_data\\settings\\'
            
            config.NAME = 'Yragan'
            config.max_limit_lenght_request = 300
            config.num_for_indentation = 7
            config.max_time_wait_voice_request = 3
            config.voiceActing_speed = 220
            config.VoiceActing_mode = 'Bot'
            config.path_requests = 'data\\user_data\\requests'
            config.role = config.roles[0]
            
            pick.dump(config.NAME, open(path_to_settings_folder + 'nameAI.bin', 'wb')) 
            pick.dump(config.max_limit_lenght_request, open(path_to_settings_folder + 'mllr.bin', 'wb')) 
            pick.dump(config.num_for_indentation, open(path_to_settings_folder + 'indendations.bin', 'wb')) 
            pick.dump(config.path_requests, open(path_to_settings_folder + 'path_requests.bin', 'wb')) 
            pick.dump(config.role, open(path_to_settings_folder + 'roleAI.bin', 'wb')) 
            pick.dump(config.max_time_wait_voice_request, open(path_to_settings_folder + 'time_wait_voice_request.bin', 'wb')) 
            pick.dump(config.VoiceActing_mode, open(path_to_settings_folder + 'VoiceActing_mode.bin', 'wb')) 
            pick.dump(config.voiceActing_speed, open(path_to_settings_folder + 'VoiceActing_speed.bin', 'wb')) 
            
            #delete_binary_files
            # os.remove(path_to_settings_folder + 'indendations.bin')
            # os.remove(path_to_settings_folder + 'mllr.bin')
            # os.remove(path_to_settings_folder + 'nameAI.bin')
            # os.remove(path_to_settings_folder + 'path_requests.bin')
            # os.remove(path_to_settings_folder + 'roleAI.bin')
            # os.remove(path_to_settings_folder + 'time_wait_voice_request.bin')
            # os.remove(path_to_settings_folder + 'VoiceActing_mode.bin')
            # os.remove(path_to_settings_folder + 'VoiceActing_speed.bin')
            # os.remove(path_to_settings_folder + '.bin')
            
            #create text
            try: txt.destroy()
            except: pass
            
            #Restart main-app
            restart_main_app()
            
            txt = Label(self.root, text = 'settings have been reset!', bg = config.win_bg, fg = '#0b8a04', font = (config.default_font, 15))
            txt.place(relx = 0.5, rely = 0.05, anchor = CENTER)
            
        def apply_settings():
            path_to_settings_folder = 'data\\app_data\\settings\\'
            
            #NameAI
            config.NAME = self.nameAI.get()
            pick.dump(self.nameAI.get(), open(path_to_settings_folder + 'nameAI.bin', 'wb')) 
            
            #MLLR
            config.max_limit_lenght_request = self.mllr.get()
            pick.dump(int(self.mllr.get()), open(path_to_settings_folder + 'mllr.bin', 'wb')) 
            
            #NFI
            config.num_for_indentation = self.nfi.get()
            pick.dump(int(self.nfi.get()), open(path_to_settings_folder + 'indendations.bin', 'wb')) 
            
            #time-wait-req
            config.max_time_wait_voice_request = self.max_time_voice_request.get()
            pick.dump(int(self.max_time_voice_request.get()), open(path_to_settings_folder + 'time_wait_voice_request.bin', 'wb')) 
            
            #VoiceActing speed
            config.voiceActing_speed = self.VoiceActing_speed.get()
            pick.dump(int(self.VoiceActing_speed.get()), open(path_to_settings_folder + 'VoiceActing_speed.bin', 'wb')) 
            
            #path requests
            config.path_requests = self.path_requests.get()
            pick.dump(self.path_requests.get(), open(path_to_settings_folder + 'path_requests.bin', 'wb')) 
            
            #role
            config.role = self.choice_roleAI.get()
            pick.dump(self.choice_roleAI.get(), open(path_to_settings_folder + 'roleAI.bin', 'wb')) 

            #VoiceActing mode
            try:
                if self.choice_mode_VoiceActing.get() == self.choice_mode_VoiceActing[1]:
                    config.VoiceActing_mode = 'Bot'
                    pick.dump('Bot', open(path_to_settings_folder + 'VoiceActing_mode.bin', 'wb'))
                elif self.choice_mode_VoiceActing.get() == self.choice_mode_VoiceActing[2]:
                    config.VoiceActing_mode = 'Artem'
                    pick.dump('Artem', open(path_to_settings_folder + 'VoiceActing_mode.bin', 'wb'))
                elif self.choice_mode_VoiceActing.get() == self.choice_mode_VoiceActing[3]:
                    config.VoiceActing_mode = 'Daima'
                    pick.dump('Daima', open(path_to_settings_folder + 'VoiceActing_mode.bin', 'wb'))
                else:
                    config.VoiceActing_mode = 'Bot'
                    pick.dump('Bot', open(path_to_settings_folder + 'VoiceActing_mode.bin', 'wb'))
            except:
                config.VoiceActing_mode = 'Bot'
                pick.dump('Bot', open(path_to_settings_folder + 'VoiceActing_mode.bin', 'wb'))
        
            #Restart main-app
            restart_main_app()
        
        def restart_main_app():
            try:
                main.App().stop() #stop
                main.App() #Run
            except:
                msg.showerror(config.status_error_1, 'Failed restart main-app!\nPlease, restart manual the "Yragan"')
                exit(0)
        
        def print_data(body, value, x: float = 0.75, y: float = 0):
            data_value = f'{int(round(float(value), 0))} / {body["to"]}'
            try: txt_value.destroy()
            except: pass
            txt_value = Label(self.root, text = data_value, bg = 'gray7', fg = 'white', font = (config.default_font, 12))
            txt_value.place(relx = x, rely = y, anchor = CENTER)
            print(data_value)
        
        #Background
        try:
            self.skils_image = Image.open('assets\\images\\background_3.png')
            self.skils_image = self.skils_image.resize((700, 700)) #TODO: 
            self.skils_image_tk = ImageTk.PhotoImage(self.skils_image) 
            
            self.background = Label(self.root, image=self.skils_image_tk, bd=0)
            self.background.place(x = 0)
        except: pass 
        
        #NameAI
        self.nameAI = Entry(self.root, width = 30, fg = 'white', bg = 'gray18', bd = 0, font = ('Futura-Bold', 16), justify = CENTER)
        self.nameAI.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        self.nameAI.insert(0, config.NAME)
        
        line = Label(self.root, width = 180, bg = 'red', bd = 0, font = ('', 3))
        line.place(relx = 0.5, rely = 0.12, anchor = CENTER)
        
        style = ttk.Style(self.root)
        style.configure("TScale", background = '#171717',troughcolor='red')

        #max_limit_length_request
        txt = Label(self.root, text = 'Max limit length request', bg = config.win_bg, fg = 'white', font = (config.default_font, 15))
        txt.place(relx = 0.5, rely = 0.2, anchor = CENTER)
        
        self.mllr = ttk.Scale(self.root, from_ = 0, to = 300, orient = HORIZONTAL, style="TScale", command = lambda event: (print_data(body = self.mllr, value = event, y = 0.25), ...), length = 200)
        self.mllr.place(relx = 0.5, rely = 0.25, anchor = CENTER)
        self.mllr.set(config.max_limit_lenght_request)
        
        #num_for_indentation
        txt = Label(self.root, text = 'Every indentation after words by after', bg = config.win_bg, fg = 'white', font = (config.default_font, 15))
        txt.place(relx = 0.5, rely = 0.3, anchor = CENTER)
        
        self.nfi = ttk.Scale(self.root, from_ = 0, to = 15, orient = HORIZONTAL, style="TScale", command = lambda event: (print_data(body = self.nfi, value = event, y = 0.35), ...), length = 200)
        self.nfi.place(relx = 0.5, rely = 0.35, anchor = CENTER)
        self.nfi.set(config.num_for_indentation)
        
        #max_time_wait_voice_request
        txt = Label(self.root, text = 'Max time wait voice request\n(if you want to remove the restriction, then leave the parameter at 0)', bg = config.win_bg, fg = 'white', font = (config.default_font, 12))
        txt.place(relx = 0.5, rely = 0.43, anchor = CENTER)
        
        self.max_time_voice_request = ttk.Scale(self.root, from_ = 0, to = 10, orient = HORIZONTAL, style="TScale", command = lambda event: (print_data(body = self.max_time_voice_request, value = event, y = 0.5), ...), length = 200)
        self.max_time_voice_request.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        self.max_time_voice_request.set(config.max_time_wait_voice_request)
        
        #VoiceActing_speed
        txt = Label(self.root, text = 'VoiceActing speed', bg = config.win_bg, fg = 'white', font = (config.default_font, 15))
        txt.place(relx = 0.5, rely = 0.55, anchor = CENTER)
        
        self.VoiceActing_speed = ttk.Scale(self.root, from_ = 0, to = 300, orient = HORIZONTAL, style="TScale", command = lambda event: (print_data(body = self.VoiceActing_speed, value = event, y = 0.6), ...), length = 200)
        self.VoiceActing_speed.place(relx = 0.5, rely = 0.6, anchor = CENTER)
        self.VoiceActing_speed.set(config.voiceActing_speed)
        
        #path_requests
        self.path_requests = Entry(self.root, width = 30, fg = 'white', bg = 'gray18', bd = 0, font = ('Futura-Bold', 16), justify = CENTER)
        self.path_requests.place(relx = 0.5, rely = 0.7, anchor = CENTER)
        self.path_requests.insert(0, config.path_requests)
        
        line = Label(self.root, width = 180, bg = 'red', bd = 0, font = ('', 3))
        line.place(relx = 0.5, rely = 0.72, anchor = CENTER)
            
        #Choice mode VoiceActing
        self.choice_mode_VoiceActing = Combobox(self.root, font = ('Bahnschrift SemiBold', 12), width = 30, justify = CENTER, foreground = 'red')
        self.choice_mode_VoiceActing['values'] = ('Choice mode-VoiceActing...', '_(Recommend)_ Voice-Bot', 'Voice-Artem', 'Voice-Daima')
        self.choice_mode_VoiceActing.current(0)
        self.choice_mode_VoiceActing.place(relx = 0.5, rely = 0.78, anchor = CENTER)
        
        #Choice roleAI
        self.choice_roleAI = Combobox(self.root, font = ('Bahnschrift SemiBold', 12), width = 30, justify = CENTER, foreground = 'red')
        self.choice_roleAI['values'] = config.roles
        self.choice_roleAI.current(0)
        self.choice_roleAI.place(relx = 0.5, rely = 0.84, anchor = CENTER)
        
        #Button reset settings
        self.btn_reset_settings = Button(self.root, bd = 0, text = 'reset-settings', width = 15, height = 2, bg = 'red', fg = 'white', font = (config.default_font, 12), command = reset_settings)
        self.btn_reset_settings.place(relx = 0.3, rely = 0.93, anchor = CENTER)
        
        #Button apply settings
        self.btn_apply_settings = Button(self.root, bd = 0, text = 'apply-settings', width = 15, height = 2, bg = '#f24d1b', fg = 'white', font = (config.default_font, 12), command = apply_settings)
        self.btn_apply_settings.place(relx = 0.7, rely = 0.93, anchor = CENTER)
        
        self.root.mainloop()

if __name__ == '__main__':
    App()
    
        