import random
import Words
from Hangman_art import logo, stages   #imported only these two from the module

words_list = Words.words   #Imported from our own module Words.py

random_word= random.choice(words_list)


word_length = len(random_word)

print(logo)
for _ in range(word_length):
    print('_' , end=" ")

game_over = False
correct_answer = []
lives = 6
while game_over == False:

    guess_word = input("\n\nGuess a letter : ").lower()

    display = ""
    
    if guess_word in correct_answer:
        print(f'''\n
 .-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
|                                          |
|          YOU ALREADY GUESSED '{guess_word}' !      |
|                                          |
 `-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
        ''')

    for letter in random_word:
        if letter ==guess_word:
            correct_answer.append(letter) 
            display += letter

        elif letter in correct_answer:
            display += letter 

        else:
            display += '_'
        
    
    if guess_word not in random_word:
        lives-=1
        print('''\n
.-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
|                                     |
|      WRONG GUESS , TRY AGAIN !      |
|                                     |
`-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
''')
        if lives == 0 :
            print("\n*******************GAME OVER!*******************")
            print(f"\n       The word was '{random_word}'.    \n")
            game_over= True
    
    
    for letter in display:
        print(letter , end = " ")

    print(stages[6 - lives])
    

    if '_' not in display:
        game_over = True
        print("\n*******************YOU WIN*******************" )
        print(f"WITH {lives}/6 ATTEMPTS LEFT!!!")
    else:
        print(f'''
 .-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
|      You have {lives}/6  attempts Left.     |
 `-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
        ''')
        



    


