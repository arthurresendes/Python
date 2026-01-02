class Solution:
    def calculate(self, s: str) -> int:
        resultado = eval(s)
        return resultado
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.calculate("3+2*2"))