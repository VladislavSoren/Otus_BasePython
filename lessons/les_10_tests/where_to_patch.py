"""
Notice that even though the target location you passed to patch() did not change,
the result of calling is_weekday() is different.
The difference is due to the change in how you imported the function.

A good rule of thumb is to patch() the object where it is looked up!
"""

# import my_calendar2
# from unittest.mock import patch
#
# with patch('my_calendar2.is_weekday'):
#     print(my_calendar2.is_weekday())


from my_calendar2 import is_weekday
from unittest.mock import patch

with patch('my_calendar2.is_weekday'):
    print(is_weekday())