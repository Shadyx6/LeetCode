class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        collection = []
        nums.sort()
        for i in range(0,len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l<r:
                if nums[i] + nums[l]+nums[r] < 0:
                    l+=1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r-=1
                else:
                    collection.append([nums[i],nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l-1] == nums[l]:
                        l+=1
                    while l< r and nums[r] == nums[r+1]:
                        r-=1
        return collection
