import unittest
import project

class TestProject(unittest.TestCase):

    def setUp(self):
        #test values for the . operator
        self.a = "a.b"
        self.b = "ab"
        self.c = "bb"
    
        #test values for the * operator
        self.d = "b*"
        self.e = "bbb"
        self.f = "abc"

        #test values for the | operator
        self.g = "a|b"
        self.h = "a"
        self.i = "abc"
        
        #test values for the + operator
        self.j = "ab+b"
        self.k = "ba"
        self.l = "ababc"
        
        #test values for the ? operator
        self.m = "a?b"
        self.n = "abba"
        self.o = "abbca"

    #Test the . operator
    def test_dot_operator_false(self):
        #get the results of the function
        result = project.match(self.a, self.c)
        #the expected result
        expected = False
        self.assertEqual(expected, result)
        

    #Test the . operator
    def test_dot_operator_true(self):
        #get the results of the function
        result = project.match(self.a, self.b)
        #the expected result
        expected = True
        self.assertEqual(expected, result)

    
   #Test the * operator
    def test_kleene_operator_false(self):
        #get the results of the function
        result = project.match(self.d, self.f)
        #the expected result
        expected = False
        self.assertEqual(expected, result)
        

    #Test the * operator
    def test_kleene_operator_true(self):
        #get the results of the function
        result = project.match(self.d, self.e)
        #the expected result
        expected = True
        self.assertEqual(expected, result)  

    #Test the | operator
    def test_or_operator_false(self):
        #get the results of the function
        result = project.match(self.g, self.i)
        #the expected result
        expected = False
        self.assertEqual(expected, result)
        

    #Test the | operator
    def test_or_operator_true(self):
        #get the results of the function
        result = project.match(self.g, self.h)
        #the expected result
        expected = True
        self.assertEqual(expected, result)

    #Test the + operator
    def test_plus_operator_false(self):
        #get the results of the function
        result = project.match(self.j, self.l)
        #the expected result
        expected = False
        self.assertEqual(expected, result)
        

    #Test the + operator
    def test_plus_operator_true(self):
        #get the results of the function
        result = project.match(self.j, self.k)
        #the expected result
        expected = False
        self.assertEqual(expected, result)
    
    #Test the ? operator
    def test_question_mark_operator_false(self):
        #get the results of the function
        result = project.match(self.m, self.o)
        #the expected result
        expected = False
        self.assertEqual(expected, result)
        

    #Test the ? operator
    def test_question_mark_operator_true(self):
        #get the results of the function
        result = project.match(self.m, self.n)
        #the expected result
        expected = False
        self.assertEqual(expected, result)


    #Test the regular expression
    def test_regex_example_true1(self):
        #get the results of the function
        result = project.match("a.b|b*", "bbb")
        #the expected result
        expected = True
        self.assertEqual(expected, result)
    
    #Test the regular expression
    def test_regex_example_false1(self):
        #get the results of the function
        result = project.match("a.b|b*", "bbcb")
        #the expected result
        expected = False
        self.assertEqual(expected, result)

    #Test the regular expression
    def test_regex_example_true2(self):
        #get the results of the function
        result = project.match("a.b.c", "abc")
        #the expected result
        expected = True
        self.assertEqual(expected, result)
    
    #Test the regular expression
    def test_regex_example_false1(self):
        #get the results of the function
        result = project.match("a.b.c*", "adfbc")
        #the expected result
        expected = False
        self.assertEqual(expected, result)

#run the tests
unittest.main()
