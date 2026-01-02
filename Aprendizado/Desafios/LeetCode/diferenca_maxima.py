class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        nums.sort()
        if len(nums) < 2:
            return 0
        diferenca = [j - i for i,j in zip(nums[:-1],  nums[1:])]
        return max(diferenca)

if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumGap([3,6,9,1]))
    print(sol.maximumGap([10]))
    print(sol.maximumGap([10,2]))