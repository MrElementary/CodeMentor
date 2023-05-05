import ast

def process_resistors(arr):

    # If the current outer nest is a list, go deeper and repeat
    if isinstance(arr, list):
        for i, item in enumerate(arr):
            arr[i] = process_resistors(item)
        if all(isinstance(item, (int, float)) for item in arr):
            values = [1 / x for x in arr]
            values = (1 / sum(values))
            return values
        else:
            return arr

    # If the current outer nest is a tuple, go deeper and repeat
    elif isinstance(arr, tuple):
        arr = list(arr)# convert immutable data structure to mutable.
        for i, item in enumerate(arr):
            arr[i] = process_resistors(item)
        if all(isinstance(item, (int, float)) for item in arr):
            return sum(arr)
        else:
            return tuple(arr)
        
    # Finally return the value if it's an integer or a float
    else:
        return arr

arr = "(6, [8, (4, [8, (4, [6, (8, [6, (10, 2)])])])])"

arr = ast.literal_eval(arr) # ast library used to parse string data set
network_resistance = round(process_resistors(arr), 1)
print(network_resistance)
