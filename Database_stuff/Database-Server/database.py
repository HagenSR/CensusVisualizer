import sqlite3
import json
from flask import Flask, g, request
import sys
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

DATABASE = './census.db'

@app.route('/getCounties', methods=['POST'])
def getCounties():
    st = request.json["county"]
    var = "SELECT CountyID, County, State FROM people WHERE County Like '{}%' LIMIT 5".format(st)
    return json.dumps(query_db(var))

@app.route('/getCounty', methods=['POST'])
def getCounty():
    st = request.json["ID"]
    var = "SELECT * FROM people WHERE CountyId like '{}'".format(st)
    return json.dumps(query_db(var))

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = make_dicts
    return db        

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv
    
