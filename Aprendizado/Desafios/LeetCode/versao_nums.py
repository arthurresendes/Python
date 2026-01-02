class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        
        version1 = int(version1[1])
        version2 = int(version2[1])
        if version1 > version2:
            return 1
        elif version1 < version2:
            return -1
        else:
            return 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.compareVersion("1.2","1.10"))
    print(sol.compareVersion("1.01","1.001"))
    print(sol.compareVersion("1.0","1.000"))
    print(sol.compareVersion("1.42","1.5"))