# input func
name = input('Enter name: ')
age = input('Enter level: ')
print('Welcome ' + name + '. Please file-in with those who are ' + age)

pr_1 = input('1-Rep Bench PR:')
pr_2 = input('1-Rep Squat PR:')
print('Your ' +pr_1+ 'lbs max and ' +pr_2+ 'lbs max qualify you for round 2.' )

name = input('Student name: ')
grad_class = input('Grad year: ')
dono = input('Donation amount: ')
print(f'Thank you for your gift of ${dono}, {name} from class of {grad_class}!')

fav_artist = input('Favorite artist:')
fav_song = input('Favorite song (of artist): ')
print(f'{fav_song} is your favorite song from {fav_artist}. Play song?')

oc = input('Name of original character: ')
ability = input('Superpower of OC: ')
hero_name = input('Alias: ')
print(f'{oc} with the power to {ability} goes by {hero_name}.')

# input func as calculator
num1 = input('Enter 1st number: ')
num2 = input('Enter 2nd number: ')
result = int(num1) + int(num2)
print(result)

num3 = input('Enter 1st number: ')
num4 = input('Enter 2nd number: ')
result = int(num3) - int(num4)
print(result)

num5 = input('Enter 1st number: ')
num6 = input('Enter 2nd number: ')
result = int(num5) * int(num6)
print(result)

num7 = input('Enter 1st number: ')
num8 = input('Enter 2nd number: ')
result = int(num7) / int(num8)
print(result)

num9 = input('Enter 1st number: ')
num10 = input('Enter 2nd number: ')
result = int(num9) ** int(num10)
print(result)

# input func w reply
print('How would you rate your mood on a scale from 1-10?')
mood_rating = input()
print('You feel like a ' + mood_rating + '. Thanks for letting us know!')

print('Which car manufacturer is your preference?')
manu = input()
print(f'The list is now filtered for {manu}.')

print('Set alarm')
bell_time = input()
print(f'Your alarm will go off at {bell_time}.')

print('Guess the word. You have 5 more attempts.')
attempt1 = input()
print(f'{attempt1} is incorrect, try again')

print('Enter direction of structure rotation: ')
direction = input()
print(f'Display now rotating {direction}.')
