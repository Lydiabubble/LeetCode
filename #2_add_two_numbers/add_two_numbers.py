# -*- coding: UTF-8 -*-
#
# Copyright (c) 2020 Baidu.com, Inc. All Rights Reserved
#
"""
Author  : wangxueyi
Time    : 2020-07-07 23:13
"""

"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例1：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

class ListNode:
    """
    链表结构体
    """
    def __init__(self, x):
        self.val = x
        self.next = None


def init_listnode(data):
    # 把head单提出来，因为链表需要返回头指针
    head = ListNode(data[0])
    # 另一个指针指向头指针，逐一往后赋值
    node = head

    for i in data[1:]:
        # 赋值node下一个节点
        node.next = ListNode(i)
        # 指针往下移动
        node = node.next

    return head


def print_listnode(head):
    node = head
    while node:
        print(node.val)
        node = node.next


class Solution:
    # 初次解法
    def addTwoNumbers_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 头指针，赋值0，返回时从头指针的下一位开始返回
        head = ListNode(0)
        node = head

        # 进位值
        carry = 0
        while l1 or l2:
            # 判断l1 l2是否为none，为none赋值为0
            if l1 and not l2:
                tmp_val = l1.val + 0 + carry
            elif not l1 and l2:
                tmp_val = l2.val + 0 + carry
            else:
                tmp_val = l1.val + l2.val + carry

            # //表示整数除法，获取下一个进位值
            carry = tmp_val // 10

            # 节点赋值个位数
            node.next = ListNode(tmp_val % 10)
            node = node.next

            # l1, l2 指向下一个节点
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry != 0:
            node.next = ListNode(carry)

        return head.next

    # 优化解法
    def addTwoNumbers_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 头指针，赋值0，返回时从头指针的下一位开始返回
        head = ListNode(0)
        node = head

        # 进位值
        carry = 0
        while l1 or l2:
            # 无论如何看起来这块都非常的冗余
            # if l1 and not l2:
            #     tmp_val = l1.val + 0 + carry
            # elif not l1 and l2:
            #     tmp_val = l2.val + 0 + carry
            # else:
            #     tmp_val = l1.val + l2.val + carry

            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            tmp_val = l1_val + l2_val + carry

            # //表示整数除法，获取下一个进位值
            carry = tmp_val // 10

            # 节点赋值个位数
            node.next = ListNode(tmp_val % 10)
            node = node.next

            # l1, l2 往下指
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry != 0:
            node.next = ListNode(carry)

        return head.next


if __name__ == '__main__':
    list1 = [2, 4, 3]
    list2 = [5, 6, 4]
    l1 = init_listnode(list1)
    l2 = init_listnode(list2)

    solution = Solution()
    node = solution.addTwoNumbers_1(l1, l2)
    print_listnode(node)
    print("************************")
    node = solution.addTwoNumbers_2(l1, l2)
    print_listnode(node)
