# Test file with formatting issues and type errors
def bad_function(x, y):
    result = x + y
    print("Result is:", result)
    return result


# Missing type hints, bad formatting
def another_function(a, b):
    if a > b:
        return a
    else:
        return b
