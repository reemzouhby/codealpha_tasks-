import nltk
from nltk.tokenize import word_tokenize
greeting=['hi','hello','good morning','good evening']
print('Hello, I am your friendly chatbot !')
while True:
    user=input('You:').lower().strip()
    word=word_tokenize(user)
    if user=='good bye':
        print('Chatbot: Good bye!')
        break
    response = None
    for greet in greeting:
        if greet in user:
            response = greet
            break
    
    if response:
        print(f'Chatbot: {response}',', What is your name?')
    elif 'name'  in word  :
          name=user.split('my name is ')[-1]
          print('Chatbot: Nice to meet you',name)
    elif 'thanks' in word   :
          print('Chatbot: You are welcome!')
    else:
          print('Chatbot: Sorry, I didn\'t understand that.')



   

    
        

