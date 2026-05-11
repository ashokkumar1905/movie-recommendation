import streamlit as st
import pandas as pd
from recommender import recommend_movies

# Load movies
movies = pd.read_csv("data/movies.csv")
st.title("🎬 AI Movie Recommendation System")

st.write(
    "Get personalized movie recommendations using Machine Learning."
)
selected_movie = st.selectbox(
    "Choose a Movie",
    movies["title"].values
)

if st.button("Recommend"):

    recommendations = recommend_movies(selected_movie)

    st.subheader("Recommended Related Movies")

    for i, movie in enumerate(recommendations, start=1):

        st.write(f"{i}. {movie}")

st.markdown("---")
st.caption("Built using Python, Scikit-Learn and MovieLens Dataset by Ashok kumar")