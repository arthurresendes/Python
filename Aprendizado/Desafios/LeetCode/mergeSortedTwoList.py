class Solution:
    def mergeTwoLists(self, list1: list[int], list2: list[int]) -> list[int]:
        lista_total = sorted(list1 + list2)
        return lista_total



if __name__ == "__main__":
    solucao = Solution()
    print(solucao.mergeTwoLists([1,2,4],[1,3,4]))
    print(solucao.mergeTwoLists([], [0]))