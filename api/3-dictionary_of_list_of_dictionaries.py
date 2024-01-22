#!/usr/bin/python3
"""
Script that exports data for all employees in JSON format.

Usage: ./export_all_to_json.py
"""

import json
import requests

API_URL = "https://jsonplaceholder.typicode.com/"


def export_all_to_json():
    """
    Export data for all employees in JSON format.

    Returns:
        None
    """
    employees = requests.get('{}users'.format(API_URL)).json()
    todos_list = requests.get("{}todos".format(API_URL)).json()

    all_employees_data = {}

    for employee in employees:
        user_id = employee.get("id")
        username = employee.get("username")

        employee_tasks = [
            {
                "username": username,
                "task": task["title"],
                "completed": task["completed"],
            }
            for task in todos_list if task["userId"] == user_id
        ]
        all_employees_data[user_id] = employee_tasks

    json_file_name = "todo_all_employees.json"

    with open(json_file_name, "w") as json_file:
        json.dump(all_employees_data, json_file, indent=2)


if __name__ == "__main__":
    export_all_to_json()
