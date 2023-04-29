from flask import Blueprint, render_template


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    "Отрисовывает форму для входа"
    return 'login'

@auth.route('/signup')
def signup():
    "Отрисовывает форму регистрации"
    return 'signup'

@auth.route('/logout')
def logout():
    return 'logout'