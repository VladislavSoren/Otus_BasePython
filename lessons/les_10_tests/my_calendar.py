"""
Since you’re testing if today is a weekday, the result depends on the day you run your test:

When writing tests, it is important to ensure that the results are predictable.
You can use Mock to eliminate uncertainty from your code during testing.
In this case, you can mock datetime and set the .return_value for .today() to a day that you choose!
"""

import datetime
import unittest
from unittest.mock import Mock
import requests
from requests.exceptions import Timeout

# Save a couple of test days
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

# Mock datetime to control today's date
datetime = Mock()


def is_weekday():
    today = datetime.datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return 0 <= today.weekday() < 5


# Mock .today() to return Tuesday
datetime.datetime.today.return_value = tuesday
# Test Tuesday is a weekday
assert is_weekday()
# Mock .today() to return Saturday
datetime.datetime.today.return_value = saturday
# Test Saturday is not a weekday
assert not is_weekday()


# Managing a Mock’s Side Effects
## Mock requests to control its behavior
requests = Mock()

def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None

# In default here will ConnectionError!
# req = get_holidays()


class TestCalendar(unittest.TestCase):
    def test_get_holidays_timeout(self):
        # Test a connection timeout
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()


# # Configuring Your Mock
# mock = Mock(side_effect=Exception)
# # print(mock())
#
# mock = Mock(name='Real Python Mock')
# print(mock)
#
# mock = Mock(return_value=True)
# print(mock())
# mock.name = 'Real Python Mock'
# print(mock.name)
# print(mock)
# mock.configure_mock(name='My name')
# print(mock)

if __name__ == '__main__':
    unittest.main()

















