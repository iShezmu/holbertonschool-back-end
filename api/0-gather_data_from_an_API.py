#!/usr/bin/python3
"""
Script that returns 'to-do list' info for a given employee ID.

Usage: ./0-gather_data_from_an_API.py <employee id>
"""

import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com/"


def gather_data(employee_id):
    """
    Gather and display 'to-do list' info for a given employee ID.

    Args:
        employee_id (int): The employee ID.

    Returns:
        None
    """
    employee = requests.get(API_URL + "users/{}".format(employee_id)).json()

    todo_list = requests.get("{}todos?userId={}".format(
        API_URL, employee_id)).json()

    completed_tasks = [task.get("title", "")
                       for task in todo_list if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name", ""), len(completed_tasks), len(todo_list)))

    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    gather_data(int(employee_id))
