class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen_triplets = set()
        nums.sort()

        k = 0

        while k < len(nums) - 2:
            l, r = 0, len(nums) - 1
            while l < r:
                if l == k:
                    l += 1
                    continue
                elif r == k:
                    r -= 1
                    continue
                # less than then this means that l is too small
                if (nums[l] + nums[r] < -nums[k]):
                    l += 1
                elif (nums[l] + nums[r] > -nums[k]):
                    r -= 1
                else:
                    seen_triplets.add(tuple([nums[l], nums[r], nums[k]]))
                    break
            k += 1






        return [list(i) for i in seen_triplets]