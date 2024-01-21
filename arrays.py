from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = {i for i in nums}
        return len(hashSet) != len(nums)

    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for i, n in enumerate(nums):
            lookingFor = target - n
            if lookingFor in numbers:
                return [i, numbers[lookingFor]]

            numbers[n] = i
        return []

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            asSorted = "".join(sorted(word))

            if asSorted in anagrams:
                anagrams[asSorted].append(word)
            else:
                anagrams[asSorted] = [word]

        return list(anagrams.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
