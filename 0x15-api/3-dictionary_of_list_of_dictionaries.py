#!/usr/bin/python3
"""
    Records all tasks of all employees from a REST API.
"""
from requests import get
import json


users = get("https://jsonplaceholder.typicode.com/users/").json()
full_list = dict()
for usr in users:
    todos = get("https://jsonplaceholder.typicode.com/todos/?userId={}".format(
                usr.get("id"))).json()
    usr_todos = list()
    for l in todos:
        d = dict()
        d['username'] = usr.get('username')
        for k, v in l.items():
            if k in ['title', 'completed']:
                d[k] = v
        usr_todos.append(d)
    full_list.update({str(usr.get("id")): usr_todos})

with open("todo_all_employees.json", mode="w", newline="") as file:
    json.dump(full_list, file)
