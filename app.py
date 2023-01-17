from flask import Flask, request, render_template
import os

# use output .txt and prog.txt if running on local host

app = Flask(__name__)

condition = ["if", "}else"]
loop = ["for", "while"]
stop_at = ['<', '>', '(', '{', '\n', ' ', ';']
bracket = ['(', '{']
endst = []
out_file = open("output.txt", "w")

def intialize():
    global out_file
    out_file = open("output.txt", "w")

def comm(s):
    if len(s) < 2:
        return False
    if s.endswith("//"):
        print("OK")
        return True
    return False

def func_cin(line):
    out_file.write("\\State Input")
    i = 5
    while i < len(line):
        temp = ""
        while i < len(line) and line[i] != ">":
            if line[i] == ";":
                break
            temp += line[i]
            i += 1
        out_file.write(" " + temp)
        if line[i] == ";":
            i+=2
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
                if(line[i] == ' '):
                    s += '\\'
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
            if line[i] =='"':
                i += 1
                continue
            if line[i] == "\\":
                temp += "$\\"
                temp += "backslash$"
                i += 1
                continue
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
                if(line[i] == ' '):
                    s += '\\'
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
                if(line[i] == ' '):
                    s += '\\'
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
        endst.append("\\EndIf")
    elif temp == "}else if":
        out_file.write("\\ElsIf{$")
    else:
        out_file.write("\\Else\n")

    if line[i] == '(':
        i += 1
        s = ""
        while brack > 0:
            if(line[i] == ' '):
                s += '\\'
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
                if(line[i] == ' '):
                    s += '\\'
                s += line[i]
                i += 1
            s = s[:-1]
            s =  s+"$}\n"
            out_file.write(s)
            return


def func_loop(line):
    brack = 1
    i=0
    temp = ""

    while(line[i] != '('):
        temp += line[i]
        i+=1
    i+=1

    cond = ""
    while(brack):
        if(line[i] == '('):
            brack +=1
        elif(line[i] == ')'):
            brack -=1
        elif(line[i] == ' '):
            cond += '\\'
        cond += line[i]
        i+=1
    cond = cond[:-1]
    i += 2

    out_file.write("\\While{$" + cond + "$}\n")
    endst.append("\\EndWhile")

    temp = ""
    while(i < len(line)):
        temp += line[i]
        i+=1
        if comm(temp):
            s = "\\Comment{$"
            while i < len(line):
                # print(s)
                if(line[i] == ' '):
                    s += '\\'
                s += line[i]
                i += 1
            s = s[:-1]
            s =  s+"$}\n"
            out_file.write(s)
            return

    print("\n")

def func_state(line):
    out_file.write("\\State $")
    i = 0
    temp = ""
    while i < len(line) and line[i] != ';':
        if(line[i] == ' '):
            temp += '\\'
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
                if(line[i] == ' '):
                    s += '\\'
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
                if(line[i] == ' '):
                    s += '\\'
                s += line[i]
                i += 1
            s = s[:-1]
            s =  s+"$}\n"
            out_file.write(s)
            return

def check(word, line):
    # print(word + " a " + line)
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
    elif word == "//":
        func_comm(line)
    else:
        func_state(line)

def cnvrt():
    inFile = open("prog.txt", "r")
    intialize()
    line = inFile.readline()
    print(len(line))
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
    if w!="":
       v.append(w)

    out_file.write("\\documentclass{article}\n")
    out_file.write("\\usepackage{algorithm}\n")
    out_file.write("\\usepackage{algpseudocode}\n")
    out_file.write("\\begin{document}\n")
    out_file.write("\\begin{algorithm}\n")

    out_file.write("\\caption{$" + s + "$}\n\\begin{algorithmic}\n")
    out_file.write("\\Procedure{$" + s + "$}{")
    if  len(v)!=0:
        out_file.write("$"+v[0])
        for i in range(1, len(v)):
            out_file.write(", " + v[i])
        out_file.write("$}\n")
    else:
        out_file.write("}\n")

    temp = ""
    while i < len(line):
        temp += line[i]
        i += 1
        if comm(temp):
            k = "\\Comment{$"
            while i < len(line):
                # print(s)
                if(line[i] == ' '):
                    k += '\\'
                k += line[i]
                i += 1
            k = k[:-1]
            k =  k+"$}\n"
            out_file.write(k)

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
        print(word)
        for i in range(len(endst)):
            print(endst[i])
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
    out_file.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_code():

    if os.path.isfile("prog.txt"):
        os.remove("prog.txt")
    file = request.files['file']
    file.save("prog.txt")
    cnvrt()
    try:
        with open("output.txt", "r") as f:
            pseudocode = f.read()
    except FileNotFoundError:
         print("output.txt file not found.")
    except:
        print("An error occurred while reading the output.txt file.")

    return render_template('index.html', pseudocode=pseudocode)


if __name__ == '__main__':
    # cnvrt()
    app.run(debug=True)