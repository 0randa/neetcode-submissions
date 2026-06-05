class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create tuples out of arrays, and use the tuples as keys

        # for each letter, we count their frequencies, and turn them into tuples, so like each index represents a letter and the value is the frequency of that letter

        # for example Array[0] = 2, then that means 'a' appeared twice.


        empty_arr = [0] * 26

        ans = defaultdict(list)

        for s in strs:
            for letter in s:
                _ascii = ord(letter) - 97
                empty_arr[_ascii] += 1
            
            
            tuple_array = tuple(empty_arr.copy())
            ans[tuple_array].append(s)
            empty_arr = [0] * 26


        return list(ans.values())

            


