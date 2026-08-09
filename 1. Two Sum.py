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
# _nums baraye zakhire kardan adad ha va index haye anha estefade mishavad.
# lenght baraye daryafte tool list estefade mishavad.
# for loop baraye daryafte index haye list estefade mishavad.
# val baraye mohasebe adad marboot be target estefade mishavad.
# if val dar _nums bashad, yani adad marboot be target dar list vojood darad va index haye anha barmigardanad.
# _nums[nums[i]]=i baraye zakhire kardan adad va index haye anha dar _nums estefade mishavad.