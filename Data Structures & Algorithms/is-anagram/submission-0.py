class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wordMap = {}
        wordMapTwo = {}
        for i in s:
            if i not in wordMap:
                wordMap[i] = 1
            else:
                wordMap[i] += 1
        
        for i in t:
            if i not in wordMapTwo:
                wordMapTwo[i] = 1
            else:
                wordMapTwo[i] += 1
        return (wordMap == wordMapTwo)
        