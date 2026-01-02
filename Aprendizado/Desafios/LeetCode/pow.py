class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n


if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(2.0,10))
    print(sol.myPow(2.100,3))
    print(sol.myPow(2.000,-2))
