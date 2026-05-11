from recommender import recommend_movies
from user_recommender import top_rated_movies


def hybrid_recommendation(movie_name):

    content_results = recommend_movies(movie_name)

    popular_movies = top_rated_movies()

    return content_results, popular_movies


if __name__ == "__main__":

    movie = "Toy Story (1995)"

    recommendations, popular = hybrid_recommendation(movie)

    print("\nRecommended Movies:\n")

    for movie in recommendations:
        print(movie)

    print("\nPopular Movies:\n")

    print(popular)