#!/usr/bin/python3
"""
Script that exports data in CSV format for a given employee ID.

Usage: ./export_to_csv.py <employee id>
"""

import csv
import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com/"

def export_to_csv(employee_id):
    """
    Export data in CSV format for a given employee ID.

    Args:
        employee_id (int): The employee ID.

    Returns:
        None
    """
    employee = requests.get(API_URL + "users/{}".format(employee_id)).json()

    todo_list = requests.get("{}todos?userId={}".format(API_URL,
                                                        employee_id)).json()

    with open("{}.csv".format(employee_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        writer.writerow(["Employee ID", "Username", "Completed", "Title"])

        for task in todo_list:
            writer.writerow([
                employee_id,
                employee.get("username", ""),
                task.get("completed", ""),
                task.get("title", "")
            ])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./export_to_csv.py <employee id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    export_to_csv(int(employee_id))

