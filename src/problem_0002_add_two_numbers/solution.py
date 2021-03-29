class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def firstnode2list(node: ListNode):
        res = [node.val]
        i = node
        while i.next:
            i = i.next
            res.append(i.val)
        
        return res
    
    @staticmethod
    def list2firstnode(l: list):
        res = ListNode(l[0])
        
        for i in range(1, len(l)):
            node = ListNode(l[i])
            exec(f'res{".next" * i} = node')
        
        return res
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.firstnode2list(l1)
        num2 = self.firstnode2list(l2)
        
        if len(num1) >= len(num2):
            max_l = num1
            min_l = num2
        else:
            max_l = num2
            min_l = num1
        
        res = [0] * len(max_l)
        memory = False
        for i in range(len(max_l)):
            if i < len(min_l):
                sum_res = max_l[i] + min_l[i]
            else:
                sum_res = max_l[i]
            
            if memory:
                sum_res += 1
                memory = False
            
            if sum_res > 9:
                res[i] = sum_res % 10
                memory = True
            else:
                res[i] = sum_res
        
        if memory:
            res.append(1)
        
        return self.list2firstnode(res)
