class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        answer = [0] * (n)
        for i in range(0,n):
            # if len(stack) > 0:
            #     print(stack[-1], stack, temperatures[stack[-1]], tem)
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                print(i, stack[-1])
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return answer
            