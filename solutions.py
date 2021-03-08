from collections import defaultdict
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
        
        
        for c in note:
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
        
        self.isPermuteHelper(nums,start)
        

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
        
        
class SolutionsToLinkListQuestions(object):
    
    def revereLinkedlink(self,head):  
        
        prev = None 
        current = head 
        while current :
            temp = current.next 
            current.next = prev
            
            prev = current 
            current = temp 
            
        return prev  
    
    
    def hasCycle(self,head):  
        
        node_set = set()
        
        while head: 
            
            if head in node_set: 
                return True 
            node_set.add(head)
            
            head = head.next 
            
        return False  
    
    
    def hasCycle2(self,head):   
        
        fast = head 
        slow = head 
        
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
            
        return False
    
    def middleNode(self,head):
        result = []
        while head:  
            result.append(head) 
            
            head = head.next  
            
        return result[len(result//2)]
    
    
    def middleNode2(self,head):
        
        fast = head
        slow = head 
        while fast  and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            
        return slow 
            
    
      
    
    
    
        
        
                 
                