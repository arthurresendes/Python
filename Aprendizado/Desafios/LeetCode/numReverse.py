class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)[::-1]
        lista = []
        for i in x_str:
            lista.append(i)
       
        if '-' in lista:
            lista.remove('-')
            res = '-'
        else:
            res = ''

        for i in lista:
            res = res + i
           
       
        return int(res)

if __name__ == "__main__":
    solucao = Solution()
    print(solucao.reverse(121))
    print(solucao.reverse(-321))
    print(solucao.reverse(120))