import os
from threading import Thread

from flask import abort, current_app, render_template
from flask_mail import Message
from jwt import decode

from jirnich.models import User


def async_send_mail(app, msg):
    from jirnich import mail
    with app.app_context():
        mail.send(msg)


def send_mail(subject, recipient, template, **kwargs):
    msg = Message(
        subject,
        sender=current_app.config['MAIL_DEFAULT_SENDER'],
        recipients=[recipient]
    )
    msg.html = render_template(template, **kwargs)
    thr = Thread(
        target=async_send_mail,
        args=[current_app._get_current_object(), msg]
    )
    thr.start()
    return thr


def verify_reset_token(token):
    try:
        username = decode(
            token,
            key=os.getenv('SECRET_KEY'),
            algorithms=["HS256"]
        )['reset_password']
    except Exception as error:
        print(error)
        abort(404)
    return User.query.filter_by(username=username).first()
