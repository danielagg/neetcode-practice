from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = {i for i in nums}
        return len(hashSet) != len(nums)

    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


print(Solution().isAnagram("test", "tsset"))
