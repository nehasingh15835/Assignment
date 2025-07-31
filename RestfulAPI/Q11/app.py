from flask import Flask
from myapp.routes import myapp_blueprint

app = Flask(__name__)
app.register_blueprint(myapp_blueprint)

if __name__ == "__main__":
    app.run(debug=True)

