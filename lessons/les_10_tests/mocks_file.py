from unittest.mock import Mock

# Create a mock object
json = Mock()

# Вызовы метода
json.loads('{"key": "value"}')
json.loads('{"key": "value"}')


# Проверки на вызовы
# json.loads.assert_not_called()
json.loads.assert_called()
# json.loads.assert_called_once()
# json.loads.assert_called_with('{"key": "value"} {"key": "value"}')


#  you can view special attributes
# Number of times you called loads():
print(json.loads.call_count)

# The last loads() call:
print(json.loads.call_args)

# List of loads() calls:
print(json.loads.call_args_list)

# List of calls to json's methods (recursively):
print(json.method_calls)


# Managing a Mock’s Return Value





