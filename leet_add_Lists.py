# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def __init__(self):
        pass
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = ListNode(val = (l1.val+l2.val)%10 , next = None)
        l3 = curr
        carry = (l1.val+l2.val)//10
        while l1.next != None or l2.next != None:
            if l1.next != None and l2.next != None:
                val = carry + l1.next.val+l2.next.val
                carry = val // 10
                print(val, carry, val %10)
                curr.next = ListNode(val = val % 10 , next = None)
                curr = curr.next
                l1 = l1.next
                l2 = l2.next 
            elif l1.next != None and l2.next == None:
                val = carry + l1.next.val
                carry = val // 10
                curr.next = ListNode(val = val % 10 , next = None)
                curr = curr.next
                l1 = l1.next
            elif l1.next == None and l2.next != None:
                val = carry + l2.next.val
                carry = val // 10
                curr.next = ListNode(val = val % 10 , next = None)
                curr = curr.next
                l2 = l2.next
        if carry > 0:
            curr.next = ListNode(val = carry , next = None)
            curr = curr.next
        return l3

if __name__ == "__main__":
    l1 = ListNode(9) #43
    l1.next = ListNode(9) #43
    l1.next.next = ListNode(9) #43
    l2 = ListNode(9) #43
    l2.next = ListNode(9) #43
    l2.next.next = ListNode(9) #43


    S = Solution()
    l3 = S.addTwoNumbers(l1,l2)
    a = []
    while l3: 
        # print(l3.val, l2.val, l1.val)
        a.append(l3.val)
        l3 = l3.next
    print(a)
