#!/usr/bin/python3
"""
Python script, using REST API for employee ID
and return returns information about his/her TODO list progress
"""
import json
import requests
import sys


if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]
    user = '{}users/{}'.format(base_url, user_id)
    user_res = requests.get(user)
    user_obj = user_res.json()
    username = user_obj.get('username')

    todos = '{}todos?userId={}'.format(base_url, user_id)
    todo_res = requests.get(todos)
    todo_obj = todo_res.json()

    tasks = []
    for task in todo_obj:
        task_json = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": username}
        tasks.append(task_json)

    task = {str(user_id): tasks}
    filename = '{}.json'.format(user_id)
    with open(filename, 'w') as f:
        json.dump(task, f)
