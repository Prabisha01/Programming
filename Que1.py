#multiply all value in the list

def multiply(list):
    result = 1
    for x in list:
        result *= x
    return result
print(multiply([1,2,8, 5]))
