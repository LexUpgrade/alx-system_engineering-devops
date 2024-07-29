#!/usr/bin/python3
"""
    Prints information about an employee from a REST API, for a given ID
    passed as argument.
"""
from requests import get
from sys import argv

if len(argv) != 2:
    print("Usage: {} <id>".format(argv[0]))
    exit(1)

id = argv[1]
employee_name = get(f"https://jsonplaceholder.typicode.com/users/{id}")\
                    .json()['name']
todos = get(f"https://jsonplaceholder.typicode.com/todos/?userId={id}").json()
number_of_done_tasks = 0
number_of_done_tasks = sum(1 for i in todos if i.get("completed"))
total_number_of_tasks = len(todos)

print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                      number_of_done_tasks,
                                                      total_number_of_tasks))
[print("\t {}".format(don['title'])) for don in todos if don.get('completed')]
