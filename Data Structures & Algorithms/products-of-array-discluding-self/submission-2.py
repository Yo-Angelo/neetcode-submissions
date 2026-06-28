class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productList = []
        count = 0
        product = 1
        while(count != len(nums)):
            for i in range(len(nums)):
                if (i == count):
                    continue
                else:
                    product *= nums[i]
            productList.append(product)
            product = 1
            count+= 1
        return productList


        
        