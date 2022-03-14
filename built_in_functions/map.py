n = (1, 2, 3, 4)


def square(x):
    return x * x


n_squared = tuple(map(square, n))

n_squared_2 = tuple(map(lambda x: x * x, n))

colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
colors_join = list(map(' '.join, colors))
