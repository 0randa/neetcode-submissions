from pprint import pprint

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # create a dictionary which represents the 

        if len(s1) > len(s2):
            return False
        # checking if both dictionaries are equal will take O(26) which is constant time

        # we will also be using constant space

        l = 0

        counter1 = Counter(s1)

        pprint(counter1)

        for l in range(len(s2) - len(s1)):
            # once we encounter 
            if s2[l] in s1:
                r = l
                new_counter = Counter()
                while r - l < len(s1):
                    new_counter[s2[r]] += 1
                    r += 1
                
                print(new_counter, counter1)
                print("what")
                if new_counter == counter1:
                    return True



        return False


