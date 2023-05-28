'''

except нужно располагать от частного к общему

'''

def div(a, b):
    return a / b


def div_safe(a, b):
    try:
        result =  div(a, b)
    except TypeError as e:
        print('could not divide, type error', e)
    except ZeroDivisionError:
        print('Dont touch me baby!!')
    except ArithmeticError as e:
        print(e)
    except Exception as e:
        print(e)
    else:  # не получили исключение
        print('OK')
        return result
    finally:
        print("Finally operation")


print(div_safe(10, 2))
print(div_safe(10, '2'))
print(div_safe(10, 0))
print(div_safe(10, 2))