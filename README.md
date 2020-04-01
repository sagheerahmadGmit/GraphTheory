# GraphTheory

Intro
-------------------------------------------------------------------------------------------------------------------

This program is a programming excersise for the module 'Graph Theory' in 3rd year Software Development Course. It is written in the Python programming language.

The aim of the project is to write an application that will match the regular expression to Ken Thompsons' construction. It will do this by taking an NFA infix and converting it to a postfix expression using the shunting algorithm. It will then match it with a given string to see if they match.

Context
-------------------------------------------------------------------------------------------------------------------

The following project has a real world problem that we may be asked to solve in our workplace or
industry. We are not required to solve this problem from the top of our heads but we should be able toresearch and investigate the different methods that we could apply to the problem to solve it. There are many solutions already available and this is one of them.


1. Regular expressions are a notation for describing sets of character strings. The simplest regular expression is a single literal character. Except for the special metacharacters *+?()|, characters match themselves. To match a metacharacter, escape it with a backslash: \+ matches a literal plus character.	

2. Thompsons construction is an algorithm developed by Ken Thompson in 1968. The algorithm splits a regular expression into its smallest sub-expression. For every sub-expression a NFA is created. All those NFA are then put together into a single NFA which can be used to match a string.

3. NFAs were introduced in 1959 by Michael O. Rabin and Dana Scott. They also showed NFA's equivalence to DFAs. NFAs are used in the implementation of regular expressions: Thompson's construction is an algorithm for compiling a regular expression to an NFA that can efficiently perform pattern matching on strings.

Structure
-------------------------------------------------------------------------------------------------------------------

There are 3 parts to this project: 
1. Using the Shunting Yard Algorithm to change a regular expression from infix to postfix.
2. Create NFAs for each fragment in the regular expression and assemble them to a single NFA.
3. Match the infix with a string.

The Shunting yard algorithm is an algorthm that converts a infix regular expression to a postfix because its easier to use Thompsons' construction on a postfix regular expression.

Once the regular expression is converted into postfix, It is then converted into a non-deterministic finite automaton. This is done by popping off fragments of the stack and creating new start and accept state for each of the special operators. 

The postfix expression is then matched against a string to see if the string matches the given postfix expression.

Special Characters
----------------------------------------------------------------------------------------------------------------

The following Special Characters are used within the program:

* Kleene Star -  means a character appears 0 or more times.

. concatenates two characters. So, a.b means a followed by a b.

| means or. So, a|b means a or a b.

+ means a character appears 1 or more times.

? means a character appears 0 or 1 time.

() are used to group characters.

Example output
-----------------------------------------------------------------------------------------------------------------

Infix: a.b|b*  String: bbb  Match:  True  
Infix: a.b|b*  String: abc  Match:  False  
Infix: a.b|b*  String: abbc  Match:  False  
Infix: a.b|b*  String: abbbbb  Match:  True  
Infix: a.b|b*  String: abccd  Match:  False  
  
Infix: a.b.c*  String: bbb  Match:  False  
Infix: a.b.c*  String: abc  Match:  True  
Infix: a.b.c*  String: abbc  Match:  True  
Infix: a.b.c*  String: abbbbb  Match:  True  
Infix: a.b.c*  String: abccd  Match:  False  
  
Infix: b**  String: bbb  Match:  True  
Infix: b**  String: abc  Match:  False  
Infix: b**  String: abbc  Match:  False  
Infix: b**  String: abbbbb  Match:  False  
Infix: b**  String: abccd  Match:  False  
  
True meaning the expression does match and false meaning that the expression does nor match.

How to run this program
------------------------------------------------------------------------------------------------------------------

1. Git clone this repository  
  git clone https://github.com/sagheerahmadGmit/GraphTheory 
 
2. cd into GraphTheory  
  cd GraphTheory/

3. run python3 project.py  
  python3 project.py


Research
-------------------------------------------------------------------------------------------------------------------

https://www.youtube.com/watch?v=RYNN-tb9WxI  
http://www.cs.may.ie/staff/jpower/Courses/Previous/parsing/node5.html  
Learning how to convert a regular expression to a NFA and then to a DFA.

https://www.youtube.com/watch?v=Wz85Hiwi5MY  
https://en.wikipedia.org/wiki/Shunting-yard_algorithm  
Learning more about the shunting yard algorithm

http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_04_01.html  
A little more insight on regular expressions  

https://swtch.com/~rsc/regexp/regexp1.html  
Regular Expression  

https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/  
Infix to Postfix  

https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton  
Nondeterministic finite automaton

https://cs.lmu.edu/~ray/notes/regex/  
Regular Expressions
