from flask import Flask, render_template

app = Flask(__name__)

# Custom filter: reverse a string
def reverse_string(s):
    return s[::-1]

# Register filter with Jinja
app.jinja_env.filters['reverse'] = reverse_string

@app.route('/')
def home():
    name = "Flask Beginner"
    return render_template("home.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)

