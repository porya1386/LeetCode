# LeetCode: 1. Two Sum
# Question in FA = 
# Ma list i az adad darim mesal numps = [2,7,11,15] va target = 9 
# bayad index haye do adad ra barmigardanad ke majmooe anha barabar ba target bashad.
# Ba hashmap
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            compelet = target - nums[i] #‌ First key then value 5 : 1
            if compelet in seen:
                return seen[compelet], i
            seen[nums[i]] = i
# Ba nested loop
#‌ with nested loops if we have a lot of item in our list the time will be more and more O(n²)
nums = [3,4,5]
target = 9
for i in range(len(nums)):
    for j in range(i + 1,len(nums)):
        if nums[i] + nums[j] == target:
            print(i,j)
