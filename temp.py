import json

data=json.load(open('data.json'))

i='y'

def loc(word):
    return data[word]

while i == 'y':
    
    word = input ('enter word: ')
    print(loc(word))
    
    i = input('do you wish to cont. y/n: ')
    
    if i=='y':
        continue
    elif i=='n':
        break

        