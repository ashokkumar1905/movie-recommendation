# 🎬 Movie Recommendation System

An intelligent movie recommendation system built using Machine Learning techniques and the MovieLens dataset.
This project recommends movies based on content similarity and user preferences, similar to how platforms like Netflix and Amazon Prime suggest content.

---

# 📌 Project Overview

The goal of this project is to create a personalized movie recommendation engine capable of suggesting relevant movies to users based on:

* Movie genres
* Content similarity
* User rating behavior
* Popularity trends

The system uses Content-Based Filtering combined with cosine similarity and TF-IDF vectorization to generate recommendations.

---

# 🚀 Features

* 🎥 Movie recommendation engine
* 🤖 Content-based filtering
* 📊 Cosine similarity algorithm
* 🔍 TF-IDF vectorization
* ⭐ Popular movie analysis
* 🌐 Interactive Streamlit web interface
* 📁 Real-world MovieLens dataset
* ⚡ Fast and lightweight recommendation system

---

# 🧠 Machine Learning Concepts Used

## 1. Content-Based Filtering

Recommends movies similar to the selected movie by analyzing genres and metadata.

Example:

* If a user likes *Batman Begins*
* The system may recommend:

  * The Dark Knight
  * Superman Returns
  * Iron Man

---

## 2. TF-IDF Vectorization

Converts movie genres into numerical vectors so that machine learning algorithms can process them.

Example:

```text
Action Adventure Sci-Fi
```

gets transformed into a mathematical representation.

---

## 3. Cosine Similarity

Measures similarity between movie vectors.

Formula:

```text
cos(θ) = (A · B) / (||A|| ||B||)
```

Movies with similar genres receive higher similarity scores.

---

# 🗂️ Dataset

This project uses the MovieLens Dataset.

Dataset includes:

* Movies
* Ratings
* Genres
* User interactions

Files used:

* `movies.csv`
* `ratings.csv`

Dataset Source:
MovieLens Latest Small Dataset

---

# 🛠️ Technologies Used

| Technology        | Purpose              |
| ----------------- | -------------------- |
| Python            | Core Programming     |
| Pandas            | Data Processing      |
| NumPy             | Numerical Operations |
| Scikit-Learn      | Machine Learning     |
| Streamlit         | Web Application      |
| TF-IDF            | Feature Extraction   |
| Cosine Similarity | Recommendation Logic |

---

# 📁 Project Structure

```text
movie-recommendation-system/
│
├── data/
│   ├── movies.csv
│   ├── ratings.csv
│
├── app.py
├── recommender.py
├── user_recommender.py
├── hybrid.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

---

## 2. Open Project Folder

```bash
cd movie-recommendation-system
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

Start the Streamlit server:

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

# 💻 How It Works

1. User selects a movie
2. System converts movie genres into vectors
3. Cosine similarity compares movie vectors
4. Most similar movies are recommended
5. Recommendations are displayed through Streamlit UI

---

# 📸 Application Preview

Features available in the interface:

* Movie selection dropdown
* Recommendation button
* Recommended movie list
* Interactive UI

---

# 📈 Future Improvements

Some planned improvements for future versions:

* Add collaborative filtering
* Add deep learning recommendation models
* Integrate TMDB API for movie posters
* Add user authentication
* Add watch history tracking
* Add real-time personalized recommendations
* Deploy on cloud platform

---

# 🔥 Challenges Faced

* Handling large movie datasets
* Optimizing similarity calculations
* Improving recommendation relevance
* Managing sparse rating data

---

# 📚 Learning Outcomes

Through this project, I learned:

* Recommendation system architecture
* Feature engineering
* Natural Language Processing basics
* Similarity algorithms
* Streamlit deployment
* Data preprocessing techniques
* Machine Learning workflow

---

# 🎯 Use Cases

This recommendation engine can be adapted for:

* OTT platforms
* E-commerce recommendations
* Music recommendation systems
* Book recommendation systems
* Personalized AI assistants

---

# 📌 Sample Recommendation

Input Movie:

```text
Toy Story (1995)
```

Recommended Movies:

```text
Toy Story 2
A Bug's Life
Monsters, Inc.
Finding Nemo
Cars
```

---

# 👨‍💻 Author

Developed as a Machine Learning project to demonstrate recommendation system concepts and practical AI implementation.

---

# 📄 License

This project is open-source and available for educational and learning purposes.
