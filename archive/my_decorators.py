def logger(function):
    def wrapper(*args, **kwargs):
        print(f"----- {function.__name__}: start -----")
        output = function(*args, **kwargs)
        print(f"----- {function.__name__}: end -----")
        return output
    return wrapper

# @logger
def some_func():
    print(True)


decorated_func = logger(some_func)

decorated_func()