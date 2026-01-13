class Solution:
    def twoSum(self, lista: list[int], target: int) -> list[int]:
        for i in range(len(lista) - 1):
            if lista[i] + lista[i+1] == target:
                return [i, i+1]
            
        


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([1,2,3,4,5,6],3))
    print(sol.twoSum([1,2,3,4,5,6],11))
