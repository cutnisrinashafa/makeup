from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os, json

# Inisialisasi Flask
app = Flask(__name__, static_folder='../', static_url_path='')
CORS(app)

# Lokasi folder dataset
DATA_DIR = os.path.join(os.path.dirname(__file__), 'datasets')

# Fungsi bantu untuk membaca file JSON
def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    print(f"📂 Membaca file: {path}")  # debug log
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

# ==========================
# 🏠 ROUTE HALAMAN FRONTEND
# ==========================

@app.route('/')
def home():
    return send_from_directory('../', 'index.html')

@app.route('/products')
def products():
    return send_from_directory('../', 'products.html')

@app.route('/tryon')
def tryon():
    return send_from_directory('../', 'tryon.html')

@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('../css', filename)

@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('../js', filename)

@app.route('/images/<path:filename>')
def serve_images(filename):
    return send_from_directory('../images', filename)

# ==========================
# 📦 ROUTE API (Dataset)
# ==========================

@app.route('/api/blushon')
def api_blushon():
    return jsonify(load_json('BlushOn.json'))

@app.route('/api/eyeshadow')
def api_eyeshadow():
    return jsonify(load_json('Eyeshadow_wardah.json'))

@app.route('/api/lipmatte')
def api_lipmatte():
    return jsonify(load_json('lipmatte.json'))

@app.route('/api/face_regions')
def api_face_regions():
    return jsonify(load_json('face_regions.json'))

# 🔄 Gabungan semua dataset (produk makeup)
@app.route('/api/all_products')
def api_all_products():
    try:
        blushon = load_json('BlushOn.json')
        eyeshadow = load_json('Eyeshadow_wardah.json')
        lipmatte = load_json('lipmatte.json')

        all_products = {
            "blushon": blushon,
            "eyeshadow": eyeshadow,
            "lipmatte": lipmatte
        }

        return jsonify(all_products)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==========================
# 🚀 RUN SERVER
# ==========================
if __name__ == '__main__':
    app.run(debug=True, port=5000)
