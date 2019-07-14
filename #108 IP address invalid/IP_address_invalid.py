#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

# 个人思路：IP地址都是由“.”分割开的，可以找到“.”替换即可

"""
mothed one
遍历一次str，如果是.则替换为[.]，如果不是则加入str中
"""

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        nums = address.split('.')
        ans = nums[0]
        for i in range(1, len(nums)):
            ans += '[.]' + nums[i]

        return ans

"""
mothed two
利用python自带函数，将字符串分割。分割后的数组元素中插入[.]
"""

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        nums = address.split('.')
        ans = nums[0]
        for i in range(1, len(nums)):
            ans += '[.]' + nums[i]

        return ans

"""
mothed three
直接利用python的函数，进行替换
"""

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        ans = address.replace('.', '[.]')
        return ans
