from flask import Flask, jsonify
import json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

from flask import Flask, jsonify
import json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/scrape', methods=['GET'])
def get_scraped_data():
    try:
        if not os.path.exists('scraped_data.json'):
            return jsonify({"error": "No data found. Please run the scraper."}), 404

        with open('scraped_data.json', 'r') as f:
            content = f.read().strip()
            if not content:
                return jsonify({"error": "Data file is empty."}), 500
            data = json.loads(content)

        return jsonify(data)

    except json.JSONDecodeError:
        return jsonify({"error": "Failed to parse JSON. File may be malformed."}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
