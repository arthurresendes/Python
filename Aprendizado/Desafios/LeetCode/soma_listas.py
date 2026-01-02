class Solution:
    def addTwoNumbers(self, l1: list[int], l2: list[int]) -> list[int]:
        l1 = l1[::-1]
        l2 = l2[::-1]
        juncao_l1 = "".join(map(str,l1))
        res1 = int(juncao_l1)
        
        juncao_l2 = "".join(map(str,l2))
        res2 = int(juncao_l2)
        
        soma = res1 + res2
        lista_res_str = list(str(soma))
        lista_res = [int(s) for s in lista_res_str]
        return lista_res[::-1]
    
    


if __name__ == "__main__":
    sol = Solution()
    print(sol.addTwoNumbers([2,4,3],[5,6,4]))
    print(sol.addTwoNumbers([0],[0]))
    print(sol.addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))