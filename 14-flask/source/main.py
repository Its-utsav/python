from flask import Flask, request, jsonify, g
import sqlite3
from datetime import datetime
import random
import string


DBPATH = "todo.db"
app = Flask(__name__)


def connect_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DBPATH)

    return db


@app.teardown_appcontext
def close_db_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.route("/")
def home():
    try:
        cur = connect_db().cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS todo(
                todoid text primary key,
                todocontent text,
                time text,
                iscompelete number check(iscompelete in (0,1))
                );
            """
        )
        todo_len = cur.execute("""SELECT COUNT(todoid) FROM todo""").fetchone()
        return jsonify({"DB": "Table connected succesfully", "total todo": todo_len})
    except ConnectionRefusedError as e:
        return "unable to connect db", e


@app.route("/alltodo", methods=["GET"])
def all_todo():
    cur = connect_db().cursor()

    cur.execute("""SELECT todoid , todocontent ,time ,iscompelete FROM todo;""")
    name = request.args.get("name")
    todos = cur.fetchall()
    todos_lst = []
    for todo in todos:
        todos_lst.append(
            {
                "todoid": todo[0],
                "todocontent": todo[1],
                "time": todo[2],
                "status": "Pending" if todo[3] == 0 else "Done",
            }
        )

    return jsonify({"name": name, "todo": todos_lst})


@app.route("/createtodo", methods=["POST"])
def create_todo():
    req = request.get_json()
    time = datetime.now()
    con = connect_db()
    cur = con.cursor()
    todo_content = req["todo-content"]
    todo_id = "".join(random.sample(string.ascii_letters, 10))
    cur.execute(
        """
        INSERT INTO todo values(?,?,?,0)""",
        (todo_id, todo_content, time),
    )
    cur.execute("""SELECT * FROM todo WHERE todoid = ?""", (todo_id,))
    ans = cur.fetchall()
    con.commit()
    return jsonify({"Flag": "Task added", "todos": ans})


@app.route("/completetodo", methods=["POST"])
def completetodo():
    req = request.args.get("id")
    con = connect_db()
    cur = con.cursor()
    # find in db
    cur.execute("""SELECT todoid FROM todo WHERE todoid = ? """, (req,))
    todo = cur.fetchone()

    # if yes mark as 1
    if todo != None:
        cur.execute("""UPDATE todo SET iscompelete = 1 WHERE todoid = ?""", (req,))
        con.commit()
    else:
        # if not return task not found
        return jsonify({"msg": "Todo Not Found"})

    return jsonify({"msg": "Todo Updated"})


@app.route("/gettodoinfo", methods=["GET"])
def get_todo_info():
    req = request.args.get("id")
    con = connect_db()
    cur = con.cursor()
    # find in db
    cur.execute("""SELECT * FROM todo WHERE todoid = ? """, (req,))
    todo = cur.fetchone()

    # if yes return it
    if todo != None:
        return jsonify(
            {
                "todoid": todo[0],
                "todocontent": todo[1],
                "time": todo[2],
                "status": "Pending" if todo[3] == 0 else "Done",
            }
        )
    else:
        # if not return task not found
        return jsonify({"msg": "Todo Not Found"})


if __name__ == "__main__":
    app.run(debug=True)
