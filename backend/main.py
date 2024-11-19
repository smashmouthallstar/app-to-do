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

@app.get('/create_tasks')
def create_tasks(todo: str):
    with sqlite3.connect('./todos.db') as conn:
        try:
            query = conn.execute("INSERT INTO todos (todo) VALUES (?)", (todo,)) #we don't want + todo) concatenation because of errors & sequel injection via ; statements
            return True
        except:
            return "Error"

@app.get('/delete_task')
def delete_task(id: int): #id is string by default
    with sqlite3.connect('./todos.db') as conn:
        try:
            query = conn.execute('DELETE FROM todos WHERE id=?', (id,))
            return True
        except:
            return "Error"
"""
notes for myself
>>sql tags & joins
>unique ids
1 "todo"
2 "todo"
3 "HW"

>tags
tags
colid colname coltodoid(foreignkey)
1 work 3 #tells these are the same thing
2 demo 2
3 demo 1

so SELECT FROM TODO JOIN tags WHERE tags.todo.id
take all from todolist & everything from tags table,
output the data as if the data was merged
format so that all tags with todoid(foreignkey) match.

use cases: anytime we want to store a list of something.
-we have a user table & post table like twitter

user
1

postid
1

refresh and you get SELECT FROM POSTID WHERE tags.user.id for example




### refresh on what sql is
### remember this is sql joins, refresh on what sql joins is
### refresh on database types?
"""