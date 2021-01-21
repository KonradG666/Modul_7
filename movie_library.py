from random import randrange
import time

now = time.strftime("%d/%m/%Y")

class Movies:
    def __init__(self, title, year, genre, view_number=0):
        self.title = title
        self.year = year
        self.genre = genre
        self.view_number = view_number

    def __str__(self):
        return (f"Choice: {self.title}\n * release date: {self.year}\n * genre: {self.genre}")

    def play(self):
        self.view_number = self.view_number + 1
        print(f"Number of watches is {self.view_number:02}")


class Series(Movies):
    def __init__(self, title, year, genre, season, episode):
        super().__init__(title, year, genre)
        self.season = season
        self.episode = episode

    def __str__(self):
        return (
            f"Choice {self.title}\n * release date: {self.year}\n * genre: {self.genre}\n * content: S{self.season:02}E{self.episode:02}")


movie1 = Movies(title="Star Wars - New Hope", year=1977, genre="Sci-fi")
movie2 = Movies(title="Pulp Fiction", year=1994, genre="crimimal")
movie3 = Movies(title="Matrix", year=1999, genre="cyber punk")
movie4 = Movies(title="Dark Knight", year=2008, genre="fantasy/drama")
movie5 = Movies(title="Once Upon a Time in Hollywood", year=2019, genre="about nothing")
serie1 = Series(title="Wataha", year=2014, genre="adventure", season=1, episode=1)
serie2 = Series(title="X-Files", year=1997, genre="criminal/sci-fi", season=2, episode=3)
serie3 = Series(title="Walking Dead", year=2012, genre="horror/gore", season=4, episode=5, )

movies_and_series = [movie1, movie2, movie3, movie4, movie5, serie1, serie2, serie3]
by_title = sorted(movies_and_series, key=lambda picture: picture.title)
by_release = sorted(movies_and_series, key=lambda picture: picture.year)


def get_movies():
    movies = []
    for m in by_title:
          if not isinstance (m, Series):
            movies.append(m)
            print(f"- {m.title}")
    return movies

def get_series():
    series = []
    for s in by_title:
        if isinstance(s, Series):
            series.append(s)
            print(f"- {s.title}")
    return series

def search():
    text = input("Choose picture You are looking for: ")
    for picture in movies_and_series:
        if picture.title.lower() == text.lower():
            print(picture)


def top_title(type, type2):
    top = []
    if type == "Movies":
      for picture in movies_and_series:
        if picture.view_number > 0:
            if isinstance(picture, Movies):
              top.append(picture.view_number)
              print(f'{picture} with {picture.view_number} views')
    elif type2 == "Series":
      for picture in movies_and_series:
        if picture.view_number > 0:
            if isinstance(picture, Series):
              top.append(picture.view_number)
              print(f'{picture} with {picture.view_number} views')
    return top

def generate_views(movies_and_series):
        library = randrange(len(movies_and_series))
        movie = movies_and_series[library]
        views = randrange(100)
        movie.view_number = views

def generate_views_10(movies_and_series):
    for i in range(100):
        generate_views(movies_and_series)

generate_views_10(movies_and_series)


def run():
    print("\t\t**** Bibloteka filmów ****\n" "\t\t"+ "-" * 26)
    get_movies()
    get_series()
    print(f"\t\t**** Najpopularniejsze filmy i seriale dnia {now} ****\n" + "\t\t" + "-" * 59)
    top_title("Movies", "Series")

run()