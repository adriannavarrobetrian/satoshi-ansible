from flask import Flask, jsonify
import os

external_url = os.environ.get('EXTERNAL_URL')

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message=f"Hello from {external_url}!" )

@app.route('/approve')
def hello():
    return jsonify(message=f"Approved from {external_url}!")

# Run the Flask app on port 8181
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181)
