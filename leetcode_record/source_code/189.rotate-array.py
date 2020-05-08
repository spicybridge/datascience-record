#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:

    def euclid(self, num1:int, num2:int) -> int:
        m = max(num1, num2)
        n = min(num1, num2)
        r = m % n
        while r != 0:
            m = n
            n = r
            r = m % n
        return n

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums:
            length = len(nums)
            k = k % length
            if k != 0:
                loop = self.euclid(length, k)
                times = int(length / loop)
                for i in range(loop):
                    index = i
                    temp1 = nums[i]
                    for j in range(times):
                        temp2 = nums[(index+k) % length]
                        nums[(index+k) % length] = temp1
                        temp1 = temp2
                        index = (index+k) % length

# @lc code=end

