"""
480. Sliding Window Median
Hard

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation:
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6
Example 2:

Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]


Constraints:

1 <= k <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
"""

from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        if len(nums) > 0:
            w = sorted(nums[:k])
            n = k // 2

            if k % 2 == 0:
                res.append((w[n] + w[n - 1]) / 2)
                for i in range(0, len(nums) - k):
                    w.remove(nums[i])
                    f = (k - 1) // 2

                    c = nums[i + k]

                    if w[f - 1] <= c <= w[f]:
                        pass
                    else:
                        while f > 0 and c < w[f - 1]:
                            f -= 1
                        while f < k - 1 and c > w[f]:
                            f += 1
                    w.insert(f, c)

                    res.append((w[n] + w[n - 1]) / 2)
            else:
                res.append(w[n])
                for i in range(0, len(nums) - k):
                    w.remove(nums[i])
                    f = (k - 1) // 2

                    c = nums[i + k]

                    if w[f - 1] <= c <= w[f]:
                        pass
                    else:
                        while f > 0 and c < w[f - 1]:
                            f -= 1
                        while f < k - 1 and c > w[f]:
                            f += 1

                    w.insert(f, c)
                    res.append(w[n])

        return res


def insertion(num, lst, k):
    l = (k - 1) // 2
    print(l)
    lst_ = lst.copy()
    if lst[l - 1] <= num <= lst[l]:
        pass
    else:
        while l > 0 and num < lst[l - 1]:
            l -= 1
            print('-', l)
        while l < k and num > lst[l]:
            l += 1
            print('+', l)
    lst_.insert(l, num)
    return lst_


from sortedcontainers import SortedList


# last Solution works too long without using specific data structures like heap queue and sortedList

class Solution_sorted:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lst = SortedList()  # maintain a sorted list

        res = []
        for i in range(len(nums)):
            lst.add(nums[i])  # O(logk)
            if len(lst) > k:
                lst.remove(nums[i - k])  # if we use heapq here, it will take O(k), but for sortedList, it takes O(logk)
            if len(lst) == k:
                median = lst[k // 2] if k % 2 == 1 else (lst[k // 2 - 1] + lst[k // 2]) / 2
                res.append(median)

        return res


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    cls = Solution_sorted()
    print(cls.medianSlidingWindow(nums, k))


