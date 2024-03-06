import requests
import argparse
import calendar

parser = argparse.ArgumentParser(description='Information for monthly report')
parser.add_argument("month", type=str, help="Enter month")
parser.add_argument("department_name", type=str, help="Enter department")
args = parser.parse_args()
month_enter = args.month
month_name = month_enter.capitalize()
month = list(calendar.month_name).index(month_name)
department = args.department_name


def fetch1_report(month, department):
    url = (f"http://localhost:5000/birthdays?"
           f"month={month}&department={department}")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Report for {department} department for {month_name} fetched.")
        print(f"Total: {data['total']}")
        print("Employees:")
        for emp in data['employees']:
            print(f"- {emp['birthday']}, {emp['name']}")
    else:
        print(f"Failed to fetch report for {department} department for {month}"
              f"Error: {response.text}")


def fetch2_report(month, department):
    url = (f"http://localhost:5000/anniversaries?"
           f"month={month}&department={department}")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Report for {department} department for {month_name} fetched.")
        print(f"Total: {data['total']}")
        print("Employees:")
        for emp in data['employees']:
            print(f"- {emp['hiring_date']}, {emp['name']}")
    else:
        print(f"Failed to fetch report for {department} department for {month}"
              f"Error: {response.text}")


if __name__ == "__main__":
    fetch1_report(month, department)
    fetch2_report(month, department)
