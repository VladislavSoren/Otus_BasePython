from unittest.mock import Mock

# Create a mock object
json = Mock()

json.loads('{"key": "value"}')


# You know that you called loads() so you can
# make assertions to test that expectation
json.loads.assert_called()
json.loads.assert_called()
json.loads.assert_called_once()
