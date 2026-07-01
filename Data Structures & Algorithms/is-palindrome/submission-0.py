class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointOne = 0
        sCheck = ''.join(char for char in s if char.isalnum())
        pointTwo = len(sCheck) - 1
        sCheck = sCheck.lower()
        print(sCheck)
        while(pointOne < pointTwo):
            if sCheck[pointOne] != sCheck[pointTwo]:
                return False
            print(pointOne)
            print(pointTwo)
            pointOne += 1
            pointTwo -= 1

        return True
        