class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        answer = [-1] * n
        for i in range(2 * n):
            while len(stack) > 0 and nums[stack[-1]] < nums[i%n]:
                answer[stack[-1]] = nums[i%n]
                stack.pop()
            if i < n:
                stack.append(i)

        return answer


