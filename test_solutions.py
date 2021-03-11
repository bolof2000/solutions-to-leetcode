import pytest 
from codeProSolutions.solutions import *

class TestAllSolutions(object):

    test = SolutionsToStringQuestions()

    @pytest.mark.anagram
    def test_anagram(self):

        result = self.test.isAnagram("bolofbaba","bababolof")
        assert result == True


    @pytest.mark.groupAnagram
    def test_group_anagram(self):

        input = ["eat","tea","ate","nat","bat"]
        actual_result = self.test.groupAnagram(input)
        expected_result = [["bat"],["nat","tan"],["ate","eat","tea"]]
        assert actual_result == expected_result

    @pytest.mark.parenthesis
    def test_valid_parenthesis(self):
        result = self.test.validParenthesis("()")
        assert result == True

    @pytest.mark.backspace
    def test_backspaceString(self):

        actual_result = self.test.backspaceString("a##c","#a#c")
        expected_result = True
        assert actual_result== expected_result



      
           
            
       