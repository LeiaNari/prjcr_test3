from flask import Flask, jsonify, request

app = Flask(__name__)

employee_data = [
    {"id": 1, "name": "John Doe", "birthday": "Apr 18", "department": "HR"},
    {"id": 2, "name": "Alice Smith", "birthday": "Apr 5", "department": "Engineering"},
    {"id": 3, "name": "Bob Johnson", "birthday": "May 10", "department": "HR"},
    {"id": 4, "name": "Emma Brown", "birthday": "Apr 30", "department": "Engineering"}
]


def filter_employees_by_month_and_department(month, department):
    return [employee for employee in employee_data if
            employee['birthday'].split()[0] == month and employee['department'] == department]


@app.route('/birthdays')
def get_birthdays():
    month = request.args.get('month')
    department = request.args.get('department')
    employees = filter_employees_by_month_and_department(month, department)
    return jsonify({'total': len(employees), 'employees': employees})


@app.route('/anniversaries')
def get_anniversaries():
    month = request.args.get('month')
    department = request.args.get('department')
    employees = filter_employees_by_month_and_department(month, department)
    return jsonify({'total': len(employees), 'employees': employees})


if __name__ == '__main__':
    app.run(debug=True)
