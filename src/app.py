import sqlite3
from flask import Flask, render_template
import json

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('capstone.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM producto').fetchall()
    conn.close()
    return 'Hola a todos'

@app.route('/<code>', methods=('GET', 'POST'))
def get_product(code):
    conn = get_db_connection()
    query = "SELECT * FROM producto WHERE codigo = '" + code + "'" 
    print("Query ", query)
    product = conn.execute(query).fetchone()
    conn.close()
    print(product)
    return render_template('product.html', producto=product)