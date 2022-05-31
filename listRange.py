
def Range(start, end):
    st = ""
    for i in range(ord(start), ord(end) + 1):
      st = st + chr(i)
    return st

def RangeModule(Input):
    if('-' not in Input):
        return Input

    output = ""
    for i in range(0,len(Input)):
        if(Input[i] == '-'):
            output = output + Range(Input[i-1],Input[i+1])

    return output