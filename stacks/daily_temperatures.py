class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for idx in range(len(temperatures)):
            temp = temperatures[idx]
            while len(stack) > 0 and temp > stack[-1][0]:
                [val, i] = stack.pop()
                temperatures[i] = idx - i
            stack.append([temp,idx])
        for val, i in stack:
            temperatures[i] = 0
        return temperatures
