# calculator-parser

This program takes in an expression as a command-line argument and parses and evaluates it, then outputs the result. It implements a stack-based approach to ensure parentheses logic and correct order of operations

``evaluate_expression(expression)``:

This method calculates the result of an expression. It does this by creating two separate lists---values and operators---that store integers and operators, respectively. The method iterates through the given string and appends the integers to values. The operators within the string are appended to the operators stack. apply_operator is then called to evaluate the sub-expression (see below). While the operators stack contains values, apply_operator is run on it to clear out values. The method ultimately returns values[0], which should be the only value remaining in values and serves as the expression's result.

``apply_operator(operators, values)``:

This method utilizes the aforementioned 'values' and 'operator' stacks to calculate the operations between two integers. The integers are popped from values and assigned to either left or right depending on their position in the expression. The method applies the relevant operation to them, and the result is appended to values.

``precedence(operator)``:

This method ensures the calculator follows the rules of precedence (PEMDAS) in determining the expression's value. If the given character is a plus sign, for example, the method returns the lowest value given that addition is assigned the least precedence in terms of order of operations. Conversely, the exponent symbol takes prededence over the plus sign and therefore causes the method to return a higher value.

