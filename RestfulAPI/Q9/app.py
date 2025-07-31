from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/go-to-contact')
def go_to_contact():
    # Redirect to the contact route
    return redirect(url_for('contact'))

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

