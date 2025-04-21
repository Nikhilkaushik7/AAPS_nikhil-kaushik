# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 , p2 =  headA , headB
        count1 = count2 = 1
        while p1.next:
            count1 +=1
            p1= p1.next
        while p2.next:
            count2 +=1
            p2 = p2.next
        diff = abs(count1-count2)
        pA, pB = headA, headB
        if count1 > count2:
            for _ in range(diff):
                pA = pA.next
        else:
            for _ in range(diff):
                pB = pB.next

        while pA and pB:
            if pA == pB:
                return pA
            pA = pA.next
            pB = pB.next
        
        return None  

        

        