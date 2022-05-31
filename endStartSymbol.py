def check(Exp,match,string):

    if(Exp[0]=='^'):
        match = match

    if(Exp[len(Exp) - 1] ==  '$'):
        if(len(string) == match[1]):
            return match
        else:
            match[0] = False
            return match

    return match