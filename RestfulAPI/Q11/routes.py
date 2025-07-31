from flask import Blueprint, render_template

myapp_blueprint = Blueprint('myapp', __name__)

@myapp_blueprint.route('/')
def home():
    return render_template("home.html")
