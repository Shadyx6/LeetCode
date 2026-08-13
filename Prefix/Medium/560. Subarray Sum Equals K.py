class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        store = {0:1}
        count = 0
        total=0
        for i in range(0, len(nums)):
            total+=nums[i]
            need = total - k
            if need in store:
                count+= store[need]
            store[total] = store.get(total, 0)+1

        return count