#!/usr/bin/python3
"""
    Records all tasks that are owned by an employee in a csv file.
"""
from requests import get
from csv import DictWriter, QUOTE_ALL
from sys import argv


if len(argv) != 2:
    print("Usage: {} <id>".format(argv[0]))
    exit(1)

id = argv[1]
user = get("https://jsonplaceholder.typicode.com/users/{}".format(id)).json()
todos = get("https://jsonplaceholder.typicode.com/todos/?userId={}".format(id))
todos = todos.json()
for i in todos:
    i['username'] = user['username']

with open(f"{id}.csv", mode="w", newline="") as file:
    fields = ['userId', 'username', 'completed', 'title']
    csv_writer = DictWriter(file, fieldnames=fields,
                            quotechar='"', quoting=QUOTE_ALL)
    for row in todos:
        r = {k: v for k, v in row.items() if k in fields}
        csv_writer.writerow(r)
