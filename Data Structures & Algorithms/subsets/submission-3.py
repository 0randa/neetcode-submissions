class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        solution = []
        subsets = []
        def answer(start_index):
            # base case: index out of bounds
            if start_index >= len(nums):
                solution.append(subsets.copy())
                return solution
            
            # decision problem

            # 1: add an item to the subet
            subsets.append(nums[start_index])
            answer(start_index + 1)
            subsets.pop()
            # 2: don't add an item to the subset
            answer(start_index + 1)

        answer(0)
        return solution
