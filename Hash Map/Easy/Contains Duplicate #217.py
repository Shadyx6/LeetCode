class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        keys = set()
        for i in nums:
            if i in keys:
                return True
            keys.add(i)

        return False