from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = {i for i in nums}
        return len(hashSet) != len(nums)
