# combining lists
states = ['New York','California','Florida','Texas']
cities = ['NYC','LA','Orlando','Houston']
states.extend(cities)
print(states)

fruits = ['Apples','Oranges','Bannanas','Papayas']
vegetables = ['lettuce','tomatoes','celery','onions']
fruits.extend(vegetables)
print(fruits)

tns_shoes = ['Nike','Addidas','Under Armour','Puma']
drs_shoes = ['Stacy Adams','Sperry','Calvin Klein']
tns_shoes.extend(drs_shoes)
print(tns_shoes)

subatomic_part = ['Protons','Elctrons','Neutrons']
states_of_matter = ['Liquid','Solid','Gas']
subatomic_part.extend(states_of_matter)
print(subatomic_part)

phys_systems = ['Circulatory','Respiratory','Digestive','Endocrine']
organs = ['heart','skin','brain','kidney']
phys_systems.extend(organs)
print(phys_systems)


# append func to add element to list
states = ['New York','California','Florida','Texas']
cities = ['NYC','LA','Orlando','Houston']
states.append('Georgia')
print(states)

fruits = ['Apples','Oranges','Bannanas','Papayas']
vegetables = ['lettuce','tomatoes','celery','onions']
fruits.append('Grapes')
print(fruits)

tns_shoes = ['Nike','Addidas','Under Armour','Puma']
drs_shoes = ['Stacy Adams','Sperry','Calvin Klein']
tns_shoes.append('New Balance')
print(tns_shoes)

subatomic_part = ['Protons','Elctrons','Neutrons']
states_of_matter = ['Liquid','Solid','Gas']
subatomic_part.append('Positrons')
print(subatomic_part)

phys_systems = ['Circulatory','Respiratory','Digestive','Endocrine']
organs = ['heart','skin','brain','kidney']
phys_systems.append('Nervous')
print(phys_systems)


# insert func to insert element at specified position of list
states = ['New York','California','Florida','Texas']
cities = ['NYC','LA','Orlando','Houston']
states.insert(2,'Georgia')
print(states)

fruits = ['Apples','Oranges','Bannanas','Papayas']
vegetables = ['lettuce','tomatoes','celery','onions']
fruits.insert(1,'Grapes')
print(fruits)

tns_shoes = ['Nike','Addidas','Under Armour','Puma']
drs_shoes = ['Stacy Adams','Sperry','Calvin Klein']
tns_shoes.insert(3,'New Balance')
print(tns_shoes)

subatomic_part = ['Protons','Elctrons','Neutrons']
states_of_matter = ['Liquid','Solid','Gas']
subatomic_part.insert(2,'Positrons')
print(subatomic_part)

phys_systems = ['Circulatory','Respiratory','Digestive','Endocrine']
organs = ['heart','skin','brain','kidney']
phys_systems.insert(0,'Nervous')
print(phys_systems)


# remove func to remove specific element from list
states = ['New York','California','Florida','Texas']
cities = ['NYC','LA','Orlando','Houston']
states.remove('California')
print(states)

fruits = ['Apples','Oranges','Bannanas','Papayas']
vegetables = ['lettuce','tomatoes','celery','onions']
fruits.remove('Bannanas')
print(fruits)

tns_shoes = ['Nike','Addidas','Under Armour','Puma']
drs_shoes = ['Stacy Adams','Sperry','Calvin Klein']
tns_shoes.remove('Puma')
print(tns_shoes)

subatomic_part = ['Protons','Elctrons','Neutrons']
states_of_matter = ['Liquid','Solid','Gas']
subatomic_part.remove('Neutrons')
print(subatomic_part)

phys_systems = ['Circulatory','Respiratory','Digestive','Endocrine']
organs = ['heart','skin','brain','kidney']
phys_systems.remove('Circulatory')
print(phys_systems)


# clear func removes all elements from list
states = ['New York','California','Florida','Texas']
cities = ['NYC','LA','Orlando','Houston']
states.clear()
print(states)

fruits = ['Apples','Oranges','Bannanas','Papayas']
vegetables = ['lettuce','tomatoes','celery','onions']
fruits.clear()
print(fruits)

