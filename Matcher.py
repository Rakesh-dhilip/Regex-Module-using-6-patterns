def indexChanger(currentState,input,i):

    if(i>=len(input)):
        return [False,0]

    elif (currentState['type'] == 'list'):
        if (input[i] in currentState['value']):
            return [True, 1]
        return [False,0]


    elif(currentState['type'] == 'element'):

        if(input[i] == currentState['value']):
            return [True,1]

        else:
            return [False,0]

def shift(QUENE):
    if(len(QUENE)==0):
        return None
    else:
        return QUENE.pop(0)

def match(input,states):
    QUENE = states
    currentState = shift(QUENE)
    i = 0
    while(currentState):

        if(currentState['quantifier'] == 'exactlyOne'):

            [isMatch,changeIndex] = indexChanger(currentState,input,i)

            if(isMatch == False):

                return [isMatch,i]

            else:
                i = i + changeIndex


                currentState = shift(QUENE)


        elif(currentState['quantifier'] == 'zeroOrMore'):
            while(True):
                [isMatch, changeIndex] = indexChanger(currentState, input, i)

                if(isMatch == False and changeIndex == 0 ):
                    currentState = shift(QUENE)
                    break
                i = i + changeIndex


        elif (currentState['quantifier'] == 'zeroOrOne'):
            if(i>=len(input)):
                currentState = shift(QUENE)
            [isMatch, changeIndex] = indexChanger(currentState, input, i)
            i = i + changeIndex
            currentState = shift(QUENE)


    return [True,i]
