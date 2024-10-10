import sys

def apply_operator(operators, values):
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    if operator == '+':
        values.append(left + right)
    elif operator == '*':
        values.append(left * right)
    elif operator == '^':
        values.append(left ** right)

def precedence(operator):
    if operator == '+':
        return 1
    elif operator == '*':
        return 2
    elif operator == '^':
        return 3
    else:
        return 0

def evaluate_expression(expression):

    values = []

    operators = []

    i = 0

    while i < len(expression):
        if expression[i].isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            values.append(num)
            i -= 1
        elif expression[i] in "+*^":
            while (operators and precedence(operators[-1]) >= precedence(expression[i])):
                apply_operator(operators, values)
            operators.append(expression[i])
        elif expression[i] == '(':
            operators.append(expression[i])
        elif expression[i] == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()
        i += 1

    while operators:

        apply_operator(operators, values)

    return values[0]

def main():

    expression = sys.argv[1]

    if '-' in expression or '/' in expression:
        print("Invalid input. Please try again.")
        return

    parentheses_stack = []

    for parentheses in expression:
        if parentheses == '(':
            parentheses_stack.append(parentheses)
        elif parentheses == ')':
            if parentheses_stack:
                parentheses_stack.pop()
    

    if not parentheses_stack:
        result = evaluate_expression(expression)
        print(result)
    else:
        print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()




    


    


