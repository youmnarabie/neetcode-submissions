class ListNode:
    def __init__(self, val=""):
        self.val = val
        self.prev = None
        self.next = None 

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr =  ListNode(homepage)

    def visit(self, url: str) -> None:
        node = ListNode(url)
        self.curr.next = node
        node.prev = self.curr
        self.curr = node 
        

    def back(self, steps: int) -> str:
        i = 0
        while i < steps and self.curr.prev is not None:
            self.curr = self.curr.prev
            i += 1 
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        i = 0
        while i < steps and self.curr.next is not None:
            self.curr = self.curr.next
            i += 1 
        return self.curr.val
    

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)