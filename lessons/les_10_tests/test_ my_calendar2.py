"""
We also can use patch() as a Context Manager
Example:
    https://realpython.com/python-mock-library/



"""

import unittest
from my_calendar2 import get_holidays
from requests.exceptions import Timeout
from unittest import mock

class TestCalendar(unittest.TestCase):
    @mock.patch('my_calendar2.requests')
    def test_get_holidays_timeout(self, mock_requests):
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()

if __name__ == '__main__':
    unittest.main()