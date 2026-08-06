class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        collection= {i: True for i in nums}
        missing =[]
        start = min(nums)
        end = max(nums)

        for i in range(start, end+1):
            if i not in collection:
                missing.append(i)
        return missing
