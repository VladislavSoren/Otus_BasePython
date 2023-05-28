def cache(func):
    result = {}
    def wrapper(*args, **kwargs):
        nonlocal results
        ...
        # result[key] = result

def sum_it(*args):
    pass

results = {}
sum_it(1, 5)
sum_it(1, 5)
sum_it(1, 5)