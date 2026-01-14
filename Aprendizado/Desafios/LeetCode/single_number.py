class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for i in nums:
            if nums.count(i) ==  1:
                return i
    
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([4,1,2,1,2]))
    print(sol.singleNumber([2,2,1]))
    print(sol.singleNumber([1,7,2,5,2,3,7,1,3]))
