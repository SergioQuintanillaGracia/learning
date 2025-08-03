import time

def delay_decorator(func):
    def wrapper():
        time.sleep(2)
        func()

    return wrapper

@delay_decorator
def say_hello():
    print("Hello")

say_hello()