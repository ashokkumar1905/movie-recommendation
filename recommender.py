import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("data/movies.csv")

movies["genres"] = movies["genres"].str.replace("|", " ", regex=False)

tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies["genres"])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
movies = movies.reset_index()
indices = pd.Series(movies.index, index=movies["title"]).drop_duplicates()


def recommend_movies(movie_title, top_n=10):

    if movie_title not in indices:
        return ["Movie not found"]

    idx = indices[movie_title]

    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(
        sim_scores,
        key=lambda x: x[1],
        reverse=True
    )

    sim_scores = sim_scores[1:top_n + 1]

    movie_indices = [i[0] for i in sim_scores]

    recommendations = movies["title"].iloc[movie_indices]

    return recommendations.tolist()


if __name__ == "__main__":

    movie = "Toy Story (1995)"

    results = recommend_movies(movie)

    print(f"\nRecommendations for {movie}:\n")

    for movie in results:
        print(movie)