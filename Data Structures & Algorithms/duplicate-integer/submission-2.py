class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # countmap = {}
        # for num in nums:
        #     if num in countmap:
        #         countmap[num] += 1
        #         return True
        #     countmap[num] = 1
        # return False
        return len(set(nums))< len(nums)