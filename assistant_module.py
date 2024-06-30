#-1
import YraganVoice as yv
import speech_recognition as sr
from tkinter import *
from tkinter import messagebox
from threading import Thread as th 
from PIL import Image, ImageTk 
import pygame, time, random, wikipedia, translate #modules
import config #files

class Voice:
    def __init__(self, language: str = 'ru-RU'):
        self.recognizer = sr.Recognizer()
        self.language = language
        
        self.record_status = False
        
    def Record(self, phrase_time_limit: int = None, start_text: str = 'say anything...'):
        self.record_status = False
        print(start_text)
        
        with sr.Microphone() as source:
            if type(phrase_time_limit) is int and phrase_time_limit != 0:
                self.audio_data = self.recognizer.listen(source, phrase_time_limit = phrase_time_limit)
            else:
                self.audio_data = self.recognizer.listen(source)
            
            self.record_status = True 
            
    def Output_Record(self):
        while self.record_status is True:
            try: return self.recognizer.recognize_google(self.audio_data, language = self.language)            
            except sr.UnknownValueError: return "ERROR: Dont trying recognize speach!"
            except sr.RequestError: return "ERROR: Dont send request the speach!"
            except: return "ERROR: Unknown-error!"
        
class Images:
    def __init__(self, path_to_image: str = None):
        self.path_to_image = path_to_image

    def data_image(self, sizeX: int = None, sizeY: int = None):
        image = Image.open(self.path_to_image)
        if (type(sizeX) is int) and (type(sizeY) is int): image = image.resize((sizeX, sizeY))            
        config.image = ImageTk.PhotoImage(image)

class Request:
    def __init__(self):
        self.answer = None
        self.words_questions = ['что', 'о', 'расскажи', 'раскажи', 'такое', 'такой', 'такие', 'чём', 'чем', 'кто', 'какой', 'какое', 'o', 'как', 'каким', 'куда', 'кем', 'чем', 'скажи', 'история', 'историю', 'к', 'чему', 'почему']
        
    def Processing_indentation(self, text: str = None, num_for_indentation: int = 5):
        if type(text) is str:
            i, c = 0, 0
            txt = text.split()
            
            for letter in txt:
                if i > num_for_indentation:
                    txt.insert(c, '\n')
                    i = 0
                i += 1
                c += 1
                
            return ' '.join(txt)
                
        else: return f"{config.status_error_1} param text is None..."
    
    def processing_request(self, request: str = None):
        list_words = request.split()
        words_for_say = 'повтори повторять повторите скажи скажите сказать кажи кажите казали включи включай включил воспроизведи воспроизвёл воспроизведение плеер плэйер видео видеа мнение относишься относиться отношение мнения мнению думаешь думать думая открой за мной напиши напечатай пиши попиши найди мне тебе'
        
        print(f'{list_words}\n')
        
        for word in list_words:
            if word.lower() in self.words_questions or word.lower() in words_for_say.split():
                list_words.remove(word)
            
        for word in list_words:
            if word.lower() in self.words_questions or word.lower() in words_for_say.split():
                list_words.remove(word)
                
        return ' '.join(list_words) 
                         
    def Output_data_wikipedia(self, query: str = None):
        try: 
            wikipedia.set_lang(config.user_country)
            result = wikipedia.page(query)
            self.answer = result.content
            
            if len(self.answer) >= config.max_limit_lenght_request: 
                self.answer = f'{self.answer[0:config.max_limit_lenght_request]}...'
                
        except wikipedia.exceptions.PageError: self.answer = '<Error>: W1'
        except wikipedia.exceptions.WikipediaException: self.answer = '<Error>: W2'
        except: self.answer = '<Error>: W3'       
        
        return self.answer    

if __name__ == '__main__':
    request = Request()
    print(request.Output_data_wikipedia(query = request.processing_request('украина')))
    print(request.Processing_indentation(text = request.Output_data_wikipedia(query = 'украина')))
    
    