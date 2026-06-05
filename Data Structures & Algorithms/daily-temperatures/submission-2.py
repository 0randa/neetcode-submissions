class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = []

        for i in range(len(temperatures)):
            curr = temperatures[i]
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ans.append(j - i)
                    break
            else:
                ans.append(0)

        return ans
