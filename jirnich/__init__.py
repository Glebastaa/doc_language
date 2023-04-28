from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Функция для создания соединения с базой данных
def get_db_conn():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="testdb",
        user="postgres",
        password="mypassword"
    )

# Маршрут для вывода "Hello"
@app.route('/')
def hello():
    return "Hello"

# Маршрут для получения списка элементов из базы данных
@app.route('/items')
def get_items():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM items")
    rows = cur.fetchall()
    items = [{'id': row[0], 'text': row[1]} for row in rows]
    cur.close()
    conn.close()
    return jsonify(items)

if __name__ == '__main__':
    app.run()