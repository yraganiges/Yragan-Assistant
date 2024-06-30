import config, YraganBuildAI as ai, random, pickle as pick

class dataset:
    fun_words = 'удача радость счастье любовь улыбка свет добро мир веселье жизнь благодарность успех цветы музыка красота дружба радуга вдохновение тепло ласковый праздник уют весна улучшение прогресс восхищение'
    normal_words = 'дом работа еда улица телефон интернет книга компьютер автомобиль одежда здоровье время деньги путешествие спорт общение учеба развлечения хобби рутина погода природа технологии наука'
    sad_words = 'боль потеря разочарование печаль злость тьма страх болезнь неудача одиночество ненависть конфликт беда утрата слезы уныние отчаяние безысходность разрушение кризис тревога страдание обиды'
    
    all_words = 'удача радость счастье любовь улыбка свет добро мир веселье жизнь благодарность успех цветы музыка красота дружба радуга вдохновение тепло ласковый праздник уют весна улучшение прогресс восхищение дом работа еда улица телефон интернет книга компьютер автомобиль одежда здоровье время деньги путешествие спорт общение учеба развлечения хобби рутина погода природа технологии наука боль потеря разочарование печаль злость тьма страх болезнь неудача одиночество ненависть конфликт беда утрата слезы уныние отчаяние безысходность разрушение кризис тревога страдание обиды'

class YraganAI:
    def __init__(self, role: str = None, condition: str = 'funny / normal / sad'):
        self.role = role
        self.condition = condition
        self.alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

        #NEURONS
        self.INPUT_LAYER_1 = []
        self.HIDDEN_LAYER_1 = []
        self.OUTPUT_LAYER_1 = []
        self.i = 0
        
        self.bias = 0
        self.WEIGHTS = []
        self.weight_neuron_1 = 0
        self.weight_neuron_2 = 0
        
    def Vectoring_text(self, text: str = None):
        output = []
        
        for let in text:
            if let.lower() in self.alphabet:
                output.append(self.alphabet.index(let.lower()) + 1)
                
        return output
        
    def estimation_word(self, word: str = None, x: int = 10, weights: list = 'random'):
        if type(word) is str:
            x = x
            
            alphabet = 'йцукенгшщзхъфывапролджэячсмитьбю'
            
            #WEIGHTS
            # funny_condition_weights = [0.1, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.1, 0, 0.1, 0.15, 0.1, 0.3, 0.1, 0.15, 0.2, 0.1, 0.2, 0.1, 0.1, 0.2, 0.1, 0.1, 0.15, 0.2, 0.2, 0.1, 0.2, 0.1] 
            
            # normal_condition_weights = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.15, 0.1, 0, 0.1, 0.15, 0.1, 0.2, 0.1, 0.15, 0.2, 0.1, 0.15, 0.1, 0.1, 0.2, 0.1, 0.1, 0.15, 0.2, 0.1, 0.1, 0.15, 0.1]
            
            # sad_condition_weights = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.15, 0.1, 0, 0.1, 0.1, 0.1, 0, 0.1, 0.15, 0, 0.1, 0.15, 0.1, 0.1, 0.2, 0.1, 0.1, 0.1, 0, 0.1, 0.1, 0.1, 0.1]

            funny_condition_weights = []
            normal_condition_weights = []
            sad_condition_weights = []
            
            if weights == 'random':
                for _ in range(32):
                    funny_condition_weights.append(round(random.uniform(0.1, 0.3), 1))
                    normal_condition_weights.append(round(random.uniform(0.1, 0.3), 1))
                    sad_condition_weights.append(round(random.uniform(0.1, 0.3), 1))
                    
            elif type(weights) is list:
                funny_condition_weights.append(weights[0][i])
                try: normal_condition_weights.append(weights[1][i])
                except: pass
                try: sad_condition_weights.append(weights[2][i])
                except: pass

            if self.condition == 'funny': 
                self.INPUT_LAYER_1 = [word, 1]
                self.WEIGHTS = funny_condition_weights
            elif self.condition == 'normal':
                self.INPUT_LAYER_1 = [word, 0.5]
                self.WEIGHTS = normal_condition_weights
            elif self.condition == 'sad':
                self.INPUT_LAYER_1 = [word, 0] 
                self.WEIGHTS = sad_condition_weights
               
            #Processing and estimation word
            i, j = 0, 0
            for x in range(len(word)):
                i = 0
                for let in alphabet:
                    if word[j].lower() in alphabet:
                        self.weight_neuron_1 += self.WEIGHTS[i]
                        j += 1
                        break
                    i += 1
                    
            #len
            self.weight_neuron_2 = len(word) / 7
               
            #Neurons
            nx = ai.Neuron(neurons = self.INPUT_LAYER_1 , x = x)
            nx.Add_weights(list_weights = [self.weight_neuron_1, self.weight_neuron_2])
            nx.Processing_hiden_layer(type_activation = 'sigmoid')
            # print(nx.output_data_list(target = 3))
            
            return nx.output_data_list(target = 3)
            
    def trainAI(self, epochs: int = 1, rounds: int = 10,  target = None, search_words: list = None):
        Ctrue = 0 #Count-True 
        Wtrue = None #Weights-true
        Ypred = 0
        accursary = 0
        weights = []
        correct_weights = []
        MSE_count = 0
        MSE = 0
        count = 0
        count_load = 0
        
        self.i += 1
        
        #Generate-weights
        for _ in range(32):
            weights.append(round(random.uniform(0, 0.25), 2) )
        
        self.HIDDEN_LAYER_1 = ai.Neuron(neurons = [], x = 10)
        self.HIDDEN_LAYER_1.Add_weights(list_weights = weights)
        
        for epoch in range(epochs * 500):
            # print(YraganAI(condition = 'funny').estimation_word(word = random.choice(dataset.fun_words.split()), x = 100))
            accursary = 0
            Ctrue = 0
            rand_word = random.choice(dataset.all_words.split())
            mood = None
            
            #definition mood and target
            if target == [1, 1]: mood = 'funny'
            if target == [0, 0]: mood = 'normal'
            if target == [1, 0] or target == [0, 1]: mood = 'sad'
            
            for _ in range(rounds):
                if YraganAI(condition = mood).estimation_word(word = rand_word, x = 5) == target and rand_word in search_words:
                    Ctrue += 1
               
            if Ypred > Ctrue:
                try: correct_weights.pop(self.i - 1)
                except: pass
                correct_weights.append(Wtrue)
            else:
                try: correct_weights.pop(self.i - 1)
                except: pass
                correct_weights.append(weights)
                
            pick.dump(correct_weights, open('data\\app_data\\ai_data\\WEIGHTS.bin', 'wb')) #Save weights
                
            Ypred = Ctrue
            Wtrue = self.HIDDEN_LAYER_1.output_data_list(target = 2)
            accursary = Ctrue * 10
            MSE_count += accursary
            count += 1
            count_load += 100 / (epochs * 500)
            print(f'accursary: {accursary}%\nTrain-AI: {round(count_load, 1)}% from 100%')
               
        MSE = MSE_count / count
        print(f'train-accursary: {MSE}% | MSE: {round((100 - MSE), 2)}%')
        print(pick.load(open('data\\app_data\\ai_data\\WEIGHTS.bin', 'rb'))) 
                
