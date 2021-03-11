from collections import defaultdict
import re 
class Node(object):
    
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solutions(object):
    def isValidBsthelper(self,root,low,high):
       pass 
        
        
    def isValidBst(self,root):
        
        if not root:
            return True 
        
        return self.isValidBsthelper(root,float('-inf'),float('inf'))
    
    
    def ransomNote(self,magazine,words):
        
        dic= defaultdict(int)
        for word in magazine:
            dic[word] +=1    
        
        
        for c in w:
            if dic[c] <=0:
                return False 
            
            dic[c] -=1 
            
        return True 
    
    
     
    def ransomNote2(self,mag,note):
        result = []
        index1= 0
        index2 =0
        
        while index1 < len(mag) and index2 < len(note):
            if mag[index1] == note[index2]:
                result.append(mag[index1])
                index1 +=1
                index2 +=1 
        print(result)                          
        if len(result) == len(note):
            return True 
        
        return False
        
class PermuteSolution(object):
    
    def isPermute(self,nums):
        
        pass 
        

class SortNumberSolution(object):
    
    def sortNumber(self,nums):
        
        one_index =0
        three_index = len(nums)-1
        index =0 
        
        while index < three_index:
            if nums[index] == 1:
                nums[index],nums[one_index] = nums[one_index],nums[index]
                
                one_index +=1
                index +=1
                
            if nums[index] == 2:
                index +=1
                
            if nums[index] == 3:
                nums[index],nums[three_index] = nums[three_index],nums[index]
                three_index -=1
                
        return nums 


class NonDupSolution(object):

    def nonDuplicateNumber(self,nums):
        
        dic = {}
        for n in nums:
            dic[n] = dic.get(n,0)+1
            
        for key, value in dic.items():
            if value == 1:
                return key 
            
        print(dic)
            
        return -1
    
class BinarySearchSolution(object):
    
    def findNumberUsingBinarySearch(self,nums,target):
        
        right =0
        left = len(nums)-1
        while right <=left:
            midpoint = (right+left)//2
            if nums[midpoint] == target:
                return midpoint
            elif target > nums[midpoint]:
                right = midpoint+1
            else:
                left = midpoint-1
                
        return -1
class SolutionsMoveZeros(object):
    
    def moveZerosToTheEnd(self,nums):
        
        right= 0 
        for num in nums:
            if num != 0:
                nums[right] = num
                right +=1
        
        for x in range(right,len(nums)):
            nums[x] = 0
        return nums 

class SolutionLongestSub(object):   
    def longestSubString(self,string):
        window_start = 0
        dic = {}
        maxLen = 0
        for i in range(len(string)):
            char = string[i]
            if char in dic and dic[char] >= window_start: 
                window_start = dic[char]+1
                
            dic[char] = i
            
            maxLen = max(maxLen,i-window_start+1)
            
        return maxLen

class Node(object):
    
    def __init__(self,val=0,next=None):
        
        self.val = val 
        self.next = next
        
   
   
   
"""
   Solutions to linked Lists questions beqin here . Test cases will be found in the tests.py 
"""     
class SolutionsToLinkListQuestions(object):
    
    def revereLinkedlink(self,head):  
        
      prev = None
      current = head    
      
      while current:
          
          temp = current.next
          current.next = prev 
          
          
          prev = current
          current = temp  
          

    def hasCycle(self,head):  
        
        node_set = set()
        current = head 
        
        while current:
            
            if current in node_set:
                return True 
            node_set.add(current) 
            
            current = current.next 
            
        return False 
        
            
        
    
    
    def hasCycle2(self,head):   
        
        slow = head 
        fast = head 
        
        while fast and fast.next:
            
            fast = fast.next.next 
            slow = slow.next 
            
            if slow == fast: 
                
                return True 
            
        return False 
      
    
    def middleNode(self,head):
       
        result = []
        current = head 
        
        while current:
            result.append(current)
            
            current = current.next 
        
        return result[len(result//2)]
        
        
    
    def middleNode2(self,head):
        
       pass 
            
            
    def removeNthNode(self,head):   
        
        pass 
    
    
    def removeElements(self,head,val):   
        
        pass  
    
    
    def mergeTwoSortedLinkedList(self,l1,l2):
        
       pass 




"""

Array Questions 

"""

class SolutionsToArrayQuestions(object):
   
    def reverseArrayInPlace(self,nums):
        
        right = 0
        left = len(nums)-1
        while right < left:
                nums[right],nums[left]= nums[left],nums[right]
            
                right +=1
                left -=1
        print(nums) 
            
        return nums 
    
    def isPalindrome(self,nums):
        
        results = []
        for i in range(len(nums)): 
            
            results.append(nums[i])
            
        print(results)
            
        return self.reverseArrayInPlace(nums) == results
    
    def reverseString(self,string): 
        #string_arr = list(string)
        string_arr = list(str(string))
        print(string_arr)
        right = 0
        left = len(string_arr)-1
        while right < left : 
            
            string_arr[right],string_arr[left] = string_arr[left],string_arr[right]
            
            right +=1
            left -=1 
            
        return int("".join(string_arr))
    
    def findDuplicate(self, nums):
    
        dic = {} 
        for num in nums:
            if num in dic:
                dic[num] +=1
            else:
                dic[num] = 1
                
        for key,value in dic.items():
            if value > 1:
                return key 
    
     
     
     
        """
        Strings Questions 
        """
class SolutionsToStringQuestions(object): 
    
    def isPalindrome(self,string):  
        
         # a string is a palindrome when the reverse characters is the same as the given string
         
        # s = re.sub(r'[\E\W_]','',string).lower()
         right =0
         left= len(string)-1
         while right < left :
             if string[right] != string[left]:  
                 
                return False 
             
                right +=1
                left -=1 
        
         return True

    def longestPalindromicSub(self,string):

        longest = ""
        for i in range(len(string)):
            for j in range(i,len(string)):
                substring = string[i:j+1]
                if len(substring) > len(longest) and self.isPalindrome(substring):
                    longest = substring

        return longest


    def isAnagram(self,s1,s2):
        if len(s1) != len(s2):
            return False
        dic = defaultdict(int)
        for char in s1:
            dic[char] +=1
        for char in s2:
            if char in dic: 
                dic[char] -=1
            else:
                dic[char] =1
        for k in dic:
            if dic[k] ==0:
                return True
        return False

    def groupAnagram(self,strs):
        dic = {}
        for word in strs:
            key = "".join(sorted(word))

            if key in dic:
                dic[key].append(word)
            else:
                dic[key] = [word]

        return list(dic.values())


    def validParenthesis(self,s):
        mapping = {"(":")","[":"]","{":"}"}
        stack = []
        for char in s :
            if char in mapping:
                stack.append(char)
            elif len(stack) == 0 or mapping[stack.pop()] != char:
                return False
        return len(stack) == 0

    def backspaceString(self,S,T):
        stack1 = []
        stack2 = []
        for char in S:
            if char == "#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(char)
        for char in T:
            if char == "#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(char)
        print(stack1)
        print(stack2)
        return len(stack1) == len(stack2)


#test = SolutionsToStringQuestions()
#print(test.backspaceString("a##c","#a#c"))











