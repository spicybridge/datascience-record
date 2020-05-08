#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = 0
        exp_num = nums[0]
        switch = 0
        for i in nums:
            if exp_num != i:
                switch = 1
                length += 1
                exp_num = i
                nums[length-1] = i
            else:
                switch += 1
                if switch < 3:
                    length += 1
                    nums[length-1] = i
        return length
# @lc code=end