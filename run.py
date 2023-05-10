from dotenv import load_dotenv

from jirnich import create_app

load_dotenv()
app = create_app()


if __name__ == '__main__':
    # Manager из flask-script не работает, ебанул напрямик, костыль.
    app.run(debug=True)
