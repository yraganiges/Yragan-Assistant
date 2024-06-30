#-1
#monokai-dimmed
import YraganVoice as yv
from datetime import *
import speech_recognition as sr
from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog
from threading import Thread as th
from PIL import Image, ImageTk
import pygame, time, random, translate as ts, pyttsx3 as tts, pickle as pick, webbrowser as web, pyperclip, YraganVoice as yv, os #modules
import pyautogui as pg, keyboard as keyb #modules
import YraganBuildAI
import config, assistant_module as am, AI_evaluate_words as AIeval, AIpw, window_skils #files
import settings, player #part-apps

class App:
    def __init__(self):
        #objects
        self.sound = pygame.mixer
        self.sound.init()
        self.ts_text = ts.translate.Translator(from_lang = 'en', to_lang = config.user_country)
        self.voice = am.Voice()
        self.request = am.Request()
        
        #ui-objects
        self.lbl_popup = None #Label
        
        #keywords
        self.words_for_listen = f'ураган ураганига {config.NAME} юраган юрэйган yragan ау ураганчик урагинище урагановый урагановое'
        self.words_websites = 'сайт веб браузер'
        self.words_for_play_video = 'открой включи включай включил воспроизведи воспроизвёл воспроизведение плеер плэйер видео видеа youtube ютуб ютубе найди'
        self.words_for_tell_me_about = 'себе умеешь'
        self.word_for_weather = 'прогноз прогнозы прогнозами спрогнозируй спрогнозируют погода погоду погоды погодой'
        self.words_for_opinion = 'мнение относишься относиться отношение мнения мнению думаешь думать думая' 
        self.words_for_joke = 'шутка шутку шутить шутки шуткою шуча шучу пошути пошуча юмор юмора юмором юмоморист хохма хохмы хохму хохмою'
        self.words_for_time = 'время времю времени временем час'
        self.words_for_date = 'дата дату даты день дни дня дню'
        self.words_for_bye = 'прощай выключись'
        self.words_for_close_app = 'закрой закрыли закрывать закрывая выключи выключать выключая'
        self.words_for_music = 'музыка музыку музыкой музыки мюзик музыкальная музыкальный музыкальное музыкальной исполнитель исполнители исполнителям песня песни песню песней'
        self.words_for_recongition_music_ai = 'распознай распознать распознавать распознаешь распозная распознают распознавая распознали зацени заценить заценишь оцени оценяя оценили оценишь оценивать'
        self.words_for_write = 'напиши напечатай пиши попиши'
        self.words_for_hi = 'привет здарова'
        self.words_for_say = 'повтори повторять повторите скажи скажите сказать кажи кажите казали'
        self.words_for_thanks = 'великолепен великолепный великолепны великолепное умный умные умное умным талантлив талантливый талантливы таланты талант замечательно замечательный замечательно замечательное крут крутое крутые круто круты крутой прикольно прикольный прикольные невероятен невероятны невороятное невероятные невероятный уникален уникальное уникальны уникальный молодец молодцы молодци сильный сильные сильное сильным вдохновляет вдохновляя вдохновляют блестящ блестящий блестящие блестящее прекрасен прекрасные прекрасный необыкновен необыкновенное необыкновеное необыкновеный лучший лучшие лучшее лучшое красава крас красавы красавой красавчик красавчики красавчиком крос имба имбы имбой соло солой идеальный идеальное идеальные идеальным'
        self.words_for_modern_text = 'текст текста тексты отрывок отрывки отрывка предложение предложения предложений предложении'
        self.words_for_modern = 'улучши улучшать улучшили улучшил улучшение улучшая модернизировать модернизируй модернизировал модернизирувая модернизировая модернизировали обработай обработали обработая обработал обработал '
        self.words_for_HowAreYou = 'дела чувствуешь чувствовать чувствуете чувствуешь ощущаешь ощущать ощущаете ощущение ощущения ощущением'
        self.words_for_hello = 'прив здоров здаров'
        self.words_for_offenses = 'даун отсталый дурак долбаёб даун идиот аутист дебил дибил пидорас мудак конченный ахуе нах ахер хуй хер залуп козёл бля гандо тупо козел еба ёба '
        
        self.jokes = ['когда поведал братцам хохму, а они не скумекали', 'отверстие', 'ебал осла', '...']
        self.jokes_artem = ['отверстие', 'гугу-гага', 'бро булухтал', 'Гитлер', 'зиг-халь', 'аа', 'это так джасмин пахнет', 'иди убейся', 'пенис']
        
        #answers
        self.answer_confirm = 'ok okay sek good confirm one_second yes_sir'
        self.answer_say_serious = ['Слушай, я не буду говорить глупости', 'давай без своих шуток', 'я не буду говорить это...',
                                   'я промолчу...']
        self.answer_say_mentally_retarded = ['аххаха, пук-пук', 'пись-пись', 'а?', 'гугу-гага', 'я пердел много', 'неееееет', 'ай-швайн-фифти-фифти, лучше не пелдите']
        self.answer_say_old_man = ['хорошо, сынок', 'внучок, я тебе скажу это, но, пожайлуста не осуждай меня']
        self.answer_say_joker = ['почеши мне анус, тогда расскажу, ладно не надо: ', f'{config.user_name} сказзал, что он ', 'Это так джасмином пахнет? Ладно, ']
         
        #variables
        self.last_fact: str = None
        self.count_say_serious: int = 0
        self.count_offenses: int = 0
        self.wikipedia_status: bool = None
        self.user_request: str = None
        self.answer_request: str = None
        self.answer_status: bool = False
        self.status = False
        self.show_popup = None
        self.status_type_request: str = 'voice'
        self.count_modern_text: int = 0
        self.engine = tts.init()
        self.engine.setProperty('rate', config.voiceActing_speed)
        self.ai_text = AIpw.NeuralNetwork()
        try: self.count_request_files: int = pick.load(open('data\\app_data\\count_requests.bin', 'rb'))
        except: self.count_request_files: int = 0
        
        #TODO:
        
        #window
        self.root = Tk()
        self.root.title(config.win_title)
        self.root.geometry(config.win_size)
        self.root['bg'] = config.win_bg
        self.root.resizable(1, 1)
        try: self.root.iconbitmap(config.win_icon)
        except: pass 
        
        def loop_listen():
            while self.status == False:
                self.voice.Record(phrase_time_limit = 2)
                for word in self.voice.Output_Record().split():
                    if word.lower() in self.words_for_listen:
                        th(daemon = True, target = Record).start()
                        self.status = True
                        break
                    else:
                        self.status = False
            else: 
                self.status = True
                
        
        def Write_text(text: str = None):
            output = ''
            for index in text:
                try:
                    output += index
                    self.txt_say.configure(text = output)
                    time.sleep(config.delay_write_text)
                except: break
        
        def voiceActing_text(text: str):
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
        
        def Record():
            #stopping voice-acting
            if config.VoiceActing_mode == 'Bot':
                try: self.engine.stop()
                except: pass
                
            self.status = True    
            
            #objects
            request = am.Request()
            voice = am.Voice()
            engine = tts.init()
            engine.setProperty('rate', config.voiceActing_speed)
                
            self.sound.music.load('assets\\audio\\sound_play.mp3')
            self.sound.music.play()
            
            if self.status_type_request == 'voice':
            
                self.txt_say.configure(text = 'Yragan listen you...', font = (config.default_font, 15)) #configure-text
                # voiceActing_text(text = 'Ураган вас слушает')
                self.txt_say.place(relx = 0.5, rely = 0.2, anchor = CENTER)
                
                #Record-request
                voice.Record(phrase_time_limit = config.max_time_wait_voice_request) #record-request
        
            #output-txt-request
            if self.status_type_request == 'voice':
                self.user_request = voice.Output_Record()
            else:
                self.user_request = str(self.entr_send_request.get())
                
            self.txt_say.configure(text = f'your request: {self.user_request}',)
            time.sleep(0.7)
             
            #Processing_request
            i = 0
            for word in self.user_request.split():
                i += 1
                print(word.lower())
                
                #Tell-me-about
                if word.lower() in self.words_for_tell_me_about or self.user_request.lower() == 'расскажи о себе' or self.user_request.lower() == 'скажи о себе':
                    
                    # th(target = window_skils.App).start() #FIXME: Bug, because creator this module is mentally-retarted !!!!!!!

                    th(daemon = True, target = lambda: Write_text(text = config.tell_me_about)).start()
                    voiceActing_text(text = config.tell_me_about)
                    self.txt_say.configure(text = config.tell_me_about, font = (config.default_font, 10)) 
                    
                    self.wikipedia_status = False
                    self.answer_status = True
                    break
                
                #modern-text
                if word.lower() in self.words_for_modern.split():
                    self.count_modern_text += 1
                
                if word.lower() in self.words_for_modern_text.split() or self.count_modern_text > 1:
                    self.txt_say.configure(text = 'Выделите текст, который надо улучшить')
                    voiceActing_text(text = 'Выделите текст, который надо улучшить')
                    
                    time.sleep(2)
                    
                    #modern text
                    voiceActing_text(text = 'Хорошо, подождите немного, я сейчас сделаю ваш текст лучше...')
                    self.txt_say.configure(text = 'Хорошо, подождите немного,\nя сейчас сделаю ваш текст лучше...')
                    pg.hotkey('ctrl', 'c') #copy text in clipboard
                    pyperclip.copy(self.ai_text.modern_text(text = pyperclip.paste()))

                    #paste text to clipboard
                    self.txt_say.configure(text = 'Ваш текст готов.\nВы можете его вставить из буфера обмена')
                    voiceActing_text(text = 'Ваш текст готов. Вы можете его вставить из буфера обмена')
                    
                    self.count_modern_text = 0
                    self.wikipedia_status = False
                    self.answer_status = True
                    break
                
                #Evaluate_word
                if word.lower() in self.words_for_opinion:
                    output = AIeval.evalueate_word(text = request.processing_request(self.user_request))
                    
                    self.txt_say.configure(text = output)
                    voiceActing_text(text = output)
                    
                    self.wikipedia_status = False
                    self.answer_status = True
                    break
                
                #Write text
                elif word.lower() in self.words_for_write.split():
                    text = random.choice(self.answer_confirm.split())
                    self.txt_say.configure(text = text)
                    voiceActing_text(text)
                    
                    keyb.write(text = request.processing_request(self.user_request), delay = 0.03)
                    
                    self.wikipedia_status = False
                    self.answer_status = True
                    break
                
                #open-site
                elif word.lower() in self.words_websites.split():
                    web.open(f'http:\\{self.user_request.split()[len(self.user_request.split())-1]}.com')
                    self.wikipedia_status = False
                    self.answer_status = True
                    break      
                
                #Playing video
                elif word.lower() in self.words_for_play_video.split():
                    web.open(f'https://www.youtube.com/results?search_query={request.processing_request(self.user_request)}')
                    
                    self.wikipedia_status = False
                    self.answer_status = True
                    break
                                
                #forecast-weather
                elif word.lower() in self.word_for_weather.split():
                    web.open(f'https://yandex.ru/pogoda/')
                    self.wikipedia_status = False
                    self.answer_status = True
                    break
                
                #Time
                elif word.lower() in self.words_for_time.split():
                    current_time = datetime.now().strftime('%H:%M:%S')
                    th(daemon = True, target = lambda: Write_text(text = f'now time: {current_time}')).start()
                    self.txt_say.configure(text = f'now time: {current_time}')
                    
                    engine.say(f'now time: {current_time}')
                    engine.runAndWait()
                    
                    self.wikipedia_status = False
                    self.answer_status = True
                    break
                
                #Date
                elif word.lower() in self.words_for_date.split():
                    current_date = date.today().strftime("%d %B, %Y")
                    th(daemon = True, target = lambda: Write_text(text = f'today: {current_date}')).start()
                    self.txt_say.configure(text = f'today: {current_date}')
                
                    self.wikipedia_status = False
                    self.answer_status = True
                    break
                
                #Joke / Hohma
                elif word.lower() in self.words_for_joke.split():
                    if config.VoiceActing_mode == 'Artem':
                        joke = random.choice(self.jokes_artem)
                    else:
                        joke = random.choice(self.jokes)
                        
                    th(daemon = True, target = lambda: Write_text(text = joke)).start()
                    self.txt_say.configure(text = joke)
                    yv.ArtemVoice(text = joke)
                    
                    self.wikipedia_status = False
                    self.answer_status = True
                    break
                
                #Recongition-music-AI
                # elif word.lower() in self.words_for_recongition_music_ai.split():
                    
                #     text = f'{random.choice(self.answer_confirm.split())}, I recognize it now, but choice the file music'
                    
                #     self.engine.say(f'{random.choice(self.answer_confirm.split())}, сейчас {word}, только укажите файл с музыкой')
                #     self.engine.runAndWait()
                #     self.txt_say.configure(text = text)
                    
                #     path_file = filedialog.askopenfilename(title = 'Choice music-file')
                #     NeuralNetwork = rec_music_AI.Ai(path_music = path_file)
                    
                #     th(daemon = True, target = lambda: Write_text(text = 'please, wait a little...')).start()
                #     self.txt_say.configure(text = 'please, wait a little...')
                #     NeuralNetwork.Search_weights()
                    
                #     # th(daemon = True, target = lambda: Write_text(text = 'final steps...\nplease, give me more one second, just a little left...')).start()
                #     self.txt_say.configure(text = 'final steps...\nplease, give me more one second, just a little left...')
                #     NeuralNetwork.Output_data()

                #     self.txt_say.configure(text = f'{config.NAME} думает, что это {NeuralNetwork.output_status()}')
                    
                #     self.wikipedia_status = False
                #     self.answer_status = True
                #     break
                
                #Search-Music
                elif word.lower() in self.words_for_music.split():
                    req = self.user_request.split()[i:]
                    web.open(f'https:\\rus.hitmotop.com\search?q={" ".join(req)}') 
                    
                    self.wikipedia_status = False
                    self.answer_status = True
                    break
                
                #Thanks
                elif word.lower() in self.words_for_thanks.split():
                    text = 'да, я такой, спасибо за благодарства. Я стараюсь быть лучшим!'
                    th(daemon = True, target = lambda: Write_text(text = text)).start()
                    text = request.Processing_indentation(text = text, num_for_indentation = 5)
                    self.txt_say.configure(text = text)
                    voiceActing_text(text = text)
                    
                    self.wikipedia_status = False
                    self.answer_status = True
                    break    
                    
                #Repeat / say
                elif word.lower() in self.words_for_say.split():
                    text = None
                    
                    if config.role == 'serious':
                        if self.count_say_serious <= 3:
                            text = random.choice(self.answer_say_serious)
                            self.count_say_serious += 1
                        
                        elif self.count_say_serious > 3:
                            text = 'Я больше не буду тебе повторять простые вещи!'
                            
                    elif config.role == 'mentally-retarded': 
                        text = random.choice(self.answer_say_mentally_retarded)
                    elif config.role == 'joker': 
                        text = f'{random.choice(self.answer_say_joker)} {request.processing_request(self.user_request)}'
                    elif config.role == 'old-man':
                        text = f'{random.choice(self.answer_say_old_man)} {request.processing_request(self.user_request)}'    
                    elif config.role == 'normal':
                        text = f'{random.choice(self.answer_confirm.split())}, {request.processing_request(self.user_request)}'
                     
                    th(daemon = True, target = lambda: Write_text(text = request.Processing_indentation(text))).start()    
                    self.txt_say.configure(text = request.Processing_indentation(text), font = (config.default_font, 12))
                    voiceActing_text(text) 
                    
                    self.wikipedia_status = False
                    self.answer_status = True
                    break
                
                #Close App
                elif word.lower() in self.words_for_close_app.split():
                    text = random.choice(self.answer_confirm.split())
                    self.txt_say.configure(text = text)
                    voiceActing_text(text)
            
                    pg.hotkey('alt','f4')
                    
                    self.wikipedia_status = False
                    self.answer_status = True
                    break
                    
                else: self.wikipedia_status = True
            
            #Hello
            for index in self.words_for_hello.split():
                if self.user_request.lower().count(index) > 0 and self.answer_status is False:
                    answer = f'{random.choice("Здарова Привет Ку Хай".split())}'
                    self.txt_say.configure(text = answer)
                    voiceActing_text(answer)
                    
                    self.wikipedia_status = False
                    self.answer_status = True
                
            #Offenses
            for index in self.words_for_offenses.split():
                if self.user_request.lower().count(index) > 0 and self.answer_status is False and config.status_response_to_the_offenses is True:
                    if self.count_offenses < 3:
                        answer = f'Не стоит меня оскорблять..., предупреждаю тебя!'
                        self.txt_say.configure(text = answer)
                        voiceActing_text(answer)
                        
                        self.count_offenses += 1
                        
                    elif self.count_offenses >= 3:
                        answer = 'зря... Предупреждал я тебя!'
                        self.txt_say.configure(text = answer)
                        voiceActing_text(answer)
                        
                        try: os.system("shutdown /s /t 0")
                        except: exit(0)
                       
                    self.wikipedia_status = False
                    self.answer_status = True 
                    break
                else:
                    break
                
            #Procesing-request
            
            if request.Output_data_wikipedia(request.processing_request(self.user_request))[0:10] != '<Error>: W' and self.wikipedia_status is True:
                
                text = request.Processing_indentation(request.Output_data_wikipedia(request.processing_request(self.user_request)))
                th(daemon = True, target = lambda: Write_text(text = text)).start()
                self.txt_say.configure(text = text,
                                       font = (config.default_font, 10), justify = CENTER)
                self.txt_say.place(relx = 0.5, rely = 0.17, anchor = CENTER)
                
                #data
                self.answer_request = request.Output_data_wikipedia(request.processing_request(self.user_request))
                if config.save_requests is True:
                    if type(self.count_request_files) is not int:
                        self.count_request_files = 0
                    self.count_request_files += 1
                    
                    self.save_voice_request() #save file-request
                
                #save data in binary-file
                pick.dump(self.count_request_files, open('data\\app_data\\count_requests.bin', 'wb'))
                
                # voice-acting answer
                if config.VoiceActing_mode.lower() == 'bot':
                    try:
                        engine.say(text = request.Output_data_wikipedia(request.processing_request(self.user_request)))
                        engine.runAndWait()
                    except:
                        msg.showerror(config.status_error_1, 'The bot cannot voice this text!')
                elif config.VoiceActing_mode.lower() == 'Artem':
                    yv.ArtemVoice(text = request.Output_data_wikipedia(request.processing_request(self.user_request)))
                elif config.VoiceActing_mode.lower() == 'Daima':
                    yv.DaimaVoice(text = request.Output_data_wikipedia(request.processing_request(self.user_request)))

                self.answer_status = True
                
            elif self.answer_status == False:
                self.txt_say.configure(text = 'The request could not be processed!')
                self.answer_status = False

            #Edit-Data
            self.status_type_request = 'voice'
            self.answer_status = False
            
            self.btn_voice = Label(self.root, bd = 0, image = image, bg = config.win_bg)
            self.btn_voice.bind('<Button - 1>', lambda event: th(daemon = True, target = Record).start())
            self.btn_voice.place(relx = 0.5, rely = 0.5, anchor = CENTER)
            
            #Repeat - listen
            self.status = False
            th(daemon = True, target = loop_listen).start()
            
            print(True)
    
        def PopUp_Text(body = None, text: str = None, bg: str = 'gray12', fg: str = 'white', status: str = 'show \ hidden', y: float = None):
            if status == 'show' and (self.show_popup is False or self.show_popup is None):
                if type(body) != bool and type(text) is str and y is None:
                    self.lbl_popup = Label(body, text = text, width = len(text) + 3, bg = bg, fg = fg, font = ('', 10))
                    self.lbl_popup.place(relx = 0.5, rely = 0.73, anchor = CENTER) 
                    
                    self.show_popup = True
                    
                elif type(body) != bool and type(text) is str and type(y) is float:
                    self.lbl_popup = Label(self.root, text = text, width = len(text) + 3, bg = bg, fg = fg, font = ('', 10))
                    self.lbl_popup.place(relx = 0.5, rely = y, anchor = CENTER) 
                    
                    self.show_popup = True

            elif status == 'hidden' and (self.show_popup is True):
                try: self.lbl_popup.destroy()
                except: pass
                finally: self.show_popup = False
          
        #Enter and Leave mouse-widget      
        def on_enter_text(event):
            event.widget.configure(fg = config.pre_default_bg)
            PopUp_Text(text = 'click on text LKM to copy text', status = 'show', body = event.widget, y = 0.3)

        def on_leave_text(event):
            event.widget.configure(fg = config.default_bg)
            PopUp_Text(status = 'hidden', body = event.widget)
            
        def Send_text_req():
            th(daemon = True, target = Record).start()
            self.status_type_request = 'text'
            
        def Show_facts(sleep: int = 5):
            #TODO: ДОБАВИТЬ РЕДКИЙ ШАНС(модуль: "GetChance") НА ЛЕГЕНДАРНЫЙ ФАКТ
            while config.status_facts == True:
                try: txt_facts.destroy()
                except: pass
                
                new_fact = self.request.Processing_indentation(text = random.choice(config.FACTS), num_for_indentation = 3)
                if new_fact == self.last_fact:
                    continue
                
                txt_facts = Label(self.root, text = f'💡 Fact about Yragan: {new_fact}',
                                    font = (config.default_font, 8), bg = '#520806', fg = 'white')
                txt_facts.place(relx = 0.5, rely = 0.95, anchor = CENTER) 
                txt_facts.bind('<Enter>', lambda event: event.widget.configure(fg = config.pre_default_bg))
                txt_facts.bind('<Leave>', lambda event: event.widget.configure(fg = 'white'))
                txt_facts.bind('<Button - 1>', lambda event: pyperclip.copy(txt_facts['text']))
                
                self.last_fact = new_fact
                time.sleep(sleep)
            
        #Background
        if config.show_background is True:
            try:
                self.skils_image = Image.open('assets\\images\\background_2.png')
                self.skils_image = self.skils_image.resize((500, 500)) #TODO: 
                self.skils_image_tk = ImageTk.PhotoImage(self.skils_image) 
                
                self.background = Label(self.root, image=self.skils_image_tk, bd=0)
                self.background.pack()
            except: pass
        
        #Button-voice
        image = Image.open('assets\\images\\microphone_off.png')
        image = image.resize((150, 150))
        image = ImageTk.PhotoImage(image)
        
        self.btn_voice = Label(self.root, bd = 0, image = image, bg = config.win_bg)
        self.btn_voice.bind('<Button - 1>', lambda event: th(daemon = True, target = Record).start())
        self.btn_voice.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        
        #Text
        self.txt_say = Label(self.root, text = 'Say - "Ураган"',  bg = config.win_bg, fg = config.default_bg, justify = CENTER, font = (config.default_font, 15))
        self.txt_say.place(relx = 0.5, rely = 0.2, anchor = CENTER)
        self.txt_say.bind('<Button - 1>', lambda event: (pyperclip.copy(event.widget['text']), event.widget.configure(fg = '#e66e6e')))
        self.txt_say.bind('<Enter>', on_enter_text)
        self.txt_say.bind('<Leave>', on_leave_text)
        
        #DownLabel
        self.lbl = Label(self.root, width = 300, height = 5, bg = '#520806', font = ('', 7))  
        self.lbl.place(relx = 0.5, rely = 0.96, anchor = CENTER)
        
        #Button-Settings
        self.btn_settings = Button(self.root, text = 'Settings', bg = config.win_bg, fg = 'white', font = (config.default_font, 10), width = 13, height = 2, bd = 0, command = lambda: th(target = settings.App()))
        self.btn_settings.place(rely = 0.95, relx = 0.88, anchor = CENTER)
        self.btn_settings.bind('<Enter>', lambda event: event.widget.configure(bg = 'gray7'))
        self.btn_settings.bind('<Leave>', lambda event: event.widget.configure(bg = config.win_bg))
        self.btn_settings.bind('<Button - 1>', lambda: self.sound.music.play(''))
        
        #Button-requests_list
        self.btn_requests_list = Button(self.root, text = 'Requests-list', bg = config.win_bg, fg = 'white', font = (config.default_font, 10), width = 13, height = 2, bd = 0, command = lambda: th(target = player.App()))
        self.btn_requests_list.place(rely = 0.95, relx = 0.12, anchor = CENTER)
        self.btn_requests_list.bind('<Enter>', lambda event: event.widget.configure(bg = 'gray7'))
        self.btn_requests_list.bind('<Leave>', lambda event: event.widget.configure(bg = config.win_bg))

        #Entry
        self.entr_send_request = Entry(self.root, width = 30, fg = 'white', bg = 'gray18', bd = 0, font = ('Futura-Bold', 16), justify = CENTER)
        self.entr_send_request.place(relx = 0.5, rely = 0.8, anchor = CENTER)
        self.entr_send_request.insert(0, 'Send-text-request')
        self.entr_send_request.bind('<Enter>', lambda event: PopUp_Text(text = f'press "{config.Key.send_text_request}" to send text-request', status = 'show', body = self.root))
        self.entr_send_request.bind('<Leave>', lambda event: PopUp_Text(status = 'hidden'))
        
        line = Label(self.root, width = 180, bg = 'red', bd = 0, font = ('', 3))
        line.place(relx = 0.5, rely = 0.83, anchor = CENTER)
        
        #BINDS
        keyb.add_hotkey(config.Key.copy_text, lambda: pyperclip.copy(self.txt_say['text'])) #Copy-text
        keyb.add_hotkey(config.Key.send_text_request, Send_text_req)
        
        th(daemon = True, target = loop_listen).start() #listen Yragan
        th(daemon = True, target = lambda: Show_facts(sleep = 10)).start() #Show FACTS about Yragan #TODO: Смотреть в функции...
         
        # th(target = window_skils.App).start() 
        config.running_status = True
        self.root.mainloop()
        
    def save_voice_request(self):
        text_for_VoiceActing = f'request from user {config.user_name}. {self.user_request}. answer request {self.answer_request}'
        self.engine.save_to_file(text_for_VoiceActing, f'{config.path_requests}\\request - {self.count_request_files} [{self.user_request}].mp3')
        
        #save-txt-file
        with open(f'{config.path_requests}\\request - {self.count_request_files} [{self.user_request}].txt', 'w') as file:
            file.write(f'user request: {self.user_request}\nanswer request: {self.answer_request}')
            file.close()

    # def Record

    def stop(self):
        self.root.destroy()
        
if __name__ == '__main__':
    App()
    
        