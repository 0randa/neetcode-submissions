class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1


        while True:

            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            # if its less than target, increment the left pointer
            elif numbers[l] + numbers[r] < target:
                l += 1
            # if its greater than target, decrement the right pointer
            elif numbers[l] + numbers[r] > target:
                r -= 1


