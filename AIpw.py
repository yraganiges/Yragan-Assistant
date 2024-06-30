"""AIpw - AI Procesing words ..."""
import random, pickle as pick, config
from AImodule import Neuron
import difflib, pyperclip

class dataset:
    fun_words = 'удача радость счастье любовь улыбка свет добро мир веселье жизнь благодарность успех цветы музыка красота дружба радуга вдохновение тепло ласковый праздник уют весна улучшение прогресс восхищение'
    normal_words = 'дом работа еда улица телефон интернет книга компьютер автомобиль одежда здоровье время деньги путешествие спорт общение учеба развлечения хобби рутина погода природа технологии наука'
    sad_words = 'боль потеря разочарование печаль злость тьма страх болезнь неудача одиночество ненависть конфликт беда утрата слезы уныние отчаяние безысходность разрушение кризис тревога страдание обиды'
    
    all_words = 'удача радость счастье любовь улыбка свет добро мир веселье жизнь благодарность успех цветы музыка красота дружба радуга вдохновение тепло ласковый праздник уют весна улучшение прогресс восхищение дом работа еда улица телефон интернет книга компьютер автомобиль одежда здоровье время деньги путешествие спорт общение учеба развлечения хобби рутина погода природа технологии наука боль потеря разочарование печаль злость тьма страх болезнь неудача одиночество ненависть конфликт беда утрата слезы уныние отчаяние безысходность разрушение кризис тревога страдание обиды'
    
    #dicitonary
    with open(config.path_to_dictionary, 'r') as file:
        words = file.read().split()
        
    words_parasites = ['вот', 'так сказать', 'в принципе']

class NeuralNetwork:
    def __init__(self):
        self.alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        self.bin_alphabet = [1, 1 , 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0, 1]
        
    def search_liminal_words(self, word: str = None, words: list = [], accursary: int = 0) -> list[str]:
        #accursary from 0 to 5
        similar_words = []
        
        for index in words:
            if word[0:len(word) // 2 + accursary].lower() == index[0:len(word) // 2 + accursary].lower() and len(word) > 1:
                similar_words.append(index)
                
        return similar_words     
        
    def Vectoring_text(self, text: str = None, type_vectoring: str = 'alph / binary') -> list[int]:
        output = []
        i = 0
        
        if type_vectoring == 'alph':
            for let in text:
                if let.lower() in self.alphabet:
                    output.append(self.alphabet.index(let.lower()) + 1)
        
        if type_vectoring == 'binary':
            for let in text:
                if let.lower() in self.alphabet:
                    output.append(self.bin_alphabet[self.alphabet.index(let.lower())])
                
        return output
    
    def modern_text(self, text: str, cutoff: float = 0.3, activate_data: float = 0.7):
        self.change_word = None
        i = 0
        self.h_weight = 0.0
        text = text.split()
    
        for word in text:
            self.change_word = None
            print(f'[{i + 1} / {len(text)}]Поиск похожих слов...')
            self.liminal_words = difflib.get_close_matches(word, dataset.words, cutoff = cutoff)
            
            #add liminals words with helping my module
            for index in self.search_liminal_words(word = word, words = dataset.all_words, accursary = 1):
                if index not in self.liminal_words:
                    self.liminal_words.append(index)
                
            print(self.liminal_words)
            #search the most best word in the opinion of AI
            try:
                print(f'[{i + 1} / {len(text)}]замена слов на более лучшие...')
                for index in self.liminal_words:
                    weights = self.Vectoring_text(text = index, type_vectoring = 'binary')
                    inputs = self.Vectoring_text(text = index, type_vectoring = 'alph')
                    bias = len(index) #default - 8
                    n = Neuron(weights, bias)
                    evaluate_word = n.feedforward(inputs = inputs, type_activation = 'sigmoid')
                    
                    if self.h_weight > evaluate_word :
                        self.change_word = index
                    
                    if evaluate_word <= activate_data:
                        self.h_weight = evaluate_word

            except:
                pass
                
            if self.change_word is None:
                self.change_word = word
            
            print(self.change_word)
                
            #change word with helping AI    
            text[i] = self.change_word
            print(text)
            
            try:
                if text[i][len(word) - 1].lower() == 'и':
                    if text[i + 1][len(text[i + 1] - 1)] == 'ж':
                        text[i + 1] += 'ы'
                    else:
                        text[i + 1] += 'и'
            except: pass
             
            i += 1
            
        return ' '.join(text)
                
    def trainAI(self, epochs: int = 1, target: list = None):
        pw = NeuralNetwork()
        CountTrue = 0
        count = 0
        MSEcount = 0
        
        #Train-AI
        for _ in range(epochs * 100):
            #Add random weights for bin-alphabet
            for _ in range(33):
                self.bin_alphabet.append(round(random.uniform(0, 1), 1))
            
            #Train AI to target and write data about bigger target  
            text = random.choice(dataset.all_words)
            
            for train in range(10):
                weights = pw.Vectoring_text(text = text, type_vectoring = 'binary')
                inputs = pw.Vectoring_text(text = text, type_vectoring = 'alph')
                bias = len(text) #default - 8
                
                n = Neuron(weights, bias)
                feedforward_data = n.feedforward(inputs = inputs, type_activation = 'sigmoid')
                
                if feedforward_data > 0.9:
                    CountTrue += 1
                    
            if CountTrue > 8:
                pick.dump(self.bin_alphabet, open('data\\app_data\\ai_data\\WEIGHTS.bin', 'wb'))
                MSEcount += 1
                
            count += 1
            print(f'{count / (epochs)}% from 100%')
        
        print(f'MSE - {MSEcount - (count / MSEcount)}%\nAccursary - {count / MSEcount * 10}% ')
        
if __name__ == '__main__':
    ai = NeuralNetwork()
    # print(ai.Vectoring_text(text = 'абас', type_vectoring = 'binary'))
    # ai.trainAI(epochs = 40)
    
    print(ai.modern_text(text = pyperclip.paste(), activate_data = 0.97, cutoff = 0.8))
    
    words = 'привет ку здарова приветы прислуга'.split()
    print(ai.search_liminal_words(word = 'привет', words = words, accursary = 1))
    
    