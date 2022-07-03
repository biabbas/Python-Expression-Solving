"""This program returns the value of an valid expression after its been solved using BODMAS
For more information and other variants of this code,
Please visit: https://github.com/biabbas
This code can Also solve -ve numbers.
"""

def Prior(x):
    '''This returns the priority of an operator
    This is useful for implementing BODMAS rule'''
    if x=='#':
        return -1
    elif x=='+' or x=='-':
        return 1
    elif x=='*' or x=='/':
        return 2
    else:
        return 0
def cal(a,b,o):
    """This function returns the result of operation between operations
    REturns a o b;"""
    if o == '+':
        return a+b
    elif o == '-':
        return a-b
    elif o == '*':
        return a*b
    else:
        return a/b
    
stack = ['#']      #Stack to stroe operations
stack2 = [0]      #Stack 2 to store digits or numbers
print("Enter Expression\n")
Str = input()
Str +='+0'
i = 0
while i<len(Str):
    if Str[i].isdigit() :
        if Str[i-1].isdigit():
            stack2[-1] = stack2[-1]*10 + int(Str[i])
        else:
            stack2.append(int(Str[i]))
    elif Str[i] == '(':
        stack.append(Str[i])
    elif Str[i] == ')':
        while stack[-1] != '(':
             a = stack2.pop()
             b = stack2.pop()
             stack2.append(cal(b,a,stack.pop()))
        stack.pop()
    elif Str[i] == '-' and (not Str[i-1].isdigit() and Str[i-1]!=')' or i<1):
        stack2.append(0)
        i = i+1
        while Str[i].isdigit() and (i+1)!=len(Str):
            stack2[-1] = stack2[-1] * 10 - int(Str[i])
            i = i+1
        i = i-1
    elif Prior(Str[i]) <= Prior(stack[-1]):
        while Prior(Str[i]) <= Prior(stack[-1]):
             a = stack2.pop()
             b = stack2.pop()
             stack2.append(cal(b,a,stack.pop()))
        stack.append(Str[i])
    else:
        stack.append(Str[i])
    i = i+1
while stack[-1]!='#':
    a = stack2.pop()
    b = stack2.pop()
    stack2.append(cal(b,a,stack.pop()))
res = stack2.pop()
print("REsult is ",res)
