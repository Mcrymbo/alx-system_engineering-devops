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

    user = '{}users'.format(base_url)
    user_res = requests.get(user)
    user_obj = user_res.json()

    task_d = {}
    for user in user_obj:
        username = user.get('username')
        userid = user.get('id')
        todos = '{}todos?userId={}'.format(base_url, userid)
        todo_res = requests.get(todos)
        todo_obj = todo_res.json()

        tasks = []
        for task in todo_obj:
            task_json = {"username": username, "task": task.get('title'),
                         "completed": task.get('completed')}
            tasks.append(task_json)

        task_d[str(userid)] = tasks
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as f:
        json.dump(task_d, f)
