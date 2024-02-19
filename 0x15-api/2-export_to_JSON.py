#!/usr/bin/python3
"""
Export data to JSON format
"""
import json
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

    data = {user_id: []}

    for todo in todos:
        task_data = {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": user_info.get('username')
        }
        data[user_id].append(task_data)

    file_name = "{}.json".format(user_id)

    with open(file_name, mode='w') as file:
        json.dump(data, file)
