from flask import Flask, request, jsonify

app = Flask(__name__)

#Strona główna
@app.route('/')
def home():
    return "Witaj na stronie głównej!"

# Endpoint do rekomendacji
@app.route('/recommend', methods=['GET'])
def recommend():
    # Przykładowa odpowiedź - później dodamy logikę rekomendacji
    sample_recommendation = [
        {"title": "The Witcher 3: Wild Hunt", "platform": "PC", "genre": "RPG"},
        {"title": "Cyberpunk 2077", "platform": "PC", "genre": "RPG"},
        {"title": "Grand Theft Auto V", "platform": "PC", "genre": "Action"},
    ]
    return jsonify(sample_recommendation)

if __name__ == '__main__':
    app.run(debug=True)
    