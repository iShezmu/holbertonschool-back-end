#!/usr/bin/python3
"""
Script that exports data in JSON format for a given employee ID.

Usage: ./export_to_json.py <employee id>
"""

import json
import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com/"


def export_to_json(employee_id):
    """
    Export data in JSON format for a given employee ID.

    Args:
        employee_id (int): The employee ID.

    Returns:
        None
    """
    employee = requests.get(API_URL + "users/{}".format(employee_id)).json()

    todo_list = requests.get("{}todos?userId={}".format(API_URL,
                                                        employee_id)).json()

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump({employee_id: [{
            "task": task.get("title", ""),
            "completed": task.get("completed", ""),
            "username": employee.get("username", "")
        } for task in todo_list]}, json_file, indent=2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./export_to_json.py <employee id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    export_to_json(int(employee_id))
