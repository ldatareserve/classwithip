# for loop with str
for letter in 'Cebu':
    print(letter)

for letter in 'Victoria Falls':
    print(letter)


# for loop with list
dinnerware = ['Fork','Salad Fork','Knife','Butter Knife','Spoon']

for utensils in dinnerware:
    print(utensils)

gas_stations = ['BP','Speedway','Thornton\'s','Shell'] 

for gas in gas_stations:
    print(gas)


# for loop with a series of numbers using the range func
for num in range(2):
    print(num)

for index in range(13):
    print(index)

# for loop with a series of specific nums
for num in range(21,31):
    print(num)

for index in range(100,150):
    print(index)


# for loop with break statements
condiments = ['Ketchup','Mustard','BBQ sauce','Honey Mustard','Ranch']

for sauce in condiments:
    print(sauce)
    if sauce == 'Honey Mustard':
        break

furniture = ['Sofa','Bed','Table','Drawer','Chair']

for unit in furniture:
    print(unit)
    if unit == 'Bed':
        break

# for loop with continue statements
uniform_styles = ['Home','Away','Alternate','Throwback']

for fits in uniform_styles:
    if fits == 'Alternate':
        continue
    print(fits)

sports = ['Football','Basketball','Soccer','Track']

for sport in sports:
    if sport == 'Soccer':
        continue
    print(sport)


# for loop with else statements
counting = [1,2,3,4,5,6,7,8,9,10]

for num in counting:
    print(num)
else:
    print('All done.')

parts_of_door = ['Stiles','Mullion','Rails','Handle','Hinges','Panels']

for parts in parts_of_door:
    print(parts)
else:
    print('Don\'t forget the frame.')


# for loop with end parameter
counting = [1,2,3,4,5,6,7,8,9,10]

for num in counting:
    print(num, end=' ')

parts_of_door = ['Stiles','Mullion','Rails','Handle','Hinges','Panels']

for parts in parts_of_door:
    print(parts, end= ' ')


