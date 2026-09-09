import pandas as pd

def load_and_clean_data(filepath='../data/games.csv'):
    # Phase 3 - Clean the game data
    df = pd.read_csv(filepath)
    
    # Remove duplicate games based on app_id
    df = df.drop_duplicates(subset=['app_id'])
    
    # Handle missing values
    df = df.fillna('')
    
    # Ensure every game has usable name, genre, tags
    df = df[df['name'].str.strip() != '']
    df = df[(df['genres'].str.strip() != '') | (df['tags'].str.strip() != '')]
    
    # Phase 4 - Create ML features
    # Combine genres, tags, description, developer, publisher
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
    
    return df

if __name__ == "__main__":
    df = load_and_clean_data()
    print(df.head())
    print(f"Total games after cleaning: {len(df)}")

