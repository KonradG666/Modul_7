from random import randint
import time


def run():
    print("**** Bibloteka filmów ****\n" + "-" * 26)


run()

now = time.strftime("%d/%m/%Y")


class Movies:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

        self.view_number = 0

    def __str__(self):
        return (f"Choice: {self.title}\n * release date: {self.year}\n * genre: {self.genre}")

    def play(self):
        self.view_number += 1
        print(f"Number of watches is {self.view_number:02}")


class Series(Movies):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return (
            f"Choice {self.title}\n * release date: {self.year}\n * genre: {self.genre}\n * content: S{self.season:02}E{self.episode:02}")


movie1 = Movies(title="Star Wars - New Hope", year=1977, genre="Sci-fi")
movie2 = Movies(title="Pulp Fiction", year=1994, genre="crimimal")
movie3 = Movies(title="Matrix", year=1999, genre="cyber punk")
movie4 = Movies(title="Dark Knight", year='(2008)', genre="fantasy/drama")
movie5 = Movies(title="Once Upon a Time in Hollywwod", year='(2019', genre="about nothing")
serie1 = Series(title="Wataha", year=2014, genre="adventure", season=1, episode=1)
serie2 = Series(title="X-Files", year=1997, genre="criminal/sci-fi", season=2, episode=3)
serie3 = Series(title="Walking Dead", year=2012, genre="horror/gore", season=4, episode=5, )

movies = [movie1, movie2, movie3, movie4, movie5]
series = [serie1, serie2, serie3]
by_movie_title = sorted(movies, key=lambda movie: movie.title)
by_serie_title = sorted(series, key=lambda serie: serie.title)


def get_movies():
    film_list = []
    for movie in by_movie_title:
        if isinstance(movie, Movies):
            film_list.append(movie)
            print(f"- {movie.title}")
    return film_list

def get_series():
    series_list = []
    for serie in by_serie_title:
        if isinstance(serie, Series):
            series_list.append(serie)
            print(f"- {serie.title}")
    return series_list

def search():
    text = input("Choose picture You are looking for: ")
    for movie in movies:
        if movie.title == text:
            print(f'{movie}')
    for serie in series:
        if serie.title == text:
            print(f'{serie}')