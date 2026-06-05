class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []

        dictionary = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z'],
            "0": ['+']
        }

        def dfs(i, sol):
            if len(sol) == len(digits):
                res.append("".join(sol))
                return

            if i >= len(digits):
                return

            curr_digit = digits[i]
            letters_for_digit = dictionary[curr_digit]

            for letter in letters_for_digit:
                # add cur letter
                sol.append(letter)
                # recurse
                dfs(i + 1, sol)
                # backtrack
                sol.pop()


        dfs(0, [])
        return res