class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper_function(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper_function

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Andreas")
new_user.is_logged_in = True
create_blog_post(new_user)

inputs = eval(input())
# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper_function(*args, **kwargs):
       print(f"You called {function.__name__}{args}\nIt returned: {function(*args)}")

    return wrapper_function


# TODO: Use the decorator 👇

@logging_decorator
def a_function(a, b, c):
  return a * b * c

a_function(inputs[0], inputs[1], inputs[2])

