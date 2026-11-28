class Movie:
    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres


class Links:
    def __init__(self, movieId, imdbId, tmdbId):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId


class Ratings:
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp


class Tags:
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp
