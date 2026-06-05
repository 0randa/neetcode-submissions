class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret_array = []
        temp_len = len(temperatures) - 1

        if temp_len == 0:
            return [0]

        # loop through the array except for the last one
        for i in range(temp_len):
            found = False
            k = 1
            for j in range(i + 1, temp_len + 1):
                if temperatures[j] > temperatures[i]:
                    found = True
                    ret_array.append(k)
                    break
                k += 1

            if not found:
                ret_array.append(0)

        ret_array.append(0)
        return ret_array