class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res, sol = [], []

        def isPali(string):
            return string == string[::-1]


        def dfs(start,end):
            if end >= len(s):
                if start == end:
                    res.append(sol[:])
                return

            # decision 1: partition and start a new string

            partition = s[start:end+1]

            if isPali(partition):
                sol.append(partition)
                dfs(end + 1, end + 1)
                sol.pop()

            # decision 2: continue without partitioning 
            dfs(start, end + 1)

        

        dfs(0 , 0)
        return res