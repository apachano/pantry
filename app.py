from flask import Flask, request
import psycopg2

app = Flask(__name__)

# Connect to your postgres DB
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="salamander")

# Open a cursor to perform database operations
cur = conn.cursor()

@app.get("/items")
def getItems():
    cur.execute("SELECT * FROM pantry_items;")
    return cur.fetchall()

@app.get("/items/<id>")
def getItem(id):
    cur.execute(f"SELECT * FROM pantry_items WHERE id = {id};")
    return cur.fetchall()

@app.post("/items")
def postItem():
    data = request.json
    cur.execute(f"INSERT INTO pantry_items (name, description, expiration) VALUES ('{data.get('name')}','{data.get('description')}','{data.get('expiration')}') RETURNING *;")
    item = cur.fetchall()
    return item

@app.delete("/items/<id>")
def deleteItem():
    cur.execute(f"DELETE FROM pantry_items WHERE id = {id};")
    return cur.fetchall()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"