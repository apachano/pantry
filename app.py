from flask import Flask, request
from database import get_connection
from item import Item

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
    if not data: return 'json expected', 400
    if not data.get('name'): return 'name required', 400
    
    item = Item(json=data)
    
    cur.execute(f"INSERT INTO pantry_items {item.sql_list} VALUES {item.sql_values} RETURNING *;")
    return cur.fetchall()

@app.put("/items/<id>")
def updateItem(id):
    data = request.json
    if not data: return 'json expected', 400

    item = Item(json=data)
    
    cur.execute(f"UPDATE pantry_items SET {item.sql_list} = {item.sql_values} WHERE id = {id}")
    return cur.fetchall()

@app.delete("/items/<id>")
def deleteItem(id):
    cur.execute(f"DELETE FROM pantry_items WHERE id = {id};")
    return cur.fetchall()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)