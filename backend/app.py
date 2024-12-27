from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname="gaming_deals",
        user="postgres",
        password="admin",
        host="localhost"
    )
    return conn

@app.route('/deals', methods=['GET'])
def get_deals():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM deals;')
    deals = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(deals)

if __name__ == '__main__':
    app.run(debug=True)
