#!/usr/bin/python3
"""
Python script, using REST API for employee ID
and return returns information about his/her TODO list progress
"""
import requests
import sys


if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(base_url, sys.argv[1])
    user_res = requests.get(user)
    user_obj = user_res.json()
    print('Employee {} is done with tasks'
          .format(user_obj.get('name')), end='')

    todos = '{}todos?userId={}'.format(base_url, sys.argv[1])
    todo_res = requests.get(todos)
    todo_obj = todo_res.json()

    tasks = []
    for task in todo_obj:
        if task.get('completed') is True:
            tasks.append(task)

    print('({}/{}):'.format(len(tasks), len(todo_obj)))
    for task in todo_obj:
        print('\t {}'.format(task.get('title')))
