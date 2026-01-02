class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = int(num1)
        num2 = int(num2)
        res = num1 * num2
        return str(res)



if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply("2","3"))
    print(sol.multiply("123","456"))