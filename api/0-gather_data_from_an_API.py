#!/usr/bin/python3
"""
Module to fetch and display TODO list progress for a given employee ID
using the JSONPlaceholder REST API.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee info
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200 or not user_response.json():
        print("Employee not found.")
        sys.exit(1)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch employee TODO list
    todos_response = requests.get(f"{base_url}/todos", params={"userId": employee_id})
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Print results in exact required format
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

