class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        mono_stack = []
        for i in range(len(temperatures)):
            while mono_stack and mono_stack[-1][1] < temperatures[i]:
                index, _ = mono_stack.pop()
                res[index] = i - index
            mono_stack.append((i, temperatures[i]))
            print(mono_stack)

        return res
