from flask import Flask, render_template

app = Flask(__name__)

kwargs = {
    "name": 'Kekeli',
    "template_name": 'Jinja2',
    "favorites": "games",
    "first_game": "Tomb Raider",
    "second_game": "Gears of War 5",
    "first_language": "Python",
    "second_language": "JavaScript",
    "first_interest": "Software Engineering",
    "second_interest":"Cloud DevOps"
}


@app.route('/')
def welcome():
    return render_template('index.html', **kwargs)
