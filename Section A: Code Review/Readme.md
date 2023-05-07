# Recursion Review:

## Scores:

### **Efficiency**: 3/4

Your second function used to calculate and display a fibonacci sequence, does not make use of recursion but instead implements a for loop. Remeber recursion is the process of defining a problem (or the solution to a problem) in terms of (a simpler version of) itself, implying that in order for the solution to be solved recursively, the function needs to implement itself as a means to solve the problem.

While for loops are an extremely effective and powerful tool in our coding arsenal, there will be times throughout our career where solving without recursion will ultimately lead to longer computational times and will be ineffective for solving complex solutions. In this instance a recursive solution will not only improve our code's effectiveness but also make it more readable to anybody trying to understand it.

### **Correctness**: 2/4

Within your main method, while the reverse_string method is executing correctly, your second method is not being called anywhere. Have a look at line 11 and consider what would be required to make use of the fibonacci recursion function for your output.

Your first function, reverse_string, contains a return call for a non-existant function name on line 26, as the name "reverseString" does not match the original name of your function, "reverse_string" as written on line 18.

In your second function, you're declaring a variable called maxNumber on line 30, however it has already been declared as a parameter of the method in line 28. Duplication of this nature will confuse the compiler into not knowing which value to perform commands on ultimately.

### **Style**: 3/4

Consider seperating your functions from your main function as stand-alone as this will conform better to best coding practices and provide a clearer picture of each functions place in our program. Once we start working on larger programs the benefit of making this a habit will be your best friend! It also makes it easier to come back to the program at a later stage and tweak things to make improvements and changes.

Using the name 'function' as a name for our method is also not considered a good practice. When we name methods we should always lean towards using names that are effective at giving a short but sweet indication of the method's purpose in our program. Consider renaming it to something like fibonacci_sequence.

### **Documentation**: 3/4

Well done one solid commenting, explaining what each function does and ultimately drawing on what the program is designed to do. Consider however as mentioned the print statement in your main method at line 11 to document the outcome of the second method as it may currently seem misleading.

Documentation is a powerful tool to explain in our absence to anybody viewing our code what it's purpose serves and how it is executed.

## Positive Aspects

Your code has a solid structure, easy to read and understand! You also show a solid understanding of what is required in your first function, reverse_string, well done!

Your comments are well formulated and explain exactly what is required.

## Aspects to improve on

Focus on your second function for the Fibonacci series to make use of itself recursively as it repeats the code until it reaches the number of values entered(maxNumber).
Refer to the information provided above on how best to approach this, also consider having a look here (https://www.w3schools.com/java/java_recursion.asp)

Here you can have a look at some naming conventions for the Java programming language: (https://www.oracle.com/java/technologies/javase/codeconventions-namingconventions.html)

## Overall Feedback

Other than the changes required to fix the code for the task at hand, you did very well! Best of luck forward and I look forward to your next submission!

Remember - a person who never made a mistake never tried anything new - Albert Einstein :D
