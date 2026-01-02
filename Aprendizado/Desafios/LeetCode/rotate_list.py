class Solution:
    def rotateRight(self, head: list[int], k: int) -> list[int]:
        for _ in range(k):
            elemento = head.pop()
            head.insert(0, elemento)
        return head

if __name__ == "__main__":
    sol = Solution()
    print(sol.rotateRight([1,2,3,4,5],2))
    print(sol.rotateRight([0,1,2],4))