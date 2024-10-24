"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.



Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]

"""

s_ = "ababcbacadefegdehijhklij"


class Solution:
    def partitionLabels(self, s: str):
        last = {c: i for i, c in enumerate(s)}
        mx = j = 0
        res = []
        for i, c in enumerate(s):
            mx = max(mx, last[c])
            if mx == i:
                res.append(i - j + 1)
                j = i + 1
        return res


if __name__ == "__main__":
    cls = Solution()
    print(cls.partitionLabels(s_))
