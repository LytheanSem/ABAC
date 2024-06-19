def PostfixToInfix(postfix):

    symbols = []

    for _ in postfix:

        # Push operands
        if not Operator(_):
            symbols.insert(0, _)

        # We will assume that the given expression is a valid postfix
        else:

            op_1 = symbols[0]
            symbols.pop(0)
            op_2 = symbols[0]
            symbols.pop(0)
            symbols.insert(0, "(" + op_2 + _ +
                           op_1 + ")")

    # At the end, the stack will contain only one string
    return symbols[0]

# Defnining a function to check if the symbol is an operator


def Operator(symbols):
    if symbols == "*" or symbols == "+" or symbols == "-" or symbols == "/" or symbols == "^" or symbols == "(" or symbols == ")":
        return True
    else:
        return False


# Calling the function
string = map(str, input().split())
print("The infix expression is: ", PostfixToInfix(string))
