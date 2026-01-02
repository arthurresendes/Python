class Solution:
    def removeNthFromEnd(self, head: list[int], n: int) -> list[int]:
        head = head[::-1]
        lista_res = []
        contador = 0
        for i in head:
            contador += 1
            if contador != n:
                lista_res.append(i)
        return lista_res[::-1]



if __name__ == "__main__":
    sol = Solution()
    print(sol.removeNthFromEnd([1,2,3,4,5],2))
    print(sol.removeNthFromEnd([1],1))
    print(sol.removeNthFromEnd([1,2],1))