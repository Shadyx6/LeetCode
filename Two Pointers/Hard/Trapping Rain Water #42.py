class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        leftMax =height[l]
        rightMax = height[r]
        totalWater = 0
        while l < r:
            leftMax = max(leftMax, height[l])
            rightMax = max(rightMax, height[r])
            if leftMax <= rightMax:
                current = height[l]
                totalWater+=leftMax - current
                l+=1
            if leftMax > rightMax:
                current = height[r]
                totalWater+=rightMax - current
                r-=1
        return totalWater
        