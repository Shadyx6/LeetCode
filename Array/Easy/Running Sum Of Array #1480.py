class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        print(n)
        for i in range(0,n):
            if i ==0:
                ans.append(nums[i])
                continue
            ans.append(ans[i-1] + nums[i])
        return ans
            