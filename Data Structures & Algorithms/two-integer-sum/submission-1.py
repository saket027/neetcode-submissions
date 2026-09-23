class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countmap = {}
        for ind, val in enumerate(nums):
            compliment = target - val
            if compliment in countmap:
                return [countmap[compliment], ind]
            countmap[val] = ind
