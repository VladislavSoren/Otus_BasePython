"""
На протоколе wsgi основываются фреймворки

"""

def app(environ, start_response):
    print('env:', environ)
    response_data = b'Hello'
    start_response("200 OK", [
        ("Content-Type", "text/plain"),  # Заголовки НЕ чувствительны к регистру (case insensitive)!!!
        ("Content-Length", str(len(response_data))),
        # ("Smth else", 123),
    ])
    yield response_data