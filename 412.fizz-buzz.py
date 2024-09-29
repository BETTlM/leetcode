#
# @lc app=leetcode id=412 lang=python
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rl = []
        for i in range(1,n+1):
            if i%15==0:
                rl.append('FizzBuzz')
            elif i%3==0:
                rl.append('Fizz')
            elif i%5==0:
                rl.append('Buzz')
            else:
                rl.append(str(i))
        return rl
        
# @lc code=end

