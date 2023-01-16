#include<bits/stdc++.h>

using namespace std;
set<string>  data_type, condition, loop, Array;
set<char> useless, bracket, stop_at;
stack<string> endst;
ofstream outFile("output.txt", ios::out);

void intialize(){
    condition = {"if", "else"};
    loop = {"for", "while"};
    stop_at = {'<', '>', '(', '{', '\n', ' ', ';'};
    bracket = {'(', ')', '{', '}'};
}

bool comm(string s){
    if(s.length() < 2)
        return 0;
    if(s == "//"){
        cout << "OK\n";
        return 1;
    }
    return 0;
}

void func_cin(string line){

    outFile << "Input";
	int i = 5;
    int flag = 0;
 	while(i < line.size())
    {
        string temp = "";
        if(line[i] == ';')
            break;
 		while(i < line.size() && line[i] != '>')
        {
            if(line[i] == ';')
                break;
            temp += line[i];
            i++;
        }
        i += 2;
        outFile << " " << temp;
 	}
    outFile << "\n";

    string temp = "";
    while(i < line.size()){
        temp += line[i];
        i++;
        if(comm(temp)){
            outFile << "\\Comment{$";
            while(i < line.size()){
                outFile << line[i];
                i++;
            }
            outFile << "$}\n";
            return;
        }
    }
}

void func_cout(string line){

	int i = 6;
    outFile << "\\State \\textbf{print} ";
 	while(i < line.size())
    {
        string temp = "";
 		while(i < line.size() && line[i] != '<')
        {
            if(line[i] == ';')
                break;
            temp += line[i];
            i++;
        }
        outFile << " " << temp;
        if(line[i] == ';'){
            i += 2;
            break;
        }
        i += 2;
 	}
    outFile << "\n";

    string temp = "";
    while(i < line.size()){
        temp += line[i];
        i++;
        if(comm(temp)){
            outFile << "\\Comment{$";
            while(i < line.size()){
                outFile << line[i];
                i++;
            }
            outFile << "$}\n";
            return;
        }
    }
}

void func_return(string line){

	int i = 7;
    outFile << "\\State \\Return $" ;
    string temp = "";
    while(i < line.size() && line[i] != ';')
    {
        temp += line[i];
        i++;
    }
    i += 2;
    if(temp == "")
        temp = "0";
    outFile << temp << "$\n";

    temp = "";
    while(i < line.size()){
        temp += line[i];
        i++;
        if(comm(temp)){
            outFile << "\\Comment{$";
            while(i < line.size()){
                outFile << line[i];
                i++;
            }
            outFile << "$}\n";
            return;
        }
    }
}

void func_cond(string line){

    int brack = 1;
	int i = 0;
    string temp = "";

	while(bracket.find(line[i]) == bracket.end()){
        temp += line[i];
        i++;
    }

    if(temp == "if")
        outFile<<"\\If{$";
    else if(temp == "elseif")
        outFile<<"\\ElsIf{$";
    else
        outFile<<"\\Else\n";

    if(line[i] == '('){
        i++;
        string s = "";
        while(brack){
            s += line[i];
            if(line[i] == '(')
                brack++;
            else if(line[i] == ')')
                brack--;
            i++;
        }
        s.pop_back();
        outFile << s << "$}\n";
        i++;
    }
    i++;

    temp = "";
    while(i < line.size()){
        temp += line[i];
        i++;
        if(comm(temp)){
            outFile << "\\Comment{$";
            while(i < line.size()){
                outFile << line[i];
                i++;
            }
            outFile << "$}\n";
            return;
        }
    }

    endst.push("\\EndIf");
}

void func_loop(string line){

    int brack = 1;
    int i=0;
    string temp = "";

    while(line[i] != '('){
        temp += line[i];
        i++;
    }
    i++;

    string ini = "", cond = "", lst = "";
    if(temp == "for"){
        while(line[i] != ';')
        {
            ini += line[i];
            i++;
        }
        outFile << "\\State $" << ini << "$\n";
        i++;
        while(line[i] != ';')
        {
            cond += line[i];
            i++;
        }
        i++;
        while(brack)
        {
            if(line[i] == '(')
                brack++;
            else if(line[i] == ')')
                brack--;
            lst += line[i];
            i++;
        }
        lst.pop_back();
        i += 2;
    }
    else{
        while(brack){
            if(line[i] == '(')
                brack++;
            else if(line[i] == ')')
                brack--;
            cond += line[i];
            i++;
        }
        cond.pop_back();
        i += 2;
    }

    outFile << "\\While{$" << cond <<"$}\n";

    temp = "";
    while(i < line.size()){
        temp += line[i];
        i++;
        if(comm(temp)){
            outFile << "\\Comment{$";
            while(i < line.size()){
                outFile << line[i];
                i++;
            }
            outFile << "$}\n";
        }
    }

    if(temp != "for")
        endst.push("\\EndWhile");
    else
        endst.push("\\State $" + lst + "$\n" + "\\EndWhile");
    cout<<"\n";
}

