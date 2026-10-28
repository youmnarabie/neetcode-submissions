class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next: ListNode = None 

class MyLinkedList:

    def __init__(self):
        self.length = 0 
        self.head = None
    
    def getObj(self, index: int) -> ListNode:
        if index < 0 or index >= self.length:
            return -1 
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr

    def get(self, index: int) -> int:
        if index < 0 or index > self.length - 1:
            return -1 
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val)
        new_head.next = self.head
        self.head = new_head
        self.length += 1 
        
    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        
        if not self.head:
            self.head = node
            self.length += 1 
            return
        curr_end = self.getObj(self.length - 1)
        curr_end.next = node
        self.length += 1 
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        elif index == 0:
            return self.addAtHead(val)
        elif index == self.length:
            return self.addAtTail(val)

        node = ListNode(val)
        curr_prev = self.getObj(index-1)
        curr_index = curr_prev.next
        curr_prev.next = node
        node.next = curr_index
        self.length += 1 

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return None 
        if index == 0:
            self.head = self.head.next
            self.length -= 1 
            return
            
        curr_prev = self.getObj(index-1)
        curr_prev.next = curr_prev.next.next
        self.length -= 1 


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)