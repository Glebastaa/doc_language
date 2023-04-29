from flask import Blueprint, render_template


users = Blueprint('users', __name__)


@users.route('/signup')
def signup():
    "Отрисовывает форму регистрации"
    pass