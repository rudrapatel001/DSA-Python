class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
            
        return True

# Test cases
solution = Solution()

# Test case 1
s = "anagram"
t = "nagaram"
print(solution.isAnagram(s, t))  # Expected output: True

# Test case 2
s = "rat"
t = "car"
print(solution.isAnagram(s, t))  # Expected output: False

# Test case 3 (empty strings)
s = ""
t = ""
print(solution.isAnagram(s, t))  # Expected output: True
