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

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        scores = {}

        for num in nums:
            if num in scores:
                scores[num] += 1
            else:
                scores[num] = 1

        sortedScores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        topKSortedScores = sortedScores[:k]

        return [score[0] for score in topKSortedScores]

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        prefix_sum = 1
        for i in range(len(nums)):
            result[i] = prefix_sum
            prefix_sum *= nums[i]

        postfix_sum = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix_sum
            postfix_sum *= nums[i]

        return result


print(Solution().productExceptSelf([1, 2, 3, 4]))
