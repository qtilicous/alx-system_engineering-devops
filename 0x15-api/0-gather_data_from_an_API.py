#!/usr/bin/python3
"""
Gathers data from an API
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        exit()

    user_id = int(argv[1])
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    response = requests.get(url)
    user_response = requests.get(user_url)

    todos = response.json()
    user_info = user_response.json()

    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get('completed')]

    print("Employee {} is done with tasks({}/{}):".format(
        user_info.get('name'), len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