tns_shoes = ['Nike','Addidas','Under Armour','Puma']
drs_shoes = ['Stacy Adams','Sperry','Calvin Klein']
tns_shoes.clear()
print(tns_shoes)

subatomic_part = ['Protons','Elctrons','Neutrons']
states_of_matter = ['Liquid','Solid','Gas']
subatomic_part.clear()
print(subatomic_part)

phys_systems = ['Circulatory','Respiratory','Digestive','Endocrine']
organs = ['heart','skin','brain','kidney']
phys_systems.clear()
print(phys_systems)


# index func to return the position of specified element
states = ['New York','California','Florida','Texas']
cities = ['NYC','LA','Orlando','Houston']
print(states.index('Texas'))

fruits = ['Apples','Oranges','Bannanas','Papayas']
vegetables = ['lettuce','tomatoes','celery','onions']
print(fruits.index('Oranges'))

tns_shoes = ['Nike','Addidas','Under Armour','Puma']
drs_shoes = ['Stacy Adams','Sperry','Calvin Klein']
print(tns_shoes.index('Nike'))

subatomic_part = ['Protons','Elctrons','Neutrons']
states_of_matter = ['Liquid','Solid','Gas']
print(subatomic_part.index('Elctrons'))

phys_systems = ['Circulatory','Respiratory','Digestive','Endocrine']
organs = ['heart','skin','brain','kidney']
print(phys_systems.index('Digestive'))


# count func to count quantity of specified value
states = ['New York','California','Florida','Florida','Florida','Texas']
cities = ['NYC','LA','Orlando','Houston']
print(states.count('Florida'))
fruits = ['Apples','Apples','Oranges','Bannanas','Papayas']
vegetables = ['lettuce','tomatoes','celery','onions']
print(fruits.count('Apples'))
tns_shoes = ['Nike','Addidas','Under Armour','Puma','Puma','Puma','Puma']
drs_shoes = ['Stacy Adams','Sperry','Calvin Klein']
print(tns_shoes.count('Puma'))
subatomic_part = ['Protons','Protons','Protons','Elctrons','Neutrons']
states_of_matter = ['Liquid','Solid','Gas']
print(subatomic_part.count('Protons'))
phys_systems = ['Circulatory','Respiratory','Digestive','Endocrine']
organs = ['heart','skin','brain','kidney']
print(phys_systems.count('Respiratory'))


# sort func to sort by numerical or alphabetical order
numbers = ['7','2','9','4','8']
cities = ['NYC','LA','Orlando','Houston']
numbers.sort()
print(numbers)

numbers = ['9','8','7','6','5']
vegetables = ['lettuce','tomatoes','celery','onions']
numbers.sort()
print(numbers)

numbers = ['1','2','1','2','1']
drs_shoes = ['Stacy Adams','Sperry','Calvin Klein']
drs_shoes.sort()
print(drs_shoes)

numbers = ['1000','10','1000000','100','1']
states_of_matter = ['Liquid','Solid','Gas']
states_of_matter.sort()
print(states_of_matter)

numbers = ['7','7','7','7','7']
organs = ['heart','skin','brain','kidney']
organs.sort()
print(organs)


# reverse func to print list in reverse
states = ['New York','California','Florida','Texas']
cities = ['NYC','LA','Orlando','Houston']
states.reverse()
print(states)

fruits = ['Apples','Oranges','Bannanas','Papayas']
vegetables = ['lettuce','tomatoes','celery','onions']
fruits.reverse()
print(fruits)

tns_shoes = ['Nike','Addidas','Under Armour','Puma']
drs_shoes = ['Stacy Adams','Sperry','Calvin Klein']
tns_shoes.reverse()
print(tns_shoes)

subatomic_part = ['Protons','Elctrons','Neutrons']
states_of_matter = ['Liquid','Solid','Gas']
subatomic_part.reverse()
print(subatomic_part)

phys_systems = ['Circulatory','Respiratory','Digestive','Endocrine']
organs = ['heart','skin','brain','kidney']
phys_systems.reverse()
print(phys_systems)


