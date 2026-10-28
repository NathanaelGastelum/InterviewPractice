from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    # O(1) space, so no hashmap
    # brute force: for each number, check every number after
    # better: binary search with the second pointer
    # best: 2 pointers, make current sum smaller or larger until target reached

    l_pointer = 0
    r_pointer = len(numbers) - 1
    
    while numbers[l_pointer] + numbers[r_pointer] != target:
        if numbers[l_pointer] + numbers[r_pointer] < target:
            l_pointer += 1
        elif numbers[l_pointer] + numbers[r_pointer] > target:
            r_pointer -= 1
    
    return [l_pointer + 1, r_pointer + 1]

twoSum([1,2,3,4], 3)