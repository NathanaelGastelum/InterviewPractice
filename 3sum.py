from typing import List


class Solution:
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        # Sort
        nums = sorted(nums)
        result = []
        # for each unique element in array, find a remaining pair that == 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            if len(nums) - i < 3:
                break
            
            lp = i + 1
            rp = len(nums) - 1
            # for each attempt, move a pointer
            while lp < rp:
                # record triplet if == 0
                if nums[i] + nums[lp] + nums[rp] == 0:
                    result.append([nums[i], nums[lp], nums[rp]])
                    lp = lp + 1
                    while nums[lp] == nums[lp-1] and lp < rp:
                        lp = lp + 1

                # increase: left pointer to the right if too small 
                if nums[i] + nums[lp] + nums[rp] < 0:
                    lp = lp + 1
                    

                # decrease: right pointer to the left if too large
                if nums[i] + nums[lp] + nums[rp] > 0:
                    rp = rp - 1

        return result

actual = Solution.threeSum([-1,-1,0,1,2,-1,-4])
expected = [[-1,-1,2],[-1,0,1]]
assert actual == expected
