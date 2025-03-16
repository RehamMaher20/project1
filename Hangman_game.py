import random
from collections import Counter

# Words to play on 
someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''
someWords= someWords.split(' ')


user= str(input('Please enter your name: '))
print(f'Hello {user} you are about to play Hangman Game, Are you ready? ')
ready= str(input("please write yes if you want to play: "))

if ready.strip().lower() == 'yes':
    print("Let's Start our Game")
    playing = 'yes'
    while playing == 'yes':
        word= random.choice(someWords)
        letterGuessed= ''
        chances = len(word) + 2
        correct = 0
        flag = 0
        for i in word:
            print('_', end=" ")
        print()
        while (chances != 0) and flag == 0:
            print()
            chances -=1
            try:
                guess = str(input('Enter a letter to guess: ')).lower()
            except:
                print('Enter only a letter!')
                continue

            # Validation of the guess
            if not guess.isalpha():
                print('Enter letter Only')
            elif len(guess)> 1:
                print('Please enter one letter')
            elif guess in letterGuessed:
                print('You have already entered this letter')


            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess


            for char in word:
                if char in letterGuessed and Counter(letterGuessed) != Counter(word):
                    print(char,end=" ")
                    correct +=1
                elif Counter(letterGuessed) == Counter(word):

                    print('The word is : ', end=" ")
                    print(word)
                    flag= 1
                    print('Congratulations, You won!')
#                     break # To break out of the for loop
#                     break # To break out of the while loop
                else:
                    print('_', end=" ")

    
        if chances <=0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))
            
        playing = str(input("Please write yes if you want to play again: "))
        playing= playing.strip().lower()
        
    
else:
    print('No problem friend we can play later')
    