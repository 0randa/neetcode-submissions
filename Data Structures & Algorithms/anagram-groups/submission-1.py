class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # have a lookup table, and we would give each anagram an index.
        array = []

        for s in strs:
            if not array:
                array.append([s])
            else:
                # check the string with the first element of every element in the array
                
                new_array = False

                for a in array:
                    # so it is a valid anagram
                    if Counter(a[0]) == Counter(s):
                        # chuck it into the array
                        new_array = True
                        a.append(s)
                        # then break out of the loop, since there is no need
                        break

                if not new_array:
                    array.append([s])


        print(array)
        return array
