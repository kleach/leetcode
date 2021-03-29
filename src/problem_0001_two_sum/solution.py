from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = dict()
        for i in range(len(nums)):
            num_map[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_map.keys() and num_map[complement] != i:
                return [i, num_map[complement]]
