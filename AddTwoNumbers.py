# Definition for singly-linked list.

# class ListNode:

#     def __init__(self, x):

#         self.val = x

#         self.next = None



class Solution:

    # @param {ListNode} l1

    # @param {ListNode} l2

    # @return {ListNode}

    def addTwoNumbers(self, l1, l2):

        def toint(l):

            if l:

                return l.val+10*toint(l.next)

            return 0

        def tolist(it):

                node = ListNode(it%10)

                if it>9:

                    node.next = tolist(it/10)

                return node

        return tolist(toint(l1)+toint(l2))
