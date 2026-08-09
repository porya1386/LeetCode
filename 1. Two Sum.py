# LeetCode: 1. Two Sum
# Question in FA = 
# Ma list i az adad darim mesal numps = [2,7,11,15] va target = 9 
# bayad index haye do adad ra barmigardanad ke majmooe anha barabar ba target bashad.
class Solution(object):
    def twoSum(self, nums, target):
        _nums = {}
        lenght = len(nums)
        for i in range(lenght):
            val = target - nums[i]
            if val in _nums:
                return [i,_nums[val]]
            _nums[nums[i]]=i