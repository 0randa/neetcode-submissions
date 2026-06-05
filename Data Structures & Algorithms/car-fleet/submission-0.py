class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = list(zip(position, speed))

        sorted_data = sorted(combined, reverse=True)
        stack = []
        for position, speed in sorted_data:
            time = (target - position) / speed
            if not stack:
                stack.append(time)
            
            top = stack[-1]
            # if the curr car time is <= the top of the stack, it joins the same fleet
            if time <= top:
                continue
            # else it forms a new fleet
            else:
                stack.append(time)


        return len(stack)


        return 0