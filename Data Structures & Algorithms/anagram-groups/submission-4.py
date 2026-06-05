class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create tuples out of arrays, and use the tuples as keys

        # for each letter, we count their frequencies, and turn them into tuples, so like each index represents a letter and the value is the frequency of that letter

        # for example Array[0] = 2, then that means 'a' appeared twice.

        # O(1)
        empty_arr = [0] * 26

        # O(1)
        ans = defaultdict(list)

        # O(m) m strings
        for s in strs:

            # O(n)
            for letter in s:
                _ascii = ord(letter) - 97
                empty_arr[_ascii] += 1
            
            # O(n)
            tuple_array = tuple(empty_arr.copy())
            ans[tuple_array].append(s)
            empty_arr = [0] * 26


        # O(m)

        # FInally its O(m * n)
        return list(ans.values())

            


