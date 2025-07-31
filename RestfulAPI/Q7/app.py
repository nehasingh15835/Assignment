from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("form.html", error=None)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')

    # Basic validation
    if not name or not email:
        error = "All fields are required."
        return render_template("form.html", error=error)

    if '@' not in email:
        error = "Please enter a valid email address."
        return render_template("form.html", error=error)

    return render_template("result.html", name=name, email=email)

if __name__ == "__main__":
    app.run(debug=True)

