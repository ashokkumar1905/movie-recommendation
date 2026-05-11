import pandas as pd

# Load datasets
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

movie_ratings = pd.merge(ratings, movies, on="movieId")
user_movie_matrix = movie_ratings.pivot_table(
    index="userId",
    columns="title",
    values="rating"
)
movie_mean_ratings = user_movie_matrix.mean().sort_values(ascending=False)


def top_rated_movies(top_n=10):

    return movie_mean_ratings.head(top_n)


if __name__ == "__main__":

    print("\nTop Rated Movies:\n")

    print(top_rated_movies())