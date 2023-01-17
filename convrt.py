import os

condition = ["if", "else"]
loop = ["for", "while"]
stop_at = ['<', '>', '(', '{', '\n', ' ', ';']
bracket = ['(', ')', '{', '}']
endst = []
out_file = open("/home/agrawalvedant03/mysite/output.txt", "w")

# def intialize():
#     global condition, loop, stop_at, bracket
#     condition = set(["if", "else"])
#     loop = set(["for", "while"])
#     stop_at = set(['<', '>', '(', '{', '\n', ' ', ';'])
#     bracket = set(['(', ')', '{', '}'])

def comm(s):
    if len(s) < 2:
        return False
    if s == "//":
        print("OK")
        return True
    return False

def func_cin(line):
    out_file.write("Input")
    i = 5
    while i < len(line):
        temp = ""
        if line[i] == ";":
            break
        while i < len(line) and line[i] != ">":
            if line[i] == ";":
                break
            temp += line[i]
            i += 1
        i += 2
        out_file.write(" " + temp)
    out_file.write("\n")

    temp = ""
    while i < len(line):
        temp += line[i]
        i += 1
        if comm(temp):
            s = "\\Comment{$"
            while i < len(line):
                # print(s)
                s += line[i]
                i += 1
            s = s[:-1]
            s =  s+"$}\n"
            out_file.write(s)
            return

def func_cout(line):
    i = 6
    out_file.write("\\State \\textbf{print}")
    while i < len(line):
        temp = ""
        while i < len(line) and line[i] != "<":
            if line[i] == ";":
                break
            temp += line[i]
            i += 1
        out_file.write(" " + temp)
        if line[i] == ";":
            i += 2
            break
        i += 2
    out_file.write("\n")

    temp = ""
    while i < len(line):
        temp += line[i]
        i += 1
        if comm(temp):
            s = "\\Comment{$"
            while i < len(line):
                # print(s)
                s += line[i]
                i += 1
            s = s[:-1]
            s =  s+"$}\n"
            out_file.write(s)
            return

def func_return(line):
    i = 7
    s = "\\State \\Return $"
    temp = ""
    while i < len(line) and line[i] != ';':
        temp += line[i]
        i += 1
    i += 2
    if not temp.strip():
        temp = "0"
    out_file.write(s + temp + "$\n")

    temp = ""
    while i < len(line):
        temp += line[i]
        i += 1
        if comm(temp):
            s = "\\Comment{$"
            while i < len(line):
                # print(s)
                s += line[i]
                i += 1
            s = s[:-1]
            s =  s+"$}\n"
            out_file.write(s)
            return


def func_cond(line):
    brack = 1
    i = 0
    temp = ""

    while line[i] not in bracket:
        temp += line[i]
        i += 1

    if temp == "if":
        out_file.write("\\If{$")
    elif temp == "elseif":
        out_file.write("\\ElsIf{$")
    else:
        out_file.write("\\Else\n")

    if line[i] == '(':
        i += 1
        s = ""
        while brack > 0:
            s += line[i]
            if line[i] == '(':
                brack += 1
            elif line[i] == ')':
                brack -= 1
            i += 1
        s = s[:-1]
        out_file.write(s + "$}\n")
        i += 1
    i += 1

    temp = ""
    while i < len(line):
        temp += line[i]
        i += 1
        if comm(temp):
            s = "\\Comment{$"
            while i < len(line):
                # print(s)
                s += line[i]
                i += 1
            s = s[:-1]
            s =  s+"$}\n"
            out_file.write(s)
            return

    endst.append("\\EndIf")

