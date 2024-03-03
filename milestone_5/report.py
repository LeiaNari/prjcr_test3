import csv
from datetime import datetime


def read_csv(filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data


def filter_by_month(data, month):
    filtered_data = []
    for row in data:
        hiring_date = datetime.strptime(row['Hiring Date'], '%Y-%m-%d')
        if hiring_date.strftime('%B').lower() == month.lower():
            filtered_data.append(row)
    return filtered_data


def count_by_department(data):
    counts = {}
    for row in data:
        department = row['Department']
        counts[department] = counts.get(department, 0) + 1
    return counts


def print_report(month, birthdays, anniversaries):
    print(f"Report for {month.capitalize()} generated")

    print("--- Birthdays ---")
    print(f"Total: {sum(birthdays.values())}")
    for department, count in birthdays.items():
        print(f"- {department}: {count}")

    print("--- Anniversaries ---")
    print(f"Total: {sum(anniversaries.values())}")
    for department, count in anniversaries.items():
        print(f"- {department}: {count}")


def main(filename, month):
    data = read_csv(filename)
    filtered_data = filter_by_month(data, month)

    birthdays = count_by_department(filtered_data)
    anniversaries = count_by_department(filtered_data)

    print_report(month, birthdays, anniversaries)


main('database.csv', 'April')
