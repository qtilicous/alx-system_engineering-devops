#!/usr/bin/python3
"""
Export data to CSV format
"""
import csv
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

    file_name = "{}.csv".format(user_id)

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([user_id,
                             user_info.get('username'),
                             todo.get('completed'),
                             todo.get('title')])
