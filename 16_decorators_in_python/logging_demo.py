import logging
from functools import wraps

# Make sure logging prints to console
logging.basicConfig(level=logging.INFO)

def log_function_call(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b

print(my_function(5, 7))
