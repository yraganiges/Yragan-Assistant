# print('fefwe'.removeprefix('fe'))

from difflib import get_close_matches
from AIpw import *

word = 'Привет, как дела'
word_list = ["здарова", "ку", "привет", "салам", "apple", 'приветсвую']
nn = NeuralNetwork()

close_matches = get_close_matches(word, word_list, cutoff = 0.1)

print("Похожие слова на", word.split(), ":", close_matches)
print(nn.Vectoring_text(text = ''.join(close_matches), type_vectoring = 'alph'))

# word = 'Привет'
# words = 'привет ку здарова приветы прислуга'

# print(word.count('при'))
# for index in words.split():
#     if 'при' == index[0:3]:
#         print(index)