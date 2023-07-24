#!/usr/bin/python3
"""script that given employee ID, returns
    information about his/her TODO list progress
    The script must accept an integer as a parameter, which is the employee ID
    The script must display on the standard output the employee
    TODO list progress in this exact format:

    First line: Employee EMPLOYEE_NAME is done with tasks
    (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
        EMPLOYEE_NAME: name of the employee
        NUMBER_OF_DONE_TASKS: number of completed tasks
        TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the
        sum of completed and non-completed tasks
    Second and N next lines display the title of completed tasks:
    TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""
import requests
from sys import argv


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com"
    todo_url = "{}/todos?userId={}".format(url, int(argv[1]))
    user_url = "{}/users/{}".format(url, int(argv[1]))

    user_response = requests.get(user_url)
    user_data = user_response.json()
    EMPLOYEE_NAME = user_data["name"]

    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()
    TOTAL_NUMBER_OF_TASKS = len(todo_data)

    count = 0
    for i in todo_data:
        if i["completed"]:
            count += 1
    NUMBER_OF_DONE_TASKS = count
    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for i in todo_data:
        if i["completed"]:
            print("\t", i["title"])
