class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        col = {}
        for i in nums:
            col[i] = col.get(i, 0) + 1
        answer = sorted(col, key=col.get, reverse=True)
        # print(sorted(col), answer)
        return answer[:k]