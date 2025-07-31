from flask import Flask

app = Flask(__name__)

# URL with parameter
@app.route('/user/<username>')
def show_user(username):
    return f"<h1>Hello, {username}!</h1>"

# Another example: number
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"<h1>Viewing Post #{post_id}</h1>"

if __name__ == "__main__":
    app.run(debug=True)

