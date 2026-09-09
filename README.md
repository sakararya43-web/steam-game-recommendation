# 🎮 Steam Game Recommender

![Steam Game Recommender](assets/bg.png)

An AI-powered, full-stack web application that uses Machine Learning to analyze your Steam library and intelligently recommend your next gaming obsession. 

By integrating directly with the official Steam and SteamSpy APIs, this engine filters out games you already own and provides personalized suggestions based on genres, tags, developer profiles, and rich descriptions.

## ✨ Features

- 🧠 **Machine Learning Engine**: Utilizes Natural Language Processing (TF-IDF & Cosine Similarity) trained on the top 2,000 most popular Steam games to find hyper-accurate recommendations.
- 🔗 **Universal Steam Search**: Look up any game—even ones not in your library. The backend dynamically fetches live metadata from Steam to vectorize and analyze it on the fly!
- 👤 **Real-Time Library Sync**: Authenticate with your 17-digit Steam ID to instantly load your most-played games and prevent the engine from recommending games you already own.
- ⚡ **Asynchronous API Integration**: Multithreaded backend architecture concurrently fetches live positive/negative review ratios, system requirements, and developer stats in milliseconds.
- 🎨 **Premium UI/UX**: A sleek, responsive Single Page Application (SPA) featuring modern glassmorphism design, neon hover effects, and authentic Steam iconography.

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: Python 3, Flask, Waitress (WSGI Server)
- **Machine Learning**: Scikit-Learn (`TfidfVectorizer`, `cosine_similarity`), Pandas, NumPy, Joblib
- **External APIs**: [Steam Storefront API](https://partner.steamgames.com/doc/webapi_overview), [SteamSpy API](https://steamspy.com/api.php)

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/sakararya43-web/steam-game-recommendation.git
cd "steam game recommend"
```

### 2. Install Dependencies
Make sure you have Python installed, then set up your virtual environment and install the required packages:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Run the ML Training Script (Optional)
The pre-trained model is already included in the `model/` folder. However, if you want to pull the absolute latest top 2,000 games from Steam and retrain the AI from scratch, run:
```bash
cd src
python fetch_data.py
python train_model.py
cd ..
```

### 4. Start the Server
Start the Flask backend (powered by Waitress for stability):
```bash
python app.py
```

### 5. Play!
Open your browser and navigate to `http://127.0.0.1:5000` to start discovering new games!

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/sakararya43-web/steam-game-recommendation/issues).

## 📄 License
This project is open-source and available under the MIT License.