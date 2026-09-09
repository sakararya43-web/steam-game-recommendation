import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import os
from preprocessing import load_and_clean_data

def train_and_save_model():
    print("Loading and cleaning data...")
    df = load_and_clean_data('../data/games.csv')
    
    # Reset index to create index mapping
    df = df.reset_index(drop=True)
    
    print("Phase 5 - Converting games into vectors using TF-IDF...")
    # Phase 5 — Convert games into vectors
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['combined_features'])
    
    print("Phase 6 - Calculating cosine similarity...")
    # Phase 6 — Calculate similarity
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    print("Phase 10 - Saving the ML model...")
    # Game -> index mapping
    indices = pd.Series(df.index, index=df['name']).drop_duplicates()
    
    # Save the necessary components
    model_data = {
        'tfidf_vectorizer': tfidf,
        'tfidf_matrix': tfidf_matrix,
        'cosine_similarity': cosine_sim,
        'dataframe': df,
        'indices': indices
    }
    
    os.makedirs('../model', exist_ok=True)
    joblib.dump(model_data, '../model/model.pkl')
    print("Model saved to '../model/model.pkl'")

if __name__ == "__main__":
    train_and_save_model()

