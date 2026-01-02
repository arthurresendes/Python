class Solution:
    def isPalindrome(self, x: int) -> bool:
        numero_teste = str(x)
        if '-' in numero_teste:
            return False
        invertendo = numero_teste[::-1]
        numero_teste = int(invertendo)
        if x == numero_teste:
            return True
        else:
            return False
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(-121))
    print(sol.isPalindrome(121))
    print(sol.isPalindrome(10))