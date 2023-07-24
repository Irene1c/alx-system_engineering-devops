#!/usr/bin/python3
"""Python script to export data in the CSV format
    Records all tasks that are owned by this employee
    Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv
"""
import csv
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

    filename = f"{int(argv[1])}.csv"
    with open(filename, mode="w", newline="") as file:
        fieldnames = ["userId", "username", "completed", "title"]
        writer = csv.DictWriter(
                file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

        USERNAME = user_data["username"]

        for todo in todo_data:
            USER_ID = int(argv[1])
            TASK_COMPLETED_STATUS = todo["completed"]
            TASK_TITLE = todo["title"]
            writer.writerow(
                    {"userId": USER_ID, "username": USERNAME,
                     "completed": TASK_COMPLETED_STATUS, "title": TASK_TITLE})
