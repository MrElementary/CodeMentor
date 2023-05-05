"""AST Module for string conversion"""
import ast

def process_resistors(arr):
    '''
    Returns the processed network resistance value of the data set provided.

        Parameters:
                arr (list, tuple): list or tuple of data set

        Returns:
                arr (float): final float value of processed data
    '''
    # Convert initial array from string to tuple/list
    if isinstance(arr, str):
        arr = ast.literal_eval(arr)

    # If the current outer nest is a list, go deeper and repeat
    if isinstance(arr, list):
        for i, item in enumerate(arr):
            arr[i] = process_resistors(item)
        if all(isinstance(item, (int, float)) for item in arr):
            values = [1 / x for x in arr]
            values = 1 / sum(values)
            return values

    # If the current outer nest is a tuple, go deeper and repeat
    elif isinstance(arr, tuple):
        arr = list(arr)# convert immutable data structure to mutable.
        for i, item in enumerate(arr):
            arr[i] = process_resistors(item)
        if all(isinstance(item, (int, float)) for item in arr):
            return sum(arr)

    # Finally return the current value of arr if it's an integer or a float
    return arr

INIT_ARRAY = "([10, 20], (30, 40))"

network_resistance = round(process_resistors(INIT_ARRAY), 1)
print(network_resistance)
