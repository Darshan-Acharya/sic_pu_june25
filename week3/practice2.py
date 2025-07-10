#INFIX EXPRESSION VALIDATION AND INFIX TO POSTFIX EXPRESSION CONVERSION
def infix_to_postfix(expression):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    stack = []  # stack to hold operators
    postfix = ''  # result string

    for char in expression:
        if char.isalnum():
            postfix += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop() 
        else:
            while (stack and stack[-1] != '(' and
                   precedence.get(char, 0) <= precedence.get(stack[-1], 0)):
                postfix += stack.pop()
            stack.append(char)

    # Pop all remaining operators
    while stack:
        postfix += stack.pop()

    return postfix


# Example usage:
infix_expr = "a+b*(c^d-e)^(f+g*h)-i"
postfix_expr = infix_to_postfix(infix_expr)
print("Infix Expression: ", infix_expr)
print("Postfix Expression:", postfix_expr)
