# Dictionaries
premier_league_champs = {
    2013:'Manchester United',
    2014:'Manchester City',
    2015:'Chelsea',
    2016:'Leicester City',
    2017:'Chelsea',
    2018:'Manchster City',
    2019:'Manchester City',
    2020:'Liverpool',
    2021:'Manchster City',
    2022:'Manchester City',
    2023:'Manchester City'
}

print(premier_league_champs[2019])

oly_100m_sprint_gold = {
    2008:'Usain Bolt',
    2012:'Usain Bolt',
    2016:'Usain Bolt',
    2020:'Marcell Jacobs'
}

print(oly_100m_sprint_gold[2008])


# Dictionaries con't
movie = {
    'Title':'Jurrasic Park',
    'Director':'Steven Spielberg',
    'Year':1993,
    'Rating':8.2,
    'Genre':'Action'
}

print(movie['Director'])

state = {
    'Name':'New York',
    'Capitol':'Albany',
    'Ratified':'July 26, 1788',
    'Region':'Northeast'
}

print(state['Capitol'])


# Updating dictionaries
movie = {
    'Title':'Jurrasic Park',
    'Director':'Steven Spielberg',
    'Year':1993,
    'Rating':8.2,
    'Genre':'Action'
}

movie['Rating'] = movie['Rating'] + 2
print(movie['Rating'])

movie = {
    'Title':'The Lost World: Jurrasic Park',
    'Director':'Steven Spielberg',
    'Year':1997,
    'Rating':6.5,
    'Genre':'Action'
}

movie['Rating'] = movie['Rating'] + 2
print(movie['Rating'])


# List inside dictionary and a dictionary within dictionary
Movie = {}
Movie['Title'] = 'Spiderman',
Movie['Director'] = 'Sam Raimi',
Movie['Year'] = '2002',
Movie['Rating'] = 7.4,

Movie['Actors'] = ['Tobey Macguire','Kirsten Dunst','William Dafoe']
Movie['Facts'] = {
    'Movielength':121,
    'Language':'English'
}

print(Movie)

Movie = {}
Movie['Title'] = 'Spiderman 2',
Movie['Director'] = 'Sam Raimi',
Movie['Year'] = '2004',
Movie['Rating'] = 7.4,

Movie['Actors'] = ['Tobey Macguire','Kirsten Dunst','Alfred Molina']
Movie['Facts'] = {
    'Movielength':127,
    'Language':'English'
}

print(Movie)


# get func in dictionaries
premier_league_champs = {
    2019:'Manchester City',
    2020:'Liverpool',
    2021:'Manchster City',
    2022:'Manchester City',
    2023:'Manchester City'
}

print(premier_league_champs.get(2023))

oly_100m_sprint_gold = {
    2008:'Usain Bolt',
    2012:'Usain Bolt',
    2016:'Usain Bolt',
    2020:'Marcell Jacobs'
}

print(oly_100m_sprint_gold.get(2012))


# values func in dictionaries
premier_league_champs = {
    2019:'Manchester City',
    2020:'Liverpool',
    2021:'Manchester City',
    2022:'Manchester City',
    2023:'Manchester City'
}

print(premier_league_champs.values())

oly_100m_sprint_gold = {
    2008:'Usain Bolt',
    2012:'Usain Bolt',
    2016:'Usain Bolt',
    2020:'Marcell Jacobs'
}

print(oly_100m_sprint_gold.values())


# keys func in dictionaries
premier_league_champs = {
    2019:'Manchester City',
    2020:'Liverpool',
    2021:'Manchster City',
    2022:'Manchester City',
    2023:'Manchester City'
}

print(premier_league_champs.keys())

oly_100m_sprint_gold = {
    2008:'Usain Bolt',
    2012:'Usain Bolt',
    2016:'Usain Bolt',
    2020:'Marcell Jacobs'
}

print(oly_100m_sprint_gold.keys())


# copy func in dictionaries
premier_league_champs = {
    2019:'Manchester City',
    2020:'Liverpool',
    2021:'Manchster City',
    2022:'Manchester City',
    2023:'Manchester City'
}

print(premier_league_champs.copy())

oly_100m_sprint_gold = {
    2008:'Usain Bolt',
    2012:'Usain Bolt',
    2016:'Usain Bolt',
    2020:'Marcell Jacobs'
}

print(oly_100m_sprint_gold.copy())

