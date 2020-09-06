import sqlite3
from flask import Flask,g

app = Flask(__name__)

DATABASE = './census.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    return db

def index():
    rtn = ""
    cur = get_db().cursor()
    for row in cur.execute('SELECT * FROM people LIMIT 10'):
        print(row)
    return "Worked?"

index()

