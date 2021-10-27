#import psycopg2
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, g, request, jsonify
#from flask_cors import CORS


app = Flask(__name__)
#CORS(app)

conn = psycopg2.connect(
     host="localhost",
     database="people",
     user="postgres",
     password="Password")

@app.route('/getCounties', methods=['POST'])
def getCounties():
    st = request.json["county"]
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT CountyID, County, State FROM people WHERE County Like '{}%' LIMIT 5".format(st))
    return jsonify(cur.fetchall())

@app.route('/getCounty', methods=['POST'])
def getCounty():
    st = request.json["ID"]
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT  * FROM people WHERE CountyId like '{}'".format(st))
    return jsonify(cur.fetchall())

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()