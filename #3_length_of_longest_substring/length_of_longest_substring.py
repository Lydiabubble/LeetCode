# -*- coding: UTF-8 -*-
#
# Copyright (c) 2020 Baidu.com, Inc. All Rights Reserved
#
"""
Author  : wangxueyi
Time    : 2020-07-08 00:30
"""

"""
题目：给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例1：
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例2：
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例3：
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""

class Solution:
    def lengthOfLongestSubstring_1(self, s: str) -> int:
        """
        思路就是：
        i 指向被判断字符
        r 指向后续字符
        mark 记录i和r之前出现过的字符
        """
        res = 0
        mark = set()  # 用集合标明是否有出现重复字母
        r = 0  # 右指针
        for i in range(len(s)):
            if i != 0:
                """
                i - 1 --> i，判断字符改变，而这时mark中记录的还是 i - 1 到 r 之间存在的字符
                所以需要把 i - 1 的元素剔除，保留 i - 1 到 r 之间存在的字符
                """
                mark.remove(s[i - 1])
            """
            如果查看r是否存在于 i - 1 到 r - i之间的字符中
            """
            while r < len(s) and s[r] not in mark:  # 如果不满足条件说明r走到了s的尽头或r指向的元素
                """
                如果r不存在于 i - 1 到 r - i之间的字符中
                mark 加入r元素的值
                """
                mark.add(s[r])  # 将当前r指向的字母加入集合
                """
                r 继续指向下一个元素
                """
                r += 1

            """
            其实应该是 r - 1 元素到 i 元素的距离（包含 r-1 和 i ），应该是 r - 1 - i + 1 = r - i
            获得最大距离
            """
            res = max(res, r - i)  # 在每一个位置更新最大值
        return res

    def lengthOfLongestSubstring_2(self, s: str) -> int:
        max = 0
        r = 0
        char = []
        for i in range(len(s)):
            while r < len(s) and s[r] not in char:
                char.append(s[r])
                r += 1
            print(char)
            char.remove(s[i])
            if r - i > max:
                max = r - i

        return max

    def lengthOfLongestSubstring_3(self, s: str) -> int:
        """
        i在遍历str的时候，将每个字符作为key，当前pos作为value存入dict中
        当char没有在char_dict中时，说明从key到i没有重复的数字，所以最长长度为ans = max(ans, i - key)
        如果char在char_dict中，key到i中的第一个字符char是重复字符，将key移动到char上一个位置，也就是现在char_dict[char]
        移动后的key到i之前没有重复字符，继续循环直到i遍历完成
        """
        ans, key, char_dict = 0, -1, {}
        for i, char in enumerate(s):
            if char in char_dict and char_dict[char] > key:
                key = char_dict[char]
            else:
                ans = max(ans, i - key)
            char_dict[char] = i
        return ans


if __name__ == '__main__':
    s = "abcabcbb"
    solution = Solution()
    length = solution.lengthOfLongestSubstring_2(s)
    print(length)