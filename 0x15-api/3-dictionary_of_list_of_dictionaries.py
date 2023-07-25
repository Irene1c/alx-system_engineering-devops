#!/usr/bin/python3
"""script to export data in the JSON format
    Records all tasks from all employees
    Format: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task":
    "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID":
    [ {"username": "USERNAME", "task": "TASK_TITLE", "completed":
    TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task":
    "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
    File name must be: todo_all_employees.json
"""
import json
import requests


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com"
    todo_url = "{}/todos".format(url)
    user_url = "{}/users".format(url)

    user_response = requests.get(user_url)
    user_data = user_response.json()

    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    filename = "todo_all_employees.json"
    with open(filename, "w", encoding="utf-8") as file:
        data = {}

        for user in user_data:
            USER_ID = user["id"]
            USERNAME = user["username"]
            data[USER_ID] = []

            for todo in todo_data:
                if todo["userId"] == USER_ID:
                    TASK_COMPLETED_STATUS = todo["completed"]
                    TASK_TITLE = todo["title"]
                    a_dict = {
                        "username": USERNAME,
                        "task": TASK_TITLE,
                        "completed": TASK_COMPLETED_STATUS
                    }
                    data[USER_ID].append(a_dict)

        json.dump(data, file)
