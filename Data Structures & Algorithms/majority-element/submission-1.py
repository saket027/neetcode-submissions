class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        major_ele = 0
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = 0
            seen[nums[i]] += 1
        for i in seen:
            if seen[i] > len(nums) / 2:
                major_ele = i
        return major_ele