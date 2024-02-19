#!/usr/bin/python3
"""
Script to export data in JSON format from all employees.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    users = response.json()

    user_dict = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')

        response = requests.get('{}/todos?userId={}'.format(url, user_id))
        tasks = response.json()

        user_tasks = []
        for task in tasks:
            task_info = {
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed'),
            }
            user_tasks.append(task_info)

        user_dict[str(user_id)] = user_tasks

    with open('todo_all_employees.json', 'w') as file:
        json.dump(user_dict, file)
