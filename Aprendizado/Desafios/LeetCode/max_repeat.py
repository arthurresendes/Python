class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        maior_num = max(nums, key=nums.count)
        return maior_num
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.repeatedNTimes([1,2,2,2,3,3,3,3,3,4,5,5,6]))
    print(sol.repeatedNTimes([2,1,2,5,3,2]))
    print(sol.repeatedNTimes([5,1,5,2,5,3,5,4]))