import nltk
from nltk.tokenize import word_tokenize
from googlesearch import search
import hangman

     
 
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
    elif 'help' in user:
        query = user.split('about ',1)[-1].strip()
        results = search(query,tld='com', num=1, lang="en")
        results = list(results) 
        print('Chatbot: Here is what I found:',results[0])
      
         
    elif 'thanks' or 'thank you ' in word   :
          print('Chatbot: You are welcome!')
    elif 'game'in word:
         print('Chatbot:yeah! I have a funny game! do you want to play?')
    elif 'yes' or 'yeah' in word :
         print('Chatbot:',hangman.Hangman())
    else:
          print('Chatbot: Sorry, I didn\'t understand that.')



   

    
        

