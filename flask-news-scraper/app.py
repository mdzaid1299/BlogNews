from flask import Flask, jsonify
import json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/scrape', methods=['GET'])
def get_scraped_data():
    try:
        with open('scraped_data.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "No data found. Please run the scraper."}), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port, debug=True)
