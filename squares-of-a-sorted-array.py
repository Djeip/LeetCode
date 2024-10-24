"""
977. Squares of a Sorted Array
Easy

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [x ** 2 for x in nums]
        return self.qsort(nums)

    def qsort(self,arr):
        if len(arr) <= 1:
            return arr
        else:
            return self.qsort([x for x in arr[1:] if x < arr[0]]) + [arr[0]] + self.qsort([x for x in arr[1:] if x >= arr[0]])

class Solution_ez:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        numbs = []
        for i in nums:
            i *= i
            numbs.append(i)
        return sorted(numbs)

if __name__ == '__main__':
    nums = [-7, -3, 2, 3, 11]
    sol = Solution_ez()
    print(sol.sortedSquares(nums))
