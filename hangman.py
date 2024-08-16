#hangman task1 
from random_word import RandomWords
# Create an instance of RandomWords
def Hangman():
 r = RandomWords()
# Generate a random word
 word = r.get_random_word()

 print("Random word:", word)
 count=4
 wordimagine=word 
#count of lettre in word 

 while count>0 and len(wordimagine)!= 0:
     char=input('give the char:')
     if len(char) != 1 or not char.isalpha():
         print("Please enter exactly one alphabetic character.")
         continue
     if char in wordimagine :
       print('yes ')
       wordimagine = wordimagine.replace(char, "",1)
 
     else:
        print('no, try again')
        count-=1
 if count==0:
         print('game over ')
 else:
      print('you win,the word is  ',word)
#exempla
rep=input('Do you want to play the game:')
if rep.lower().strip()=='yes':
    print ('Enjoy dear')
    Hangman()
else:
    print('good bye ')
           