def func_loop(line):
    brack = 1
    i=0
    temp = ""

    while(line[i] != '('):
        temp += line[i]
        i+=1

    i+=1

    ini = ""
    cond = ""
    lst = ""
    if temp == "for":
        while(line[i] != ';'):
            ini += line[i]
            i+=1
        out_file.write("\\State ${}$\n".format(ini))
        i+=1
        while(line[i] != ';'):
            cond += line[i]
            i+=1
        i+=1
        while(brack):
            if(line[i] == '('):
                brack +=1
            elif(line[i] == ')'):
                brack -=1
            lst += line[i]
            i+=1
        lst = lst[:-1]
        i += 2
    else:
        while(brack):
            if(line[i] == '('):
                brack +=1
            elif(line[i] == ')'):
                brack -=1
            cond += line[i]
            i+=1
        cond = cond[:-1]
        i += 2

    out_file.write("\\While{$" + cond + "$}\n")

    temp = ""
    while(i < len(line)):
        temp += line[i]
        i+=1
        if comm(temp):
            s = "\\Comment{$"
            while i < len(line):
                # print(s)
                s += line[i]
                i += 1
            s = s[:-1]
            s =  s+"$}\n"
            out_file.write(s)
            return

    if temp != "for":
        endst.append("\\EndWhile")
    else:
        endst.append("\\State ${}$\n\\EndWhile".format(lst))
    print("\n")

def func_state(line):
    out_file.write("\\State $")
    i = 0
    temp = ""
    while i < len(line) and line[i] != ';':
        temp += line[i]
        i += 1
    i += 1
    out_file.write(temp + "$\n")
    temp = ""
    while i < len(line):
        temp += line[i]
        i += 1
        if comm(temp):
            s = "\\Comment{$"
            while i < len(line):
                # print(s)
                s += line[i]
                i += 1
            s = s[:-1]
            s =  s+"$}\n"
            out_file.write(s)
            return

def func_comm(line):
    i = 0
    temp = ""
    while(i < len(line)):
        temp += line[i]
        i += 1
        if comm(temp):
            s = "\\Comment{$"
            while i < len(line):
                # print(s)
                s += line[i]
                i += 1
            s = s[:-1]
            s =  s+"$}\n"
            out_file.write(s)
            return

def check(word, line):
    # print(word)
    if word == "cin":
        func_cin(line)
    elif word == "cout":
        func_cout(line)
    elif word == "return":
        func_return(line)
    elif word in condition:
        func_cond(line)
    elif word in loop:
        func_loop(line)
    elif word == "\\\\":
        func_comm(line)
    else:
        func_state(line)

if __name__ == "__main__":
    inFile = open("prog.txt", "r")
    # intialize()
    line = inFile.readline()

    i = 0
    while i < len(line) and line[i] != ' ':
        i += 1
    i += 1
    s = ""
    while i < len(line) and line[i] != '(':
        s += line[i]
        i += 1
    i += 1
    brack = 1
    v = []
    w = ""
    while i < len(line) and brack:
        if line[i] == '(':
            brack += 1
        elif line[i] == ')':
            brack -= 1
        w += line[i]
        if line[i] == ' ':
            w = ""
        elif line[i] == ',':
            w = w[:-1]
            v.append(w)
            w = ""
        i += 1
    w = w[:-1]
    v.append(w)

    out_file.write("\\documentclass{article}\n")
    out_file.write("\\usepackage{algorithm}\n")
    out_file.write("\\usepackage{algpseudocode}\n")
    out_file.write("\\begin{document}\n")
    out_file.write("\\begin{algorithm}\n")

    out_file.write("\\caption{$" + s + "$}\n\\begin{algorithmic}\n")
    out_file.write("\\Procedure{$" + s + "$}{$")
    if v:
        out_file.write(v[0])
        for i in range(1, len(v)):
            out_file.write(", " + v[i])
        out_file.write("$}\n")

    while inFile:
        line = inFile.readline()
        if not line:
            break
        if line == "\n":
            continue
        i = 0
        word = ""
        while i < len(line) and (line[i] not in stop_at):
            word += line[i]
            i += 1
        if word == "}":
            if not endst:
                continue
            s = endst.pop()
            out_file.write(s + "\n")
            continue
        check(word, line)
    out_file.write("\\EndProcedure\n")
    out_file.write("\\end{algorithmic}\n")
    out_file.write("\\end{algorithm}\n")
    out_file.write("\\end{document}\n")