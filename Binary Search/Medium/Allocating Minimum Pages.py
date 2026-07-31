class Solution:

    def findPages(self, pages, k):

        if k > len(pages):
            return -1

        low = max(pages)
        high = sum(pages)

        answer = high

        while low <= high:

            mid = (low + high) // 2

            students = 1
            currentPages = 0

            for page in pages:

                if currentPages + page <= mid:
                    currentPages += page
                else:
                    students += 1
                    currentPages = page

            if students <= k:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer