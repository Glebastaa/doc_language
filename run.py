import os

from jirnich import create_app


app = create_app()
app.config.from_object(os.environ['APP_SETTINGS'])

if __name__ == '__main__':
    #Manager из flask-script не работает, ебанул напрямик, костыль.
    app.run(debug=True)