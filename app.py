import streamlit as st
import pickle
import pandas as pd
import requests

# Set page layout
st.set_page_config(page_title="Movie Recommender", layout="wide")

@st.cache_data
def load_data():
    movies_dict = pickle.load(open('movies.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity

movies, similarity = load_data()

def fetch_poster(movie_id):
    """Fetch movie poster from TMDB API"""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    except Exception:
        pass
    # Fallback placeholder image
    return "https://via.placeholder.com/500x750?text=No+Poster+Available"

def recommend(movie_title):
    movie_index = movies[movies['title'] == movie_title].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
        
    return recommended_movies, recommended_posters

# Streamlit UI Setup
st.title("🎬 AI Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Select or type a movie you like:",
    movies['title'].values
)

if st.button("Get Recommendations"):
    names, posters = recommend(selected_movie_name)
    
    st.write(f"### Movies similar to *{selected_movie_name}*:")
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.image(posters[idx], use_container_width=True)
            st.caption(names[idx])