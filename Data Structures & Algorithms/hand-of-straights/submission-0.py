class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        # sort them and pop them.

        hand.sort()

        print(hand)
        
        # utilise a priority queue of some sorts.
        _counter = (Counter(hand))

        # iterate through the counter, and check if i... i+3, have their frequencies
        
        for i, h in enumerate(hand):
            print(h)

            if _counter[h] == 0:
                continue

            for h2 in range(h, h+groupSize):
                if h2 not in _counter or _counter[h2] == 0:
                    return False
                _counter[h2] -= 1

            print()
        
        return True