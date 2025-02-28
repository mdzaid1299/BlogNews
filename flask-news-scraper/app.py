from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def serve_scraped_data():
    file_path = 'output/data.json'
    if not os.path.exists(file_path):
        return jsonify({"error": "No data found. Please run scraper first."}), 404

    with open(file_path, 'r') as file:
        data = json.load(file)

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
