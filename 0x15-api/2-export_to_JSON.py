#!/usr/bin/python3
"""script to export data in the JSON format
    Records all tasks that are owned by this employee
    Format: { "USER_ID": [{"task": "TASK_TITLE", "completed":
    TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task":
    "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"}, ... ]}
    File name must be: USER_ID.json
"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com"
    todo_url = "{}/todos?userId={}".format(url, int(argv[1]))
    user_url = "{}/users/{}".format(url, int(argv[1]))

    user_response = requests.get(user_url)
    user_data = user_response.json()

    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    filename = f"{int(argv[1])}.json"
    with open(filename, "w", encoding="utf-8") as file:
        data = {}
        USER_ID = int(argv[1])
        data[USER_ID] = []

        USERNAME = user_data["username"]
        for todo in todo_data:
            TASK_COMPLETED_STATUS = todo["completed"]
            TASK_TITLE = todo["title"]
            a_dict = {
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            }
            data[USER_ID].append(a_dict)

        json.dump(data, file)
