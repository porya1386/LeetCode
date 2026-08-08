# LeetCode: 1. Two Sum


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Given a list of integers `nums` and an integer `target`,
        return the indices of the two numbers such that they add up to `target`.

        This implementation uses a single-pass hashmap (dictionary) to achieve
        O(n) time complexity and O(n) extra space. As we iterate through the
        list we store each number's index in the hashmap; for each number we
        check whether its complement (target - num) has already been seen.

        Args:
            nums (list[int]): A list of integers.
            target (int): The target sum to find.

        Returns:
            list[int]: A list containing the indices of the two numbers that add up to `target`.

        Raises:
            ValueError: If no two numbers sum up to the target.
        """
        seen: dict[int, int] = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        # If the problem guarantees a solution (as LeetCode does), this line
        # should never run; otherwise raise to make failure explicit.
        raise ValueError("No two sum solution")
