import listRange

stack = [[]]

def last():
    return stack[len(stack)-1]

def lastElementStack():
    return last()[len(last())-1]

def parentheses(i,string,value):
    index = string[i:].find('}')
    index = i + index # becuase the substring will return it own index so adding to the i same for []
    Range = string[i:index].split(',')

    if(len(Range) == 1):
        i = i + len(Range[0])
        for val in range(0,int(Range[0])):
            last().append(value)
        return i+1

    else:
        i  = i + len(Range[0]) + len(Range[1])
        for val in range(0,int(Range[0])):
            last().append(value)

        if(Range[1] != ''):
            endMultipler = int(Range[1])
            end = value.copy()
            end['quantifier'] = 'zeroOrOne'
            for val in range(int(Range[0]), endMultipler):
                last().append(end)
            return i+2

        elif(Range[1] == ''):
            AtLeast = value.copy()
            AtLeast['quantifier'] = 'zeroOrMore'
            last().append(AtLeast)
            return i + 2


def re(string): # START
    i = 0
    length = len(string)
    while(i<length):
        char = string[i]
        if(char == '^' or char == '$'):
            i = i + 1

        elif(char =='*'):
            lastElementStack()['quantifier'] = 'zeroOrMore'
            i = i + 1

        elif (char == '+'):
            d2 = lastElementStack().copy() # deep copy
            d2['quantifier'] = 'zeroOrMore'
            last().append(d2)
            i = i + 1

        elif(char == '{'):
            value = lastElementStack()
            last().pop() # pop the last element becz value has the last element
            if(value['type']== 'list'):
                value['quantifier'] = 'exactlyOne'

            stack.append([])
            i = i + 1
            i = parentheses(i , string,value)
            parenthesesSet = stack.pop()
            for val in parenthesesSet:
                last().append(val)

        elif(char == '['):
            endIndex = string[i:].find(']')# becuase the substring will return it own index so adding to the i same for {}
            endIndex = i + endIndex
            i = 1 + i
            Input = string[i : endIndex]
            i = endIndex + 1
            valueString = listRange.RangeModule(Input)


            state = {
                'type' : 'list',
                'value': valueString,
                'quantifier': 'exactlyOne'
            }

            last().append(state)


        else:
            last().append({
                'type': 'element',
                'value' : char,
                'quantifier': 'exactlyOne'
            })
            i = i + 1
    return stack[0]




