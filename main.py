from fastapi import FastAPI
from movie import Movie, Links, Ratings, Tags
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
    return read_file("database\\links.csv")


@app.get("/ratings")
def read_ratings():
    return read_file("database\\ratings.csv")


@app.get("/tags")
def read_tags():
    return read_file("database\\tags.csv")


def read_file(file_path):
    objects = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if file_path.endswith("movies.csv"):
                movie = Movie(row[0], row[1], row[2])
                objects.append(movie.__dict__)
            elif file_path.endswith("links.csv"):
                link = Links(row[0], row[1], row[2])
                objects.append(link.__dict__)
            elif file_path.endswith("ratings.csv"):
                rating = Ratings(row[0], row[1], row[2], row[3])
                objects.append(rating.__dict__)
            elif file_path.endswith("tags.csv"):
                tag = Tags(row[0], row[1], row[2], row[3])
                objects.append(tag.__dict__)

    return objects
