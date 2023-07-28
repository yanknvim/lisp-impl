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

env = dict() 
def eval(s, env=env):
    if isinstance(s, int):
        return s
    elif isinstance(s, str):
        return env[s]
    elif s[0] == "+":
        return eval(s[1], env) + eval(s[2], env)
    elif s[0] == "-":
        return eval(s[1], env) - eval(s[2], env)
    elif s[0] == "*":
        return eval(s[1], env) * eval(s[2], env)
    elif s[0] == "/":
        return eval(s[1], env) / eval(s[2], env)
    elif s[0] == "quote":
        return s[1]
    elif s[0] == "atom":
        return isinstance(eval(s[1], env), int)
    elif s[0] == "eq?":
        return eval(s[1], env) == eval(s[2], env)
    elif s[0] == "car":
        return eval(s[1], env)[0]
    elif s[0] == "cdr":
        return eval(s[1], env)[1:]
    elif s[0] == "cons":
        return [eval(s[1], env), eval(s[2], env)]
    elif s[0] == "if":
        if eval(s[1], env) == True:
            return eval(s[2], env)
        else:
            return eval(s[3], env)
    elif s[0] == "begin":
        val = 0
        for exp in s[1:]:
            val = eval(exp, env)
        return val
    elif s[0] == "define":
        env[s[1]] = s[2]
    elif s[0][0] == "lambda":
        penv = dict()
        penv[s[0][1]] = s[1]
        return eval(s[0][2], penv)
    elif s[0] == "print":
        print(eval(s[1], env))
    else:
        eval(s[0], env)

program = input()
print(parse(tokenize(program)))
eval(parse(tokenize(program)), env)
