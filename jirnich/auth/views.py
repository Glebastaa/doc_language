from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user

from jirnich.auth.forms import (ForgotPasswordForm, LoginForm, PasswordForm,
                                SignUpForm)
from jirnich.database import db
from jirnich.models import User
from jirnich.utils import send_mail, verify_reset_token

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    """Отрисовывает форму для входа."""
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


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    """Отрисовывает форму регистрации."""
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(
                email=form.email.data,
                username=form.username.data
                )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=form.remember.data)
        return redirect(url_for('main.index'))

    return render_template('auth/signup.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Вы разлогинились!")
    return redirect(url_for('main.index'))


@auth.route('/reset', methods=['POST', 'GET'])
def reset_password():
    """Отрисовывает форму с почтой для сброса пароля."""
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first_or_404()
        subject = "Сброс пароля на сайте Жирнич"
        token = user.get_reset_token()
        recover_url = url_for(
            'auth.reset_with_token',
            token=token,
            _external=True
        )
        send_mail(
            subject,
            user.email,
            'email/recover.html',
            recover_url=recover_url
        )
        flash('Письмо для сброса пароля отправлено')
        return redirect(url_for('main.index'))
    return render_template('auth/reset.html', form=form)


@auth.route('/reset/<token>', methods=['POST', 'GET'])
def reset_with_token(token):
    user = verify_reset_token(token)
    form = PasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template(
        'auth/reset_with_token.html',
        form=form,
        token=token
    )
