import warnings
warnings.filterwarnings('ignore')
import random
import hangman_stages
word_list=['monday', 'tuesday','wednesday','thursday','amazon','google','rcb','csk','jasmine','medimix','punjab','doctor','cricket','dramas','anime','software','friend','money','wifi']
lives=6
choosen_word=random.choice(word_list)
#print(choosen_word)
display=[]
for letter in choosen_word:
    display+='_'
print(display)
game_over=False
while not game_over:
    guessed_letter=input('guess a letter: ').lower()
    for position in range(len(choosen_word)):
        letter=choosen_word[position]
        if(letter==guessed_letter):
           display[position]=guessed_letter
    print(display)
    print(hangman_stages.stages[lives])
    if guessed_letter not in choosen_word:
        lives-=1
        print('Wrong Guess!!!')
        if lives == 0:
            game_over=True
            print('you lose!!!')
    if '_' not in display:
        game_over=True
        print('You Win!!!')
   

        

