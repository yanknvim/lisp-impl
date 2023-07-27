def atom(token):
    try:
        return int(token)
    except:
        return str(token)

def tokenize(program):
    return program.replace("(", " ( ").replace(")", " ) ").split()

def parse(tokens):
    token = tokens.pop(0)
    if token == "(":
        l = []
        while tokens[0] != ")":
            l.append(parse(tokens))
        tokens.pop(0)
        return l
    else:
        return atom(token)

def eval(s):
    if isinstance(s, int):
        return s
    elif s[0] == "+":
        return eval(s[1]) + eval(s[2])
    elif s[0] == "-":
        return eval(s[1]) - eval(s[2])
    elif s[0] == "*":
        return eval(s[1]) * eval(s[2])
    elif s[0] == "/":
        return eval(s[1]) / eval(s[2])
    elif s[0] == "quote":
        return s[1]
    elif s[0] == "atom":
        return isinstance(eval(s[1]), int)
    elif s[0] == "eq?":
        return eval(s[1]) == eval(s[2])
    elif s[0] == "car":
        return eval(s[1])[0]
    elif s[0] == "cdr":
        return eval(s[1])[1:]
    elif s[0] == "cons":
        return [eval(s[1]), eval(s[2])]
    elif s[0] == "if":
        if eval(s[1]) == True:
            return eval(s[2])
        else:
            return eval(s[3])
    elif s[0] == "print":
        print(eval(s[1]))

program = input()
eval(parse(tokenize(program)))