void func_state(string line){
    outFile << "\\State $";
    int i = 0;
    string temp = "";
    while(i < line.size() && line[i] != ';'){
        temp += line[i];
        i++;
    }
    i++;
    outFile << temp << "$\n";
    temp = "";
    while(i < line.size()){
        temp += line[i];
        i++;
        // cout << temp << "x\n";
        if(comm(temp)){
            outFile << "\\Comment{$";
            while(i < line.size()){
                outFile << line[i];
                i++;
            }
            outFile << "$}\n";
            return;
        }
    }
}

void func_comm(string line){

    int i = 0;
    string temp = "";

    while(i < line.size()){
        temp += line[i];
        i++;
        if(comm(temp)){
            outFile << "\\Comment{$";
            while(i < line.size()){
                outFile << line[i];
                i++;
            }
            outFile << "$}\n";
            return;
        }
    }
}

void check(string word, string line){
	if(word == "cin") {
		func_cin(line);
	}
	else if(word == "cout") {
		func_cout(line);
	}
	else if(word == "return") {
		func_return(line);
	}
	else if(condition.find(word) != condition.end()) {
		func_cond(line);
	}
	else if(loop.find(word) != loop.end()) {
		func_loop(line);
	}
    else if(word == "\\\\") {
        func_comm(line);
    }
	else {
		func_state(line);
	}
}

void PrintStack(stack<string> s)
{
    if (s.empty())
        return;
    string x = s.top();
    s.pop();
    PrintStack(s);
    cout << x << " ";
    s.push(x);
}

int main()
{
    ifstream inFile("prog.txt");
    intialize();
    string line;

    int i = 0;

    outFile << "\\documentclass{article}\n";
    outFile << "\\usepackage{algorithm}\n";
    outFile << "\\usepackage{algpseudocode}\n";
    outFile << "\\begin{document}\n";
    outFile << "\\begin{algorithm}\n";

    getline(inFile, line);

    while(i < line.size() && line[i] != ' ')
        i++;
    i++;
    string s = "";
    while(i < line.size() && line[i] != '('){
        s += line[i];
        i++;
    }
    i++;
    int brack = 1;
    vector<string> v;
    string w = "";
    while(i < line.size() && brack){
        if(line[i] == '(')
            brack++;
        else if(line[i] == ')')
            brack--;
        w += line[i];
        if(line[i] == ' ')
            w = "";
        else if(line[i] == ','){
            w.pop_back();
            v.push_back(w);
            w = "";
        }
        i++;
    }
    w.pop_back();
    v.push_back(w);
    outFile << "\\caption{$" << s << "$}\n\\begin{algorithmic}\n";
    outFile << "\\Procedure{$" << s << "$}{$";
    if(!v.empty()){
        outFile << v[0];
        int l = v.size();
        for(int i = 1; i < l; i++)
            outFile << ", " << v[i];
    }
    outFile << "$}\n";

    while(inFile){

        // cout << line << "\n";
        int len = endst.size();
        PrintStack(endst);
        cout << "\n";
        getline(inFile, line);
        if(line == "\n")
            continue;
        i = 0;
        string word = "";
        while(i < line.size() && stop_at.find(line[i]) == stop_at.end() ){
            word += line[i];
            i++;
        }
        if(word == "}"){
            if(endst.empty())
                continue;
            string s = endst.top();
            outFile << s << "\n";
            endst.pop();
            continue;
        }
        check(word, line);


    }

    outFile << "\\EndProcedure\n";
    outFile << "\\end{algorithmic}\n";
    outFile << "\\end{algorithm}\n";
    outFile << "\\end{document}\n";

    inFile.close();
    outFile.close();


    return 0;
}