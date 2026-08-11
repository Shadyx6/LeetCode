class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def square(num):
            return num*num
        n = len(nums)
        left = 0
        right = n-1
        res = [0] * n
        pos = n-1

        while left <=right:
            if square(nums[left]) >square(nums[right]):
                res[pos] = square(nums[left])
                pos-=1
                left+=1
            else:
                res[pos] = square(nums[right])
                right-=1
                pos-=1
        
        return res 
            


