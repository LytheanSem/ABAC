def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


Stack = []
postfix_expr = input().split()
print(postfix_expr)
for token in postfix_expr:
    if is_number(token):
        Stack.append(float(token))
    else:
        operand2 = Stack.pop()
        operand1 = Stack.pop()
        # print(operand1)
        # print(operand2)
        # print(Stack)

        if token == '+':
            result = operand1 + operand2
        elif token == '-':
            result = operand1 - operand2
        elif token == '*':
            result = operand1 * operand2
        elif token == '/':
            result = operand1 / operand2
        elif token == '%':
            result = operand1 % operand2
        elif token == '^':
            result = operand1 ** operand2
        elif token == '//':
            result = operand1 // operand2

        Stack.append(result)
print('%.1f' % Stack[0])
print(round(Stack[0], 1))
