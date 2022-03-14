single_quotes_list = ['one', 'two', 'three']


def add_double_quotes_in_string(single_quotes_list_):
    return ['"' + x + '"' for x in single_quotes_list_]


double_quotes_list = add_double_quotes_in_string(single_quotes_list)

assert double_quotes_list == ['"one"', '"two"', '"three"']

assert ", ".join(double_quotes_list) == '"one", "two", "three"'
