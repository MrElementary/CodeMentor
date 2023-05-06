# **Time/Space Complexity Report:**

## Time Complexity:

The Time Complexity of this function can be expressed as O(n), where n is the total number of resistance values in our input data set. The reson for this is because our function recursively processes each resistance value in the input and performs constant-time operations to calculate the equivalent resistance of the network.

## Space Complexity:

The Space Complexity of this function can also be expressed as O(n), where n is the total number of resistance values in the input data set. The reason for this would be because the function stores the input data set and any intermediary results in memory during the recursive calls.

The worst-case scenario would be incrementally related to the size of the data set itself, and in terms of time complexity, the longer the overall processing time will be due to the larger number of recursive calls required for each tuple/list to unpack. In terms of Space complexity, this continous increment of recursion would also ultimately require larger increases in memory to support the successful run of the application as the data set given becomes larger.

In summary the worst-case scenario for the resistor_networks.py program would still be expressed as O(n) where n is the total number of resistance values in the input.
