import unittest
from unittest.mock import patch
from server import filter_employees_by_month_and_department, app


class TestServer(unittest.TestCase):

    def test_filter_employees_by_month_and_department_success(self):
        month = 'Apr'
        department = 'Engineering'
        expected_result = [
            {"id": 2, "name": "Alice Smith", "birthday": "Apr 5", "department": "Engineering"},
            {"id": 4, "name": "Emma Brown", "birthday": "Apr 30", "department": "Engineering"}
        ]
        result = filter_employees_by_month_and_department(month, department)
        self.assertEqual(result, expected_result)

    @patch('server.request')
    def test_get_birthdays_success(self, mock_request):
        mock_request.args.get.return_value = 'Apr'
        response = app.test_client().get('/birthdays')
        data = response.get_json()
        self.assertEqual(data['total'], 2)
        self.assertEqual(len(data['employees']), 2)
        self.assertEqual(response.status_code, 200)

    @patch('server.request')
    def test_get_birthdays_incorrect_inputs(self, mock_request):
        mock_request.args.get.return_value = None
        response = app.test_client().get('/birthdays')
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()

