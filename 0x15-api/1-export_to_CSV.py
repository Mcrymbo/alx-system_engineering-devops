#!/usr/bin/python3
"""
Python script, using REST API for employee ID
and return returns information about his/her TODO list progress
"""
import requests
import sys
import csv


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
        tasks.append([user_id,
                      username,
                      task.get('completed'),
                      task.get('title')])

    filename = '{}.csv'.format(user_id)
    with open(filename, 'w') as f:
        data = csv.writer(f, delimiter=',',
                          quotechar='"',
                          quoting=csv.QUOTE_ALL)

        for task in tasks:
            data.writerow(task)
