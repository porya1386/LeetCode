
nums = [2, 7, 11, 15]
target = 18

left = 0  # Starting from index 0
# Starting from last index in our list so -1 is 15 in this case
right = len(nums) - 1
for i in range(len(nums)):
    total = nums[left] + nums[right]  # left + right means 2 + 15 so 17
    if total == target:  # if 17 = 18
        print(nums[left], nums[right])  # print the numbers inside the list
        # print the index we did +1 so it start from 1 not 0 for leetcode question
        print(left + 1, right + 1)
        break
    elif total < target:  # if 17 < 18 , left index +1 so 2 -> 7
        left += 1
    else:  # if 18 > 17 , in this case it is so right index -1 15 -> 11
        right -= 1
        # This process is in one loop so O(n) and everytime total its not == target we close the gap from left and right untill we get the anwser


# For leet code
class Solution:
    # This is Python 3, and we're using type hints to make the expected input and return types clear.
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        right = len(numbers) - 1
        while left < right:  # it continue untill we get left == right that means left and right get into same index i guss
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1

    # sorry if my comment are fkdup
