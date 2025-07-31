from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to JSON Demo</h1><p>Go to /api/data to see JSON</p>"

@app.route('/api/data')
def get_data():
    data = {
        "name": "Flask Beginner",
        "age": 25,
        "skills": ["Python", "Flask", "APIs"],
        "is_active": True
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

