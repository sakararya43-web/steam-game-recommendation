import nbformat as nbf

nb = nbf.v4.new_notebook()

text = """\
# Steam Game Recommendation System

This notebook follows the steps to create a machine learning model for game recommendations based on Steam data.
"""

code_imports = """\
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import os
import requests
from dotenv import load_dotenv
"""

text_p3 = """\
## Phase 3 — Clean the game data
Load `games.csv`, remove duplicates, handle missing values.
"""

code_p3 = """\
# Load data
df = pd.read_csv('data/games.csv')

# Clean data
df = df.drop_duplicates(subset=['app_id'])
df = df.fillna('')
df = df[df['name'].str.strip() != '']
df = df[(df['genres'].str.strip() != '') | (df['tags'].str.strip() != '')]
df = df.reset_index(drop=True)

df.head()
"""

text_p4 = """\
## Phase 4 — Create ML features
Combine relevant features into one column.
"""

code_p4 = """\
def combine_features(row):
    features = [
        str(row['genres']),
        str(row['tags']),
        str(row['description']),
        str(row['developer']),
        str(row['publisher'])
    ]
    return " ".join(features)

df['combined_features'] = df.apply(combine_features, axis=1)
df[['name', 'combined_features']].head()
"""

text_p56 = """\
## Phase 5 & 6 — Convert games into vectors and Calculate similarity
Use TF-IDF Vectorizer and Cosine Similarity.
"""

code_p56 = """\
# Phase 5 - TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined_features'])

# Phase 6 - Cosine Similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

print(f"TF-IDF Matrix Shape: {tfidf_matrix.shape}")
print(f"Cosine Similarity Matrix Shape: {cosine_sim.shape}")
"""

text_p7 = """\
## Phase 7 — Build the recommendation function
"""

code_p7 = """\
# Game -> index mapping
indices = pd.Series(df.index, index=df['name']).drop_duplicates()

def recommend_games(game_name, top_n=10, owned_games=None):
    if game_name not in indices:
        # Partial match
        matches = [name for name in indices.index if game_name.lower() in str(name).lower()]
        if not matches:
            return [f"Game '{game_name}' not found."]
        game_name = matches[0]
        
    idx = indices[game_name]
    if isinstance(idx, pd.Series):
        idx = idx.iloc[0]
        
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:] # exclude the game itself
    
    recommendations = []
    owned_app_ids = set(owned_games) if owned_games else set()
    
    for i, score in sim_scores:
        game_app_id = df.iloc[i]['app_id']
        if game_app_id not in owned_app_ids:
            recommendations.append((df.iloc[i]['name'], score))
            if len(recommendations) == top_n:
                break
                
    return recommendations

# Test the function
print("Recommendations for Counter-Strike 2:")
for game, score in recommend_games("Counter-Strike 2", top_n=10):
    print(f"{game} ({score:.2f})")
"""

text_p8 = """\
## Phase 8 & 9 — Steam Integration
Loading Steam API key and conceptually matching games.
"""

code_p8 = """\
load_dotenv()
api_key = os.getenv("STEAM_API_KEY")

class SteamAPI:
    def __init__(self, key):
        self.api_key = key
        
    def get_owned_games(self, steam_id):
        url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
        params = {'key': self.api_key, 'steamid': steam_id, 'format': 'json', 'include_appinfo': True}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if 'response' in data and 'games' in data['response']:
                return [game['appid'] for game in data['response']['games']]
        return []

steam = SteamAPI(api_key)
# Example usage:
# user_owned_app_ids = steam.get_owned_games("USER_STEAM_ID")
# recommend_games("Counter-Strike 2", top_n=10, owned_games=user_owned_app_ids)
"""

text_p10 = """\
## Phase 10 — Save the ML model
"""

code_p10 = """\
model_data = {
    'tfidf_vectorizer': tfidf,
    'tfidf_matrix': tfidf_matrix,
    'cosine_similarity': cosine_sim,
    'dataframe': df,
    'indices': indices
}

os.makedirs('model', exist_ok=True)
joblib.dump(model_data, 'model/model.pkl')
print("Model successfully saved to 'model/model.pkl'")
"""

nb['cells'] = [
    nbf.v4.new_markdown_cell(text),
    nbf.v4.new_code_cell(code_imports),
    nbf.v4.new_markdown_cell(text_p3),
    nbf.v4.new_code_cell(code_p3),
    nbf.v4.new_markdown_cell(text_p4),
    nbf.v4.new_code_cell(code_p4),
    nbf.v4.new_markdown_cell(text_p56),
    nbf.v4.new_code_cell(code_p56),
    nbf.v4.new_markdown_cell(text_p7),
    nbf.v4.new_code_cell(code_p7),
    nbf.v4.new_markdown_cell(text_p8),
    nbf.v4.new_code_cell(code_p8),
    nbf.v4.new_markdown_cell(text_p10),
    nbf.v4.new_code_cell(code_p10)
]

with open('steam_recommender.ipynb', 'w') as f:
    nbf.write(nb, f)
print("Jupyter notebook 'steam_recommender.ipynb' created successfully.")

