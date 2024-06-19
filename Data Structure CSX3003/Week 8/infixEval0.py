class evaluateString:

    def evalString(self, expression):
        valueStack = []
        opStack = []
        i = 0

        while (i < len(expression)):
            if (expression[i] == ' '):
                continue
            if (expression[i] >= '0' and expression[i] <= '9'):
                charNumber = []  # for storing number
                j = i
                while (j < len(expression) and expression[j] >= '0' and expression[j] <= '9'):
                    charNumber.append(expression[j])
                    j += 1

                i = (j-1)
                valueStack.append(int(''.join(charNumber)))

            elif (expression[i] == '('):
                opStack.append(expression[i])

            elif (expression[i] == ')'):
                while (opStack[-1] != '('):
                    valueStack.append(self.applyOperation(
                        opStack.pop(), valueStack.pop(), valueStack.pop()))
                opStack.pop()
            elif (expression[i] == '+' or expression[i] == '-' or expression[i] == '*' or expression[i] == '/'):
                while ((len(opStack) != 0) and (self.opPrecedence(expression[i], opStack[-1]))):
                    valueStack.append(self.applyOperation(
                        opStack.pop(), valueStack.pop(), valueStack.pop()))
                opStack.append(expression[i])
            i = i + 1

        while (len(opStack) != 0):
            valueStack.append(self.applyOperation(
                opStack.pop(), valueStack.pop(), valueStack.pop()))

        return valueStack.pop()

    def applyOperation(self, op, a, b):
        if op == '+':
            return a+b
        elif op == '-':
            return b-a
        elif op == '*':
            return a*b
        elif op == '/':
            return b/a
        else:
            return 0

    def opPrecedence(self, op1, op2):
        if (op2 == '(' or op2 == ')'):
            return False
        if ((op1 == '*' or op1 == '/') and (op2 == '+' or op2 == '-')):
            return False
        else:
            return True


a = evaluateString()
string = str(input())
print(string)
print(a.evalString(string))  # print 122
