def is_operator_or_variable(char):
    return char in {'+', '-', '*', '/', '(', ')'} or char.isalpha()

def precedence(operator):
    return {'+': 1, '-': 1, '*': 2, '/': 2}.get(operator, 0)

def infix_to_postfix(infix_expression):
    output = []
    operator_stack = []

    for char in infix_expression:
        if char.isalnum():  
            output.append(char)
        elif is_operator_or_variable(char):
            if char == '(':
                operator_stack.append(char)
            elif char == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                operator_stack.pop()
            else:
                while operator_stack and is_operator_or_variable(operator_stack[-1]) and precedence(char) <= precedence(operator_stack[-1]):
                    output.append(operator_stack.pop())
                operator_stack.append(char)
        print("output:"," ".join(output))
        print("Stack:", operator_stack)



    while operator_stack:
        output.append(operator_stack.pop())

    print("output:"," ".join(output))
    print("Stack:", operator_stack)

    return ''.join(output)

def evaluate_postfix(postfix_expression, variables=None):
    if variables is None:
        variables = {}

    stack = []

    for char in postfix_expression:
        if char.isalpha():  
            stack.append(variables.get(char, 0))
            print(f"Stack: {stack}")
        elif char.isdigit():
            stack.append(int(char))
            print(f"Stack: {stack}")
        elif is_operator_or_variable(char):
            right_operand = stack.pop()
            left_operand = stack.pop()
            if char == '+':
                result = left_operand + right_operand
            elif char == '-':
                result = left_operand - right_operand
            elif char == '*':
                result = left_operand * right_operand
            elif char == '/':
                result = left_operand / right_operand
            stack.append(result)
            print(f"Stack: {stack}")

    return stack[0]


def main():
    infix_expression = input("Enter an infix expression: ")
    postfix_expression = infix_to_postfix(infix_expression)
    print("Postfix expression:", postfix_expression)

    variables = {}
    for char in postfix_expression:
        if char.isalpha() and char not in variables:
            value = input(f"Enter value for variable {char}: ")
            variables[char] = int(value)

    result = evaluate_postfix(postfix_expression, variables)
    print("Evaluation result:", result)

if __name__ == "__main__":
    main()