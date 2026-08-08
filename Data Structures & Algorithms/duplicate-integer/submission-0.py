class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exclude_duplicates = set(nums)
        return len(nums) != len(exclude_duplicates)