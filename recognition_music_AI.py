from tkinter import messagebox as msg

try:
    import YraganBuildAI as ai
    import details_music as dm
    import config #files
except ModuleNotFoundError: msg.showerror('Error in import modules!', 'necessary download list modules: "YraganBuildAI", "details_music", and file config.exe / config.py !')

class Ai:
    def __init__(self, path_music: str = None):
        #variables
        self.bias = 7
        self.x = 2.4 #2.7
        self.i = 0
        self.index_music = 5
        self.status: str = None
        self.type_activation_neuron = 'sigmoid'
        self.HIDDEN_NEURONS_1, self.HIDDEN_NEURONS_2, self.HIDDEN_NEURONS_3 = [], [], []
        self.bias_WEIGTHS = []
        
        #objects
        self.nx = ai.Neuron(neurons = path_music, x = self.x)
        self.music = dm.CheckMusic(path_music = path_music) #{config.path_music}\\music_{index_music}.mp3

    def Search_weights(self, BMP: int = None):
        BMP = int(self.music.BMP())
        print(self.nx._sigmoid_data(self.x))
        if type(BMP) is int:
            #Add DMP in list
            for num in str(BMP):
                self.HIDDEN_NEURONS_1.append(int(num))
                
            #Processing BMP to HIDDEN_LAYER_2
            NHidden = ai.Neuron()
            
            i = 0
            for num in str(self.HIDDEN_NEURONS_1):
                if num.isdigit():
                    if i < 2 and len(self.HIDDEN_NEURONS_1) == 3: self.HIDDEN_NEURONS_2.append(NHidden._sigmoid_data(x = int(num)))
                    if len(self.HIDDEN_NEURONS_1) == 2:
                        if int(num) < 1: num = 1
                        if int(num) == 8: self.HIDDEN_NEURONS_2.append(NHidden._sigmoid_data(x = int(num) - self.bias))
                        if int(num) == 9: self.HIDDEN_NEURONS_2.append(NHidden._sigmoid_data(x = 0.1))
                        if i == 1 and int(num) < 8: self.HIDDEN_NEURONS_2.append(NHidden._sigmoid_data(x = int(num) / 10))
                        if i == 0 and int(num) < 8: self.HIDDEN_NEURONS_2.append(NHidden._sigmoid_data(x = int(num)))
                    if int(num) < 1: num = 1
                    if i == 2 and len(self.HIDDEN_NEURONS_1): self.HIDDEN_NEURONS_2.append(NHidden._sigmoid_data(x = int(num) / 10))
                    i += 1
                
            #Search tonality
            self.music.Tonality()
            self.bias_WEIGTHS.append(self.music.Num_tonality())

            return self.HIDDEN_NEURONS_1, self.HIDDEN_NEURONS_2
        else:
            msg.showerror('Error type-file!', 'please, choice file with format, which relates to music(mp3, ogg, ...) !')

    def Output_data(self):
        i = 0
        
        #BIAS
        for weight in self.HIDDEN_NEURONS_2:
            try:
                self.HIDDEN_NEURONS_2[i] += self.bias_WEIGTHS[i] / 2
                if len(self.HIDDEN_NEURONS_2) == 3: self.HIDDEN_NEURONS_2[i + 1] -= self.bias_WEIGTHS[i] / 2
                print('bias:',self.bias_WEIGTHS[i])
                
                self.HIDDEN_NEURONS_2[i + 2] += (self.bias_WEIGTHS[i])
                i += 1

            except IndexError: pass
            
        #Add-Weights
        self.nx.Add_weights(list_weights = self.HIDDEN_NEURONS_2)
        print(self.nx.output_data_list(target = 2))
        self.nx.Processing_hiden_layer(type_activation = self.type_activation_neuron)    
        self.HIDDEN_NEURONS_3 = self.nx.output_data_list(target = 3)
        
        print(self.HIDDEN_NEURONS_3)
        return self.HIDDEN_NEURONS_3

    def output_status(self):
        
        try:
            try:
                if self.HIDDEN_NEURONS_3[1] == 1: status = 'весёлая музыка'
                elif self.HIDDEN_NEURONS_3[0] == 1: status = 'грустная музыка'
                if self.HIDDEN_NEURONS_3[2] == 1 and self.HIDDEN_NEURONS_3[1] == 0: status = 'спокойная музыка'
                if self.HIDDEN_NEURONS_3[1] == 0 and self.HIDDEN_NEURONS_3[0] == 0: status = 'спокойная музыка'
                if self.HIDDEN_NEURONS_3[0] == 1 and self.HIDDEN_NEURONS_3[1] == 1: status = 'спокойная музыка'

            except IndexError:
                if self.HIDDEN_NEURONS_3[0] == 1: status = 'грустная музыка'
                if self.HIDDEN_NEURONS_3[1] == 1: status = 'весёлая музыка'
                if self.HIDDEN_NEURONS_3[0] == 1 and self.HIDDEN_NEURONS_3[1] == 1: status = 'спокойная музыка'
                if self.HIDDEN_NEURONS_3[0] == 0 and self.HIDDEN_NEURONS_3[1] == 0 : status = 'спокойная музыка'
                
            return status
        
        except: return f'{config.NAME} не распознал тип музыки :('


if __name__ == '__main__':
    NeuralNetwork = Ai(path_music = 'D:\\рабочий стол\\Yragan_Assistant_2_0\\assets\\audio\\sound_click.mp3')
    print(NeuralNetwork.Search_weights(), NeuralNetwork.Output_data())
    print(NeuralNetwork.output_status())