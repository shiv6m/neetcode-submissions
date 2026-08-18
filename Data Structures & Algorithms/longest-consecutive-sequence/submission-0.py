class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        highest = 0
        for num in nums:
            if num - 1 in hashset:
                continue
            else:
                current = num
                while (current + 1 in hashset):
                    current +=1
                length = current + 1 - num
                if length > highest:
                    highest = length
        return highest