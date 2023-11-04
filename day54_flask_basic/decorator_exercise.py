import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇
def speed_calc_decorator(function):
    def wrapper_function():
        before_time = time.time()
        function()
        after_time = time.time()
        time_diff = after_time - before_time
        print(f"{function.__name__} run speed: {time_diff}s")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

fast_function()
slow_function()