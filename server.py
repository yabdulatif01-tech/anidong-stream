import json
import os
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'catalog.json')

def load_catalog():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if data and len(data) > 0:
                    return data
        except Exception:
            pass
    return []

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