if __name__ == '__main__':
    
    # weights_mood = [[0.03, 0.15, 0.21, 0.24, 0.06, 0.14, 0.12, 0.11, 0.13, 0.05, 0.17, 0.23, 0.15, 0.02, 0.18, 0.19, 0.15, 0.08, 0.02, 0.24, 0.01, 0.15, 0.06, 0.21, 0.21, 0.03, 0.18, 0.17, 0.11, 0.02, 0.02, 0.12], [0.18, 0.04, 0.03, 0.01, 0.14, 0.14, 0.19, 0.25, 0.01, 0.22, 0.17, 0.0, 0.25, 0.1, 0.09, 0.19, 0.1, 0.01, 0.06, 0.03, 0.13, 0.08, 0.15, 0.05, 0.17, 0.1, 0.25, 0.08, 0.13, 0.07, 0.01, 0.14], [0.21, 0.06, 0.13, 0.02, 0.08, 0.09, 0.23, 0.15, 0.02, 0.0, 0.15, 0.15, 0.24, 0.21, 0.03, 0.01, 0.21, 0.08, 0.16, 0.14, 0.0, 0.18, 0.14, 0.06, 0.03, 0.01, 0.02, 0.15, 0.06, 0.17, 0.19, 0.04]]
    
    # yai = YraganAI(condition = 'funny')
    # # yai.trainAI(target = [1, 0],  epochs = 5, rounds = 10, search_words = dataset.fun_words.split())
    # print(yai.estimation_word(word = 'успех', weights = weights_mood))
    
    NeuralNetwork = YraganAI()
    print(NeuralNetwork.Vectoring_text(text = 'Артём гондурас'))