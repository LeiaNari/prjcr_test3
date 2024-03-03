import csv
from faker import Faker
import random

fake = Faker()


def generate_employee_data(num_records):
    data = []
    departments = ['HR', 'Finance', 'Marketing', 'IT', 'Operations']

    for _ in range(num_records):
        name = fake.name()
        hiring_date = fake.date_this_decade()
        birthday = fake.date_of_birth(minimum_age=20, maximum_age=60)
        department = random.choice(departments)
        data.append([name, hiring_date, birthday, department])

    return data


def write_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Hiring Date', 'Birthday', 'Department'])
        writer.writerows(data)


employee_data = generate_employee_data(100)

write_to_csv(employee_data, 'database.csv')
