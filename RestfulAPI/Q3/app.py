from flask import Flask, request, render_template

app = Flask(__name__)

# GET method: Just loads the homepage
@app.route('/')
def home():
    return "Welcome to the homepage!"

# GET + POST method: Handles form
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"Hello, {name}!"
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
