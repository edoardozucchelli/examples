from datetime import datetime


# ----- Example 1 ----- #


def f(x):
    """
    Python 3.10 (2021) introduced the match-case
    statement which provides a first-class
    implementation of a "switch" for Python.
    """
    match x:
        case 'a':
            return 1
        case 'b':
            return 2
        case _:
            return 0   # 0 is the default case if x is not found


# ----- Example 2 ----- #


def g(x):
    return {
        'a': 1,
        'b': 2
    }.get(x, 'default')


# ----- Example 3 ----- #


class Switch:
    """
    Context Manager uses __enter__ and __exit__
    method when called with the "with" statement.
    """
    def __init__(self, value):
        self.value = value

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return False  # Allows a traceback to occur

    def __call__(self, *values):
        return self.value in values


with Switch(datetime.today().weekday()) as case:
    if case(0):
        # Basic usage of switch
        print("I hate mondays so much.")
        # Note there is no break needed here
    elif case(1, 2):
        # This switch also supports multiple conditions (in one line)
        print("When is the weekend going to be here?")
    elif case(3, 4):
        print("The weekend is near.")
    else:
        # Default would occur here
        print("Let's go have fun!")
