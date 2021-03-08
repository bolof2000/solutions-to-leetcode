
import unittest

from solutions import *
class TestAllSolutions(unittest.TestCase):
       

     test = NonDupSolution()
     def testNonDuplications(self):
        nums = [1,1,2,2,3,3,4,4,4,5]
        result = self.test.nonDuplicateNumber(nums)
        self.assertEqual(5,result)
        
     testBinarySearchSolution = BinarySearchSolution()
     def testBinarySearch(self):
           result = self.testBinarySearchSolution.findNumberUsingBinarySearch([1,2,3,4,5,6],6) 
           
           self.assertEqual(5,result)
         
    
     testMoveZeroSolutons = SolutionsMoveZeros()
     def testMoveZeros(self):
            
            result = self.testMoveZeroSolutons.moveZerosToTheEnd([0,1,0,3,12])
            
            self.assertEqual([1,3,12,0,0],result)
            
            
     solutionLongestSub = SolutionLongestSub()
     def testLongestSubSolution(self):
            result = self.solutionLongestSub.longestSubString("abcabcbb")
            
            self.assertEqual(3,result)
                 


      
           
            
       