from flask import Flask, request
from database import get_connection

app = Flask(__name__)
cur = get_connection()

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

if __name__ == "__main__":
    app.run(debug=True)