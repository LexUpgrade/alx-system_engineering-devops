#!/usr/bin/python3
"""
    Records all tasks that are owned by an employee in a json file from a
    REST API.
"""
from requests import get
from sys import argv
import json

if len(argv) != 2:
    print("Usage: {} <id>".format(agv[0]))
    exit(1)

id = argv[1]
user = get(f"https://jsonplaceholder.typicode.com/users/{id}").json()
todos = get(f"https://jsonplaceholder.typicode.com/todos/?userId={id}").json()

new = list()
for i in todos:
    r = {}
    for j in ["title", "completed"]:
        r[j] = i[j]
    r['username'] = user['username']
    new.append(r)

fields = ["task", "completed", "username"]
new_list = list()
for v in new:
    new_list.append(dict(zip(fields, v.values())))
dictionary = {id: new_list}

with open(f"{id}.json", mode="w", newline="") as file:
    json.dump(dictionary, file)
