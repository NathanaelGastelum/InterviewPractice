from typing import List


class Solution:
    @staticmethod
    def longestConsecutive(nums: List[int]) -> int:
        # Some kind of weird linked list type situation to do this in a constant number of passes:
        # 1st pass: get start and end values for each group of consecutive sequences
            # Use 2 dicts, one for starts:ends and the other for ends:starts
            # for each element, update start or end key
            # Connect groups when end and start are both consecutive to current value (so this check comes first)
            # handle duplicates with visited set
            # handle empty input

        # 2nd pass: get largest value for end - start

        # this is close to most optimal time,
            # but space and simplicity can be improved to just o(n) instead of o(2n)
            # time can also be o(n) even if length is saved as we go
        set_lengths = dict()
        longest = 0

        for num in nums:
            if num in set_lengths:
                continue
            
            if num - 1 in set_lengths and num + 1 in set_lengths:
                set_lengths[num] = set_lengths[num-1] + set_lengths[num+1] + 1
                # handle updating set boundaries
                set_lengths[num-set_lengths[num-1]] = set_lengths[num]
                set_lengths[num+set_lengths[num+1]] = set_lengths[num]
            elif num - 1 in set_lengths:
                set_lengths[num] = set_lengths[num-1] + 1
                set_lengths[num-set_lengths[num-1]] = set_lengths[num]
            elif num + 1 in set_lengths:
                set_lengths[num] = set_lengths[num+1] + 1
                set_lengths[num+set_lengths[num+1]] = set_lengths[num]
            else:
                set_lengths[num] = 1

            if set_lengths[num] > longest:
                longest = set_lengths[num]
            
        return longest

actual = Solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
expected = 9
assert actual == expected, f"Test: expected: {expected}, recieved: {actual}"

actual = Solution.longestConsecutive([])
expected = 0
assert actual == expected, f"Test: expected: {expected}, recieved: {actual}"
