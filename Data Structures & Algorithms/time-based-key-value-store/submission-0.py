class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        diction = self.store
        
        if key not in diction:
            diction[key] = [(timestamp, value)]
        else:
            diction[key].append((timestamp, value))

        return None

    def get(self, key: str, timestamp: int) -> str:
        diction = self.store

        if key not in diction:
            return ""
        arr = diction[key]

        arr_len = len(arr)
        if arr_len == 1:
            return arr[0][1]

        l, r = 0, arr_len - 1

        for item in arr:
            print(item)

        while l <= r:
            middle = (l + r) // 2
            curr_timestamp = arr[middle][0]

            if timestamp == curr_timestamp:
                return arr[middle][1]
            elif curr_timestamp < timestamp:
                l = middle + 1
            else: 
                r = middle - 1

        return arr[middle][1]
