# while loop
i = 7

while i < 100:
    print('Up, up, and away')
    i += 1

print('Pretty nice up here')

i = -15

while i < 0:
    print('Getting out of the red')
    i += 3

print('Time to build')


# Never ending while loop
i = 12

while i > 10:
    print('Going and...')

print('Can\'t touch this')

i = 79

while i < 200:
    print(i)

print('Numbers don\'t change')


# while loop with statements
i = 3

while i < 9:
    print('Fly again')
    i += 3

i = -40

while i < -30:
    print('Better')
    i += 1


# fstring
temp = input('Enter ideal temperature setting: ')

print(f'Room now set to {temp} degrees.')

licence_yr = input('Verify date of licensure')

print(f'{licence_yr} is within the current range of validity')


# while loop with input func and fstring
weapon = input('Choose your own weapon(Sword or Axe): ')

while weapon == '':
    print('No weapon chosen')
    weapon = input('Choose your own weapon(Sword or Axe): ')

print(f'The {weapon} has been chosen.')

stage = input('Select stage(Stadium or Alleyway): ')

while stage == '':
    print('No stage chosen.')
    stage = input('Select stage(Stadium or Alleyway): ')

print(f'{stage} selected. Round 1, Fight!')


# more complex while loops
pitch_speed = int(input('Fastest recoreded pitch during game? '))

while pitch_speed < 90:
    print('Ineligible for specialized training')
    pitch_speed = int(input('Fastest recoreded pitch during game? '))

print(f'A {pitch_speed}mph pitch is eligible for specialized sessions. Please choose trainer.')

fav_nfl = input('Enter NFl team supported: ')
recent_sb_success = int(input('Franchise Super Bowls since 2010: '))

while recent_sb_success <= 1:
    print('No dynasty potential')
    recent_sb_success = int(input('Franchise Super Bowls since 2010: '))

print(f'With {recent_sb_success} Super Bowls the {fav_nfl} are in position to become a dynasty.')


# using the not operator with while loops
color = input('Color of your house(or q to quit): ')

while not color == 'q':
    print(f'Your color {color} is HOA approved.')
    color = input('Color of your house(or q to quit): ')

print('Please maintain paint every other year.')

movie = input('Next most watched movie(n for N/A): ')

while not movie == 'n':
    print(f'This accounts most next watched movie is {movie}. Continue')
    movie = input('Next most watched movie(n for N/A): ')

print('Data up to date.')


# using the or operator with while loops
num = int(input('Enter random number (100-199): '))

while num < 100 or num > 199:
    print(f'{num} not within range')
    num = int(input('Enter random number (100-199): '))

print(f'{num} is your seat number, please wait in the lobby.')

density_state = input('Which of the states of matter is the least dense(gas/liquid/solid)? ')

while density_state == 'liquid' or density_state == 'solid':
    print(f'{density_state} is incorrect. Try again')
    density_state = input('Which of the states of matter is the least dense(gas/liquid/solid)? ')

print(f'{density_state} is the correct answer. Well done.')



