# Cpp-to-Pseudocode
This code is a Flask application that creates a web page for converting a file to pseudocode.

It does this by doing the following:

1.	Imports the necessary modules such as Flask, request and os.
2.	Creates an instance of Flask web application.
3.	Defines a route for the root URL '/' which renders an HTML template 'index.html'.
4.	Defines another route '/convert' which is only accessible via a POST request.
5.	When a file is posted to the '/convert' route, it checks if the file 'prog.txt' exists and removes it if it does.
6.	It then saves the posted file as 'prog.txt'
7.	It generates an output file 'output.txt' which is read and the contents are saved in a variable "pseudocode"
8.	The template 'index.html' is rendered again but this time with the pseudocode variable passed to it.
Finally, the script runs the flask application in debug mode which allows for the application to be reloaded automatically when changes are made to the code.




Converting C++ to LaTeX PseudoCode is given below:

This script reads a given file and converts its code to pseudocode and writes the output in a file called "output.txt"

First, it creates global variables, such as lists of keywords for conditions and loops, a list of characters to stop at when parsing the file, and a list of bracket characters.
It also opens the output file in write mode.

The script defines several functions:

1.	The comm() function checks if a line has a single-line comment marker.
2.	The func_cin() function handles lines that contain input statements and writes the corresponding pseudocode to the output file.
3.	The func_cout() function handles lines that contain output statements and writes the corresponding pseudocode to the output file.
4.	The func_return() function handles lines that contain return statements and writes the corresponding pseudocode to the output file.
5.	The func_cond() function handles lines that contain conditional statements and writes the corresponding pseudocode to the output file.
6.	The func_loop() function handles lines that contain loop statements and writes the corresponding pseudocode to the output file.
7.	The func_state() function handles lines that contain operation statements and writes the corresponding pseudocode to the output file.
8.	The func_comm() function handles lines that contain only comment and writes the corresponding pseudocode to the output file.
It then reads the input file line by line, and calls the appropriate function based on the keyword used in the line.

Finally, it closes the output file.

Link for Tutorial Video: https://drive.google.com/file/d/1eA_pvJRxE1R8_PEUlp4hjSe-5canCD6L/view?usp=share_link

Link for Website: http://frankenstein0208.pythonanywhere.com/