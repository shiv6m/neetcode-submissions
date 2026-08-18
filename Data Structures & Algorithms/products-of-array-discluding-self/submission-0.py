class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        total = 1
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
                continue
            total *= num

        if zeros >= 2:
            return output
        elif zeros == 1:
            for i, n in enumerate(nums):
                if n == 0:
                    output[i] = total
            return output
        else: 
            for i, n in enumerate(nums):
                output[i] = total//n
            return output
            


