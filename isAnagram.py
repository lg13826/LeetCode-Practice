s = "anagram" 
t = "nagaram"
output = True

class Solution(object):
    def isAnagram(self, s, t):
        s = sorted(s)
        t = sorted(t)
        if s == t: 
            return True
        else: False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

if __name__ == "__main__":
    sol = Solution()
    if sol.isAnagram(s, t) == output:
        print("Correct")
    else: print("Wrong")