import json
from flask import Blueprint, render_template
from . import create_app


blueprint = Blueprint("app", __name__)

# app = create_app()

@blueprint.route('/')
def home():
    return render_template('home.html')

@blueprint.route('/directors_profile')
def directors_profile():
    return render_template('directors_profile.html')

@blueprint.route('/verticals')
def verticals():
    return render_template('verticals.html')

@blueprint.route('/vision')
def vision():
    return render_template('vision.html')

@blueprint.route('/people')
def people():

    with open("app\static\json_files\people.json", "r") as content:
        people_data = json.load(content)
    return render_template("people.html", people=people_data)

@blueprint.route('/research')
def research():
    return render_template('research.html')

@blueprint.route('/dia_coes')
def dia_coes():
    return render_template('dia_coes.html')

@blueprint.route('/forms')
def forms():
    return render_template('forms.html')

@blueprint.route('/achievements')
def achievements():
    return render_template('achievements.html')

@blueprint.route('/projects')
def projects():
    return render_template('projects.html')


@blueprint.route('/contact')
def contact():
    return render_template('contact.html')

@blueprint.route('/important_links')
def important_links():
    return render_template('important_links.html')