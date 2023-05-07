"""AST Module for string conversion"""
import ast

def process_resistors(arr, top_level=True):
    '''
    Returns the processed network resistance value of given data set.

        Parameters:
                arr (list, tuple): list or tuple of data set
                top_level (bool): True if the current call
                is the top-level call, False otherwise

        Returns:
                arr (float): final float value of processed data
    '''
    # Convert input from string to tuple/list
    try:
        if isinstance(arr, str):
            arr = ast.literal_eval(arr)
    except Exception:
        return print("Invalid Input")

        
    # If the current outer nest is a list, go deeper and repeat
    if isinstance(arr, list):
        for i, item in enumerate(arr):
            arr[i] = process_resistors(item, False)
        if all(isinstance(item, (int, float)) for item in arr):
            values = [1 / x for x in arr]
            values = 1 / sum(values)
            if top_level:
                print(f"Total network resistance: {round(values, 1)}")
            return values

    # If the current outer nest is a tuple, go deeper and repeat
    elif isinstance(arr, tuple):
        arr = list(arr) # convert immutable data structure to mutable.
        for i, item in enumerate(arr):
            arr[i] = process_resistors(item, False)
        if all(isinstance(item, (int, float)) for item in arr):
            result = sum(arr)
            if top_level:
                print(f"Total network resistance: {round(result, 1)}")
            return result

    # Finally return the current value of arr if it's float or int
    return arr

# Driver code example
INIT_ARRAY = "(6, [8, (4, [8, (4, [6, (8, [6, (10, 2)])])])])"

if __name__ == "__main__":
    network_resistance = process_resistors(INIT_ARRAY)
