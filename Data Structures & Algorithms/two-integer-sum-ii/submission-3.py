class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complement = {}

        for index, num in enumerate(numbers):
            comp = target - num

            if comp in complement:
                return [complement[comp], index]
            
            complement[comp] = index

        for index, num in enumerate(numbers):
            if num in complement:
                return [index + 1, complement[num] + 1]
