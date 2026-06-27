class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        listy = []

        for i,n in enumerate(nums):
            if n not in hmap:
                hmap[n] = 1
            else:
                hmap[n] += 1
            
        thevals = sorted(list(hmap.values()))
        thevals = thevals[len(thevals)-k:len(thevals):]

        for i,n in enumerate(hmap):
            if hmap[n] in thevals:
                listy.append(n)
        return listy
    


