class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        thresh = 0
        n = len(people)
        l = 0
        r = n-1
        needed = 0
        people.sort()
        while l <=r:
            if people[l] + people[r] > limit:
                needed+=1
                r-=1
            else:
                l+=1
                needed +=1
                r-=1

        return needed