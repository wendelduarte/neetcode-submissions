class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}


        for i, num in enumerate(nums):
            difference = target - num
            if (difference in mapp):
                return [mapp[difference], i]
            mapp[num] = i