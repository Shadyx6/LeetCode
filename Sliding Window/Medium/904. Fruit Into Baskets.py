class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0
        store = {}
        maxBas = 0
        while r < len(fruits):
            store[fruits[r]] = store.get(fruits[r], 0) + 1
            while len(store) > 2:
                store[fruits[l]] -= 1
                if store[fruits[l]] == 0:
                    del store[fruits[l]]
                l+=1
            maxBas = max(maxBas, r -l+1)
            r+=1

        return maxBas
            