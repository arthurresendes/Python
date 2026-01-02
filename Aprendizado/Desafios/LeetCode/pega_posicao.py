class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lista_indice = []
        contador = 0
        for i in nums:
            if i == target:
                lista_indice.append(contador)
            contador += 1
        
        if len(lista_indice) == 0:
            return [-1,1]
        else:
            return lista_indice
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([5,7,7,8,8,10], 8))
    print(sol.searchRange([5,7,7,8,8,10], 6))
    print(sol.searchRange([], 0))
