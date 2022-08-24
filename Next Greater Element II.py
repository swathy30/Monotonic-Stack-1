class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        result = [-1] * len(nums)
        mstack =[]
        
        for i in range(2*(len(nums))):
            while(len(mstack)!=0 and nums[mstack[-1]]<nums[i%len(nums)]):
                greatest = nums[i%len(nums)]
                result[mstack[-1]] = greatest
                mstack.pop()
                
            if i<len(nums):
                mstack.append(i)
                
        return result