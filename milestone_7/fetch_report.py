import requests


def fetch_report(month, department):
    response = requests.get(f"http://localhost:5000/birthdays?month={month}&department={department}")
    report = response.json()
    print(f"Report for {department} department for {month} fetched.")
    print(f"Total: {report['total']}")
    print("Employees:")
    for employee in report['employees']:
        print(f"- {employee['birthday']}, {employee['name']}")


if __name__ == "__main__":
    fetch_report("April", "Engineering")
