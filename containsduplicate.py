nums = [1,2,3,1]
output = True

class Solution(object):
    def containsDuplicate(self, nums):
        cache = list()
        for i in nums:
            if i in cache:
                return True
            else: cache.append(i)
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
if __name__ == "__main__":
    s = Solution()
    if s.containsDuplicate(nums) == output:
        print("Correct")
    else: print("Wrong")