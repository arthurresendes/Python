class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        juncao_listas = nums1 + nums2
        juncao_listas.sort()
        meio = len(juncao_listas) // 2
        mediana = 0
        if len(juncao_listas) % 2 == 0:
            mediana = (juncao_listas[meio -1] + juncao_listas[meio]) / 2
        else:
                mediana  = juncao_listas[meio]
       
        return float(mediana)


if __name__ == "__main__":
    solucao = Solution()
    print(solucao.findMedianSortedArrays([1,2], [4,3]))
    print(solucao.findMedianSortedArrays([1,2], [3]))
    print(solucao.findMedianSortedArrays([1,2], [3,4,5]))
    print(solucao.findMedianSortedArrays([1,2,6], [3,4,5]))
