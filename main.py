from fastapi import FastAPI
from movie import Movie
import csv

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/movies")
def read_movies():
    return read_file("database\\movies.csv")

@app.get("/links")
def read_links():
    pass

@app.get("/ratings")
def read_ratings():
    pass

@app.get("/tags")
def read_tags():
    pass

def read_file(file_path):
    objects = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            movieid, title, genres = row
            movie = Movie(movieid, title, genres)
            objects.append(movie.__dict__)

    return objects





