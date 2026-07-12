class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        idx = 0
        for n in nums:
            if target - n in hm:
                return [hm[target-n], idx]
            else:
                hm[n] = idx
                idx += 1