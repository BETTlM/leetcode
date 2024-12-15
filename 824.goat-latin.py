#
# @lc app=leetcode id=824 lang=python
#
# [824] Goat Latin
#

# @lc code=start
class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        vowels = list('aeiou')
        words = ''
        count = 1
        old = sentence.split()
        for i in old:
            if i[0].lower() in vowels:
                i = i+"ma"
                i = i+("a"*count)
                i += ' '
                words+= (i)
            else:
                letter = i[0]
                i = i[1:]
                i = i+letter
                i=i+"ma"
                i=i+("a"*count)
                i += ' '
                words+= (i)
            count = count + 1
        return words[:-1]
        
# @lc code=end

