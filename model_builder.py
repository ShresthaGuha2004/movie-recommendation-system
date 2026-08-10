import pandas as pd  
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.metrics.pairwise import cosine_similarity  

def build_model():
    print("Loading dataset...")
    # Load dataset (Download 'tmdb_5000_movies.csv' from Kaggle)
    movies = pd.read_csv('dataset/tmdb_5000_movies.csv')

    # Select relevant features
    movies = movies[['id', 'title', 'overview', 'genres', 'keywords']]
    
    # Handle missing values
    movies.dropna(inplace=True)

    # Combine text features into a single tag column
    movies['tags'] = movies['overview'] + ' ' + movies['genres'] + ' ' + movies['keywords']
    movies['tags'] = movies['tags'].apply(lambda x: x.lower())

    # Create TF-IDF Vectorizer
    print("Extracting features with TF-IDF...")
    tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
    vectors = tfidf.fit_transform(movies['tags'])

    # Compute Cosine Similarity Matrix
    print("Calculating similarity matrix...")
    similarity = cosine_similarity(vectors)

    # Save processed dataframe and model matrix
    pickle.dump(movies[['id', 'title']].to_dict(orient='records'), open('movies.pkl', 'wb'))
    pickle.dump(similarity, open('similarity.pkl', 'wb'))
    print("Model built and exported successfully!")

if __name__ == '__main__':
    build_model()