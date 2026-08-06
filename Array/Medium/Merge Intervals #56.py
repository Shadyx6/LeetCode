class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n= len(intervals)
        ans = [intervals[0]]

        for i in range(1,n):
            intStart , intEnd = intervals[i]
            ansStart, ansEnd = ans[-1]

            if intStart <= ansEnd:
                ans[-1][1] = max(intEnd, ansEnd)
            else:
                ans.append([intStart, intEnd])

        return ans