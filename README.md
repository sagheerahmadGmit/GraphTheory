# GraphTheory

Intro
-------------------------------------------------------------------------------------------------------------------

This program is a programming excersise for the module 'Graph Theory' in 3rd year Software Development Course. It is written in the Python programming language.

The aim of the project is to write an application that will match the regular expression to Ken Thompsons' construction. It will do this by taking an NFA infix and converting it to a postfix expression using the shunting algorithm. It will then match it with a given string to see if they match.

Context
-------------------------------------------------------------------------------------------------------------------

The following project has a real world problem that we may be asked to solve in our workplace or
industry. We are not required to solve this problem from the top of our heads but we should be able toresearch and investigate the different methods that we could apply to the problem to solve it. There are many solutions already available and this is one of them.

Structure
-------------------------------------------------------------------------------------------------------------------

There are 3 parts to this project: 
1. Using the Shunting Yard Algorithm to change a regular expression from infix to postfix.
2. Create NFAs for each fragment in the regular expression and assemble them to a single NFA.
3. Match the infix with a string.

The Shunting yard algorithm is an algorthm that converts a infix regular expression to a postfix because its easier to use Thompsons' construction on a postfix regular expression.

Once the regular expression is converted into postfix, It is then converted into a non-deterministic finite automaton. This is done by popping off fragments of the stack and creating new start and accept state for each of the special operators. 

The postfix expression is then matched against a string to see if the string matches the given postfix expression.

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
2. cd into GraphTheory
3. run python3 project.py


Research
-------------------------------------------------------------------------------------------------------------------

https://www.youtube.com/watch?v=RYNN-tb9WxI  
Learning how to convert a regular expression to a NFA and then to a DFA.

https://www.youtube.com/watch?v=Wz85Hiwi5MY  
https://en.wikipedia.org/wiki/Shunting-yard_algorithm  
Learning more about the shunting yard algorithm

http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_04_01.html  
A little more insight on regular expressions  


