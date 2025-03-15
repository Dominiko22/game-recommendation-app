from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Obsługa CORS, aby żądania frontendowe nie były blokowane

API_KEY = "9118e94249b7472babb649c4786460e0"  # Zamień na swój klucz API RAWG

@app.route('/')
def home():
    return "Witaj na stronie głównej!"

@app.route('/recommend', methods=['GET'])
def recommend():
    genre = request.args.get('genre', '').lower()
    platform = request.args.get('platform', '').lower()

    platform_ids = {
        "pc": 4,
        "playstation": 18,
        "xbox": 1,
        "nintendo": 7,
        "android": 21
    }
    platform_id = platform_ids.get(platform) if platform else None

    params = {
        "key": API_KEY,
        "page_size": 5,
        "ordering": "-rating",
    }
    if genre:
        params["genres"] = genre
    if platform_id:
        params["platforms"] = platform_id

    response = requests.get("https://api.rawg.io/api/games", params=params)
    if response.status_code == 200:
        data = response.json()
        recommendations = [
            {
                "name": game['name'],
                "platforms": [platform['platform']['name'] for platform in game['platforms']],
                "genres": [genre['name'] for genre in game['genres']],
                "image": game['background_image'],
            }
            for game in data['results']
        ]
        return jsonify(recommendations)
    else:
        print(f"Error: {response.status_code}, {response.text}")  # Dodane logowanie błędu
        return jsonify({"error": "Nie udało się pobrać danych z RAWG API"}), response.status_code

if __name__ == "__main__":
    app.run(debug=True)