class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        col = {}
        for i,j in enumerate(nums):
            if j in col and i - col[j] <=k:
                return True
            col[j] = i

        return False
