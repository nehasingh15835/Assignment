from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Redirect to greet with a query parameter (name)
    return redirect(url_for('greet', name='FlaskUser'))

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    return render_template('greet.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)

