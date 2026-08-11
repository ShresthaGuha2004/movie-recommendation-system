2. README for Movie Recommendation System


#  AI Movie Recommendation System

A Content-Based Movie Recommender web application built with Python, Pandas, Scikit-Learn, and Streamlit. The system analyzes movie metadata (genres, keywords, cast, crew, overview) and recommends the 5 most similar movies along with their official poster artwork fetched live via TMDB API integration.

---

##  Key Features
- **Content-Based Filtering:** Analyzes similarity between movies based on combined metadata tags.
- **Cosine Similarity Matrix:** Calculates distance vectors between movie embeddings for instant recommendations.
- **TMDB API Integration:** Fetches high-resolution poster images for recommended movies in real time.
- **Interactive Web Interface:** Searchable dropdown menu with automatic layout rendering via Streamlit.

---

## Tech Stack
| Category | Technology / Library |
| :--- | :--- |
| **Language** | Python 3.12 |
| **Machine Learning** | Scikit-Learn (`CountVectorizer` / `TfidfVectorizer`, Cosine Similarity) |
| **Data Processing** | Pandas, NumPy, Pickle |
| **API Integration** | TMDB (The Movie Database) REST API, Requests |
| **Web Framework** | Streamlit |
| **Version Control** | Git, GitHub |

---

## Repository Structure


movie-recommendation-system/
│
├── dataset/
│   ├── tmdb_5000_movies.csv      # TMDB 5000 Movies Dataset
│   └── tmdb_5000_credits.csv     # TMDB 5000 Credits Dataset
├── model_builder.py              # Feature extraction & matrix computation script
├── app.py                        # Streamlit web app UI with TMDB API fetching
├── movies.pkl                    # Exported processed movie dictionary artifact
├── similarity.pkl                # Pre-calculated cosine similarity matrix artifact
├── requirements.txt              # Required dependencies
└── .gitignore                    # Excluded files
