import json
import os
from flask import Flask, jsonify, request, send_from_directory, render_template_string

app = Flask(__name__, static_folder='static', static_url_path='/static')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'catalog.json')

def load_catalog():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/api/catalog', methods=['GET'])
def get_catalog():
    catalog = load_catalog()
    category = request.args.get('type')  # 'anime' or 'donghua'
    genre = request.args.get('genre')
    audio = request.args.get('audio')
    
    filtered = catalog
    if category and category != 'all':
        filtered = [item for item in filtered if item['type'] == category]
    if genre and genre != 'all':
        filtered = [item for item in filtered if genre in item.get('genres', [])]
    if audio and audio != 'all':
        filtered = [item for item in filtered if audio.lower() in item.get('audio', '').lower()]
        
    return jsonify(filtered)

@app.route('/api/trending', methods=['GET'])
def get_trending():
    catalog = load_catalog()
    featured = [item for item in catalog if item.get('featured')]
    return jsonify(featured)

@app.route('/api/series/<series_id>', methods=['GET'])
def get_series(series_id):
    catalog = load_catalog()
    item = next((x for x in catalog if x['id'] == series_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Series not found"}), 404

@app.route('/api/search', methods=['GET'])
def search_catalog():
    query = request.args.get('q', '').lower().strip()
    catalog = load_catalog()
    if not query:
        return jsonify(catalog)
        
    results = []
    for item in catalog:
        title = item.get('title', '').lower()
        native = item.get('nativeTitle', '').lower()
        genres = " ".join(item.get('genres', [])).lower()
        type_str = item.get('type', '').lower()
        
        if query in title or query in native or query in genres or query in type_str:
            results.append(item)
            
    return jsonify(results)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"🚀 AniDong Anime & Donghua Stream Server running at http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)
