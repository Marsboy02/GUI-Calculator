from stack import *
from math import sin
def evalPostfix(expr):
    s = Stack()
    for token in expr:
        if token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if (token == '+'):
                s.push(val1 + val2)
            elif (token == '-'):
                s.push(val1 - val2)
            elif (token == '*'):
                s.push(val1 * val2)
            elif (token == '/'):
                s.push(val1 / val2)
        else:
            s.push(float(token))

    return s.pop()


# expr1 = ['8', '2', '/', '3', '-', '3', '2', '*', '+']
# expr2 = ['1', '2', '/', '4', '*', '1', '4', '/', '*']
# print(expr1, ' --> ', evalPostfix(expr1))
# print(expr2, ' --> ', evalPostfix(expr2))


# ----------------------------------------------------------------------
def precedence(op):
    if op == '(' or op == ')':
        return 0
    elif op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else:
        return -1


def check_sin(expr):
    while True:
        temp = []
        if 'S' in expr:
            index = expr.index('S')
            expr.pop(index)
            expr.pop(index)
            while expr[index] != ')':
                temp.append(expr.pop(index))
            expr.pop(index)

            string = ''
            for i in temp:
                string += i

            expr.insert(index, string)

        else:
            break

        print(expr)
        return expr



def MakeNewList(expr): # 수식을 list 형식으로 전달받음
    print(expr)
    fixed_expr = []
    temp = []


    for i in expr:
        if i in '0123456789':
            temp.append(i)

        elif i == '(':
            fixed_expr.append(i)

        elif i == ')':
            string = ''
            for k in temp:
                string += k
            fixed_expr.append(string)
            fixed_expr.append(i)
            temp = []

        else:
            string = ''
            for j in temp:
                string += j
            fixed_expr.append(string)
            fixed_expr.append(i)
            temp = []

    if temp:
        string = ''
        for k in temp:
            string += k
        fixed_expr.append(string)

    print(fixed_expr)
    return fixed_expr


def Infix2Postfix(expr):
    s = Stack()
    output = []
    for term in expr:
        if term in '(':
            s.push('(')
        elif term in ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)
        elif term in "+-*/":
            while not s.isEmpty():
                op = s.peek()
                if(precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else:
                    break
            s.push(term)
        else:
            output.append(term)

    while not s.isEmpty():
        output.append(s.pop())

    return output

# def check_sin(string):
#     return string.replace('sin', 'S')


# infix1 = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
# infix2 = ['1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']
# postfix1 = Infix2Postfix(infix1)
# postfix2 = Infix2Postfix(infix2)
# result1 = evalPostfix(postfix1)
# result2 = evalPostfix(postfix2)
# print('  중위표기: ', infix1)
# print('  후위표기: ', postfix1)
# print('  계산결과: ', result1, end='\n\n')
# print('  중위표기: ', infix2)
# print('  후위표기: ', postfix2)
# print('  계산결과: ', result2)
#
# data = list("23+14")
# print(data)
# print('테스트:', evalPostfix(Infix2Postfix(list(data))))
