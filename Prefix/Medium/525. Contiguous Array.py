class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        store = {0:-1}
        prefixSum = 0
        maxLen = 0
        for i in range(0, len(nums)):
            print(nums[i])
            if nums[i] == 0:
                prefixSum-=1
            else:
                prefixSum+=1
            # print(prefixSum)
            if prefixSum in store:
                print("yes")
                maxLen = max(maxLen, i - store[prefixSum])
            else:
                store[prefixSum] = i           
        return maxLen           