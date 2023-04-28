from collections import namedtuple
import random


def what_to_watch():
    """Films list, returns random movie from stored list, matching requirements"""
    Film = namedtuple("Film", "title genre year")
    genres = ('Action', 'Drama', 'Crime', 'Fantasy', 'Sci-Fi', 'Thriller')
    films = []
    films.append(Film('Terminator 2. Judgement Day', 'Action', 1991))
    films.append(Film('The Shawshank Redemption', 'Drama', 1994))
    films.append(Film('Pulp Fiction', 'Crime', 1994))
    films.append(Film('Forrest Gump', 'Drama', 1994))
    films.append(Film('Inception', 'Action', 2010))
    films.append(Film('The Empire Strikes Back', 'Fantasy', 1980))
    films.append(Film('The Matrix', 'Sci-Fi', 1999))
    films.append(Film('The Silence of the Lambs', 'Thriller', 1997))

    print('What kind of movies do you like?')
    for index, item in enumerate(genres):
        print(index + 1, '. ', item, sep='')
    genre = int(input('Please make a choice: '))
    query = [f for f in films if f[1] == genres[genre-1]]
    print(f'Have you seen "{random.choice(query)[0]}"({random.choice(query)[2]})? '
          f'It\'s one of the best {random.choice(query)[1].lower()} movie ever!')

def what_to_listen():
    """Songs list, returns random track from stored list, matching requirements"""
    Song = namedtuple("Song", "title author genre")
    genres = ('Jazz', 'Lounge', 'Disco', 'Pop', 'DnB', 'Rock')
    songs = []
    songs.append(Song('Take Five', 'Dave Brubeck', 'Jazz'))
    songs.append(Song('West End Blues', 'Louis Armstrong', 'Jazz'))
    songs.append(Song('Too Simple', 'Fiona Daniels', 'Lounge'))
    songs.append(Song('Sex and Freedom', 'Roy Bennett', 'Lounge'))
    songs.append(Song('I Will Survive', 'Gloria Gaynor', 'Disco'))
    songs.append(Song('Daddy Cool', 'Boney M.', 'Disco'))
    songs.append(Song('Can\'t Get You Out of My Head', 'Kylie', 'Pop'))
    songs.append(Song('Sexy Bitch', 'David Guetta', 'Pop'))
    songs.append(Song('Breathe', 'The Prodigy', 'DnB'))
    songs.append(Song('Let Me Hold You', 'Netsky', 'DnB'))
    songs.append(Song('Another Brick In The Wall', 'Pink Floyd ', 'Rock'))
    songs.append(Song('Smells Like Teen Spirit', 'Nirvana', 'Rock'))

    print('What kind of music do you like?')
    for index, item in enumerate(genres):
        print(index + 1, '. ', item, sep='')
    genre = int(input('Please make a choice: '))
    query = [s for s in songs if s[2] == genres[genre-1]]
    print(f'You have to listen to "{random.choice(query)[0]}" by {random.choice(query)[1]}! '
          f'It\'s one of the best from {random.choice(query)[2].lower()} ever!')

def what_to_play():
    """Games list, returns random game from stored list, matching requirements"""
    Game = namedtuple("Game", "title genre")
    genres = ('Shooter', 'Strategy', 'Quest', 'RPG', 'Racing')
    games = []
    games.append(Film('Blood', 'Shooter'))
    games.append(Film('Half Life', 'Shooter'))
    games.append(Film('Cossaks', 'Strategy'))
    games.append(Film('Age of Empires', 'Strategy'))
    games.append(Film('Myth', 'Quest'))
    games.append(Film('Siberia', 'Quest'))
    games.append(Film('Fallout', 'RPG'))
    games.append(Film('Skyrim', 'RPG'))
    games.append(Film('Dirt 2', 'Racing'))
    games.append(Film('Colin McRay Rally', 'Racing'))

    print('What kind of games do you like?')
    for index, item in enumerate(genres):
        print(index + 1, '. ', item, sep='')
    genre = int(input('Please make a choice: '))
    query = [g for g in games if f[1] == genres[genre-1]]
    print(f'You should try "{random.choice(query)[0]}"! '
          f'It\'s one of the best {random.choice(query)[1].lower()} game ever!')
