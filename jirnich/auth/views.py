from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import login_required, login_user

from jirnich.database import db
from jirnich.models import User
from .forms import LoginForm


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    "Отрисовывает форму для входа"
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(
            User.username == form.username.data
        ).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.index'))
        
        flash("Неправильный логин/пароль", 'error')
        return redirect(url_for('auth.login'))
    return render_template('auth/login.html', form=form)

@auth.route('/signup')
def signup():
    "Отрисовывает форму регистрации"
    return render_template('auth/signup.html')

@auth.route('/logout')
@login_required
def logout():
    return 'logout'