from AIpw import NeuralNetwork
from AImodule import Neuron
import random, config
    
def evalueate_word(text: str = 'Text'):
    pw = NeuralNetwork()

    weights = pw.Vectoring_text(text = text, type_vectoring = 'binary')
    inputs = pw.Vectoring_text(text = text, type_vectoring = 'alph')

    bias = len(text) #default - 8

    n = Neuron(weights, bias)
    if n.feedforward(inputs = inputs, type_activation = 'sigmoid') > 0.7:
        return random.choice(config.response.good_stage.split())
    
    elif n.feedforward(inputs = inputs, type_activation = 'sigmoid') > 0.6:
        return random.choice(config.response.middle_stage.split())
    
    elif n.feedforward(inputs = inputs, type_activation = 'sigmoid') < 0.6:
        return random.choice(config.response.bad_stage.split())
 
if __name__ == '__main__':
    print(evalueate_word(text = 'привить'))
    