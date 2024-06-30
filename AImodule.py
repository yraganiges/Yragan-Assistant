import numpy as np

e = 2.718 #num by euler

class calc:
    def sigmoid(x: int = 0):
        return 1 / (1 + e ** -x)
    
    def tanh(x: int = 0):
        return 2 / (1 + e ** -2*x) - 1

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
 
    def feedforward(self, inputs, type_activation: str = 'sigmoid / tanh') -> int | float:
        total = np.dot(self.weights, inputs) 
        total /= self.bias
        
        if type_activation == 'sigmoid': return calc.sigmoid(total)
        if type_activation == 'tanh': return calc.tanh(total)
        
#Test data
if __name__ == '__main__':
    from AIpw import NeuralNetwork
    
    pw = NeuralNetwork()
    text = 'Адольф Кукущ'
    
    weights = pw.Vectoring_text(text = text, type_vectoring = 'binary')
    inputs = pw.Vectoring_text(text = text, type_vectoring = 'alph')
    
    bias = len(text) #default - 8
    
    n = Neuron(weights, bias)
    print(n.feedforward(inputs = inputs, type_activation = 'sigmoid'))
 