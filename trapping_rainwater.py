from typing import List

class Solution:
    @staticmethod
    def trap(height: List[int]) -> int:
        # 2 pointers at opposite ends
        p1 = 0
        p2 = len(height) - 1
        l_max = height[p1]
        r_max = height[p2]
        total = 0

        # move shorter until p2 >= p1
        while p1 < p2:
            if height[p1] <= height[p2]:
                p1 += 1
                # get water above current height
                if height[p1] < l_max:
                    total += l_max - height[p1]
                # update max edge height
                l_max = max(l_max, height[p1])
            else:
                p2 -= 1

                if height[p2] < r_max:
                    total += r_max - height[p2]
                r_max = max(r_max, height[p2])

        return total


print(Solution.trap([4,2,0,3,2,5]))