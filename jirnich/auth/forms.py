from flask_wtf import FlaskForm
from wtforms import (BooleanField, EmailField, PasswordField, StringField,
                     SubmitField)
from wtforms.validators import DataRequired, Email, EqualTo, Length

from jirnich.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField()


class SignUpForm(FlaskForm):
    email = EmailField(
        'Email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6)]
    )
    confirm = PasswordField(
        'Repeat password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match')
        ]
    )
    remember = BooleanField('Remember Me')
    submit = SubmitField()

    # Переопределяем валидацию и добавляем новые проверки.
    def validate(self, extra_validators=None):
        initial_validation = super(SignUpForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append('Почта уже зарегистрирована!')
            return False
        if self.password.data != self.confirm.data:
            self.password.errors.append('Пароли не совпадают!')
            return False
        return True
