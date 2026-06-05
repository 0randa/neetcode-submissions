class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        _Counter = Counter(nums)


        array = [[] for _ in range(len(nums))]

        ans = []
        for key,value in _Counter.items():
            array[value - 1].append(key)

        i = 0

        print(array)

        for value in array[::-1]:
            if i == k:
                break

            print(value)
            if not value:
                continue
            for v in value:
                ans.append(v)
                i += 1

        return ans
