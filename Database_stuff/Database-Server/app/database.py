#import psycopg2
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, g, request, jsonify
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)

conn = ""
if os.environ['DATABASE_URL']:
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
else:    
    conn = psycopg2.connect(
        host="localhost",
        database="People",
        user="postgres",
        password="password")

@app.route('/getCounties', methods=['POST'])
def getCounties():
    st = request.form["county"]
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT CountyID, County, State FROM people WHERE County Like '{}%' LIMIT 5".format(st))
    return jsonify(cur.fetchall())

@app.route('/getCounty', methods=['POST'])
def getCounty():
    st = request.form["ID"]
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT  * FROM people WHERE CountyId = '{}'".format(st))
    return jsonify(cur.fetchall())

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()