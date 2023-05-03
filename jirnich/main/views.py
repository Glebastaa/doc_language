from flask import Blueprint, redirect, render_template, request
from googletrans import Translator

from jirnich.database import db
from jirnich.models import Text

main = Blueprint('main', __name__)


@main.route('/')
def index():
    """Главная страница."""
    text_obj = Text.query.first()
    return render_template('index.html', text_obj=text_obj)


@main.route('/create', methods=['POST', 'GET'])
def create():
    """Тестовая страница на добавление текста в базу."""
    if request.method == 'POST':
        text = request.form['text']
        txt = Text(text=text)
        try:
            db.session.add(txt)
            db.session.commit()
            return redirect('/')
        except Exception:
            return 'Ошибка!!!'

    return render_template('create.html')


@main.route('/translate')
def translate():
    text = request.args.get('text')
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='ru').text
    return translated_text