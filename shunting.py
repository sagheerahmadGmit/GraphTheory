#Sagheer Ahmad
#The Shunting yard algorithm for regular exxpressions

#The input
infix = "(a|b).c*"
print("The input is: ", infix )
#Expected output = "ab|c*."

#Convert input to a stackish list
infix = list(infix)[::-1]

#operator stack
opers = []

#output list
postfix = []

#Operator precedence
prec = {'*': 100, '.': 80, '|': 60, ')': 40, '(': 20}

#loop through the input one character at a time
while infix:
    #pop a characterfro the input
    c = infix.pop()

    #decide what to do
    #if c is an operator or a bracket - do something
    if c == '(':
        #Push an open bracket to the opers stack
        opers.append(c)
    elif c == ')':
        #pop the operator stack until you find an open bracket
        while opers[-1] != '(':
            postfix.append(opers.pop())
        #get rid of the open bracket
        opers.pop()
    elif c in prec:
        #push any operators on the opers stack with the higher prec to the output
        while opers and  prec[c] < prec[opers[-1]]:
            postfix.append(opers.push())
        #push c to the operator stack
        opers.append(c)
    else:
        #typically, we just push the character to the output
        postfix.append(c)

#pop all operators to the output
while opers:
    postfix.append(opers.pop())


#Convert output list to string
postfix = ''.join(postfix)

#Print the results
print("The output is: ", postfix)
