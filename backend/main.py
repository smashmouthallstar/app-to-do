from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get('/get_tasks')

def get_tasks():
    with sqlite3.connect("./todos.db") as conn:
        query = conn.execute("SELECT * FROM todos;")
        result = query.fetchall()

        response = []
        for todo in result:
            todo_json = {
                'id' : todo[0],
                'todo': todo[1]

            }
            response.append(todo_json)
        return response