import random
import time



print('Welcomte to game')
time.sleep(1)

chance = 1

words = ['word1','word2', 'word3']

answer = random.choice(words)

if answer == 'word1':
    print('your hint: this word1')

if answer == 'word2':
    print('your hint: this word2')

if answer == 'word3':
    print('your hint: this word3')

time.sleep(0.5)

player = input("enter your guess   :")


if player != answer:
    chance -=1
    print('wrong answer. but you have one more right')
    player = input("enter your guess   :")


if player == answer:
    print('congratulations! Correct answer')
    time.sleep(5)


if chance == 0:
    print('Sorry. All your rights are gone. You Lose :(')
    time.sleep(5)
