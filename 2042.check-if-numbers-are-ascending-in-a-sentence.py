#
# @lc app=leetcode id=2042 lang=python
#
# [2042] Check if Numbers Are Ascending in a Sentence
#

# @lc code=start
class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        words = s.split()
        nums = []
        for word in words:
            if word.isdigit():
                nums.append(int(word))
        print(nums)

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                return False
        return True 
    
        
# @lc code=end

