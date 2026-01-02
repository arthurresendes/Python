class Solution:
    def mySqrt(self, x: int) -> int:
        x = x ** 0.5
        return x

if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(100))