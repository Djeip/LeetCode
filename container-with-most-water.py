"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of
the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


class Solution:
    def maxArea(self, height: list) -> int:
        r = len(height) - 1
        l = 0
        maxx = 0

        mh = max(height)

        while l != r:
            cur = (r - l) * min(height[r], height[l])
            maxx = max(cur,maxx)

            if mh * (r - 1) <= maxx:
                break

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxx


if __name__ == '__main__':
    height = [1,3,2,5,25,24,5]
    sol = Solution()
    print(sol.maxArea(height))
