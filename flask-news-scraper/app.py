from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/scrape-techcrunch', methods=['GET'])
def get_scraped_data():
    try:
        with open('scraped_data.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "No data found. Please run the scraper."}), 404

if __name__ == '__main__':
    app.run(debug=True)
