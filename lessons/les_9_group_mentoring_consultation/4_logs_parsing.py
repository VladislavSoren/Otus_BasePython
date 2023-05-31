"""
Parsing

match - case можно реализовать на базе словаря

"""

log_content = '''10:10:15 28.03.2023 GET /users User-agent: Safari
10:10:16 28.03.2023 POST /users User-agent: Safari'''


def parse_row(row):
    _time, _date, _method, _endpoint, *_ = row.split()
    return _time, _date, _method, _endpoint


parsed_log = [parse_row(row) for row in log_content.splitlines()]

print(parsed_log)
# :=
