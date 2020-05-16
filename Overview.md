#Graph Theory Project

Introduction
-------------------------------------------------------------------------------------------------------------------------------

https://github.com/sagheerahmadGmit/GraphTheory  

The following project has a real-world problem that we may be asked to solve in our workplace or industry. We are not required to solve this problem from the top of our heads, but we should be able to research and investigate the different methods that we could apply to the problem to solve it. There are many solutions already available and this is one of them. One of the ways to solve this problem is to use Thompson’s Construction  
  

This repository demonstrates my understanding of Thompson’s Construction and contains a program that was developed for the module 'Graph Theory' in the 3rd year Software Development Course. The program is written in the Python programming language.  
  

The aim of the project was to write an application that will match the regular expression to Ken Thompsons' construction. It does this by taking an NFA infix and converting it to a postfix expression using the shunting algorithm. It will then match it with a given string to see if they match.  
  

The minimum requirement for the application was to accept a regular expression with the special characters ".", "|" and "*" and to match it against an input string. But it has also included the “+” and the “?” operators.  
   
The main parts of this program that we need to know are:  

1.	Regular expressions: are a notation for describing sets of character strings. The simplest regular expression is a single literal character. Except for the special metacharacters “*”, “+”, “?”, “()”, “|”, these characters match themselves. To match a metacharacter, escape it with a backslash: + matches a literal plus character.
2.	Thompsons construction: is an algorithm developed by Ken Thompson in 1968. The algorithm splits a regular expression into its smallest sub-expression. For every sub-expression, an NFA is created. All those NFAs are then put together into a single NFA which can be used to match a string.
3.	NFAs: were introduced in 1959 by Michael O. Rabin and Dana Scott. They showed NFA's equivalence to DFAs. NFAs are used in the implementation of regular expressions: Thompson's construction is an algorithm for compiling a regular expression to an NFA that can efficiently perform pattern matching on strings.

