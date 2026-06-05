class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(timestamp, value)]
        else:
            self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        arr = self.store[key]
        l, r = 0, len(arr) - 1

        while l <= r:
            middle = (l + r) // 2
            curr_timestamp = arr[middle][0]
            
            if curr_timestamp == timestamp:
                return arr[middle][1]
            elif curr_timestamp < timestamp:
                l = middle + 1
            else:
                r = middle - 1
        
        if r >= 0:
            return arr[r][1]
        return ""