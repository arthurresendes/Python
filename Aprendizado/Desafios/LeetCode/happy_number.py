class Solution:
    def isHappy(self, n: int) -> bool:
        n1, n2 = map(int, str(n))
        n1 = n1** 2
        n2 = n2** 2
        return n1+n2

if __name__ == "__main__":
    sol = Solution()
    print(sol.isHappy(19))
    print(sol.isHappy(82))