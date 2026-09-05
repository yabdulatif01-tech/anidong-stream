import json
import os
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'catalog.json')

DEFAULT_CATALOG = [
  {
    "id": "solo-leveling",
    "title": "Solo Leveling",
    "type": "anime",
    "country": "Japan",
    "poster": "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?w=600&auto=format&fit=crop&q=80",
    "rating": 9.8,
    "episodes": [
      { "number": 1, "title": "1-qism: I'm Used to It", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4" },
      { "number": 2, "title": "2-qism: If I Had One More Chance", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4" },
      { "number": 3, "title": "3-qism: It's Like a Game", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4" }
    ]
  },
  {
    "id": "naruto-shippuden",
    "title": "Naruto Shippuden",
    "type": "anime",
    "country": "Japan",
    "poster": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=600&auto=format&fit=crop&q=80",
    "rating": 9.9,
    "episodes": [
      { "number": 1, "title": "1-qism: Uyga qaytish", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4" },
      { "number": 2, "title": "2-qism: Akatsuki harakatga keldi", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4" }
    ]
  },
  {
    "id": "soul-land",
    "title": "Soul Land (Douluo Dalu)",
    "type": "donghua",
    "country": "China",
    "poster": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=600&auto=format&fit=crop&q=80",
    "rating": 9.6,
    "episodes": [
      { "number": 1, "title": "1-qism: Rebirth in Douluo Dalu", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerJoyplays.mp4" },
      { "number": 2, "title": "2-qism: Blue Silver Grass", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerMeltdowns.mp4" }
    ]
  },
  {
    "id": "btth",
    "title": "Battle Through the Heavens",
    "type": "donghua",
    "country": "China",
    "poster": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=600&auto=format&fit=crop&q=80",
    "rating": 9.5,
    "episodes": [
      { "number": 1, "title": "1-qism: The Fallen Prodigy", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4" },
      { "number": 2, "title": "2-qism: Mysterious Ring", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/SubaruOutbackOnStreetAndDirt.mp4" }
    ]
  },
  {
    "id": "demon-slayer",
    "title": "Demon Slayer: Kimetsu no Yaiba",
    "type": "anime",
    "country": "Japan",
    "poster": "https://images.unsplash.com/photo-1563089145-599997674d42?w=600&auto=format&fit=crop&q=80",
    "rating": 9.7,
    "episodes": [
      { "number": 1, "title": "1-qism: Cruelty", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4" },
      { "number": 2, "title": "2-qism: Trainer Sakonji Urokodaki", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WeAreGoingOnBullrun.mp4" }
    ]
  },
  {
    "id": "a-will-eternal",
    "title": "A Will Eternal (Yi Nian Yong Heng)",
    "type": "donghua",
    "country": "China",
    "poster": "https://images.unsplash.com/photo-1514539079130-25950c84af65?w=600&auto=format&fit=crop&q=80",
    "rating": 9.4,
    "episodes": [
      { "number": 1, "title": "1-qism: Lighting the Incense", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WhatCarCanYouGetForAGrand.mp4" }
    ]
  }
]

def load_catalog():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if data:
                    return data
        except Exception:
            pass
    return DEFAULT_CATALOG

@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/api/catalog', methods=['GET'])
def get_catalog():
    catalog = load_catalog()
    category = request.args.get('type')
    if category and category != 'all':
        catalog = [item for item in catalog if item.get('type') == category]
    return jsonify(catalog)

@app.route('/api/series/<series_id>', methods=['GET'])
def get_series(series_id):
    catalog = load_catalog()
    item = next((x for x in catalog if x['id'] == series_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Series not found"}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
