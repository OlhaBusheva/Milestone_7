from flask import Flask, jsonify, request
import csv
from datetime import datetime

app = Flask(__name__)


def load_data():
    with open("database.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        DB = list(reader)
    return DB


def birthday_employees(DB, month, department):
    filtered_employees = []
    for employee in DB:
        if employee['department'] == department:
            birthday = datetime.strptime(employee['birthday'], "%Y-%m-%d")
            if birthday.month == month:
                filtered_employees.append({
                    "id": employee['id'],
                    "name": employee['name'],
                    "birthday": birthday.strftime("%b %d")
                })
    return filtered_employees


def hiring_employees(DB, month, department):
    filtered_employees = []
    for employee in DB:
        if employee['department'] == department:
            hiring_date = datetime.strptime(
                employee['hiring_date'], "%Y-%m-%d"
                )
            if hiring_date.month == month:
                filtered_employees.append({
                    "id": employee['id'],
                    "name": employee['name'],
                    "hiring_date": hiring_date.strftime("%b %d")
                })
    return filtered_employees


@app.route('/birthdays', methods=['GET'])
def get_birthdays():
    month = int(request.args.get('month'))
    department = request.args.get('department')
    DB = load_data()
    filtered_employees = birthday_employees(DB, month, department)
    response = {
        "total": len(filtered_employees),
        "employees": filtered_employees
    }
    return jsonify(response)


@app.route('/anniversaries', methods=['GET'])
def get_anniversaries():
    month = int(request.args.get('month'))
    department = request.args.get('department')
    DB = load_data()
    filtered_employees = hiring_employees(DB, month, department)
    response = {
        "total": len(filtered_employees),
        "employees": filtered_employees
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
