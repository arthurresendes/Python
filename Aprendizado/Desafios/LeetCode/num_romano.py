dicionario_romanos = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}

class Solution:
    def romanToInt(self, s: str) -> int:
        separando = list(s)
        res = 0
        for i in separando:
            for chave,valor in dicionario_romanos.items():
                if i == chave:
                    res += valor
        
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("III"))
    print(sol.romanToInt("LVIII"))
