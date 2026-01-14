class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in t:
            if i in s:
                pass
            else:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram","nagaram"))
    print(sol.isAnagram("rat","cat"))