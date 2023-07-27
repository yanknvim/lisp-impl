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
        return s
    elif s[0] == "eq":
        return eval(s[1]) == eval(s[2])
    elif s[0] == "car":
        return s[1][0]
    elif s[0] == "cdr":
        return s[1][1:]

program = input()
print(eval(parse(tokenize(program))))
