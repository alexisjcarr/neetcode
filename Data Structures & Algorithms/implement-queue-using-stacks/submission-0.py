"""
Brainstorm:
 - Can use two stacks:
    - inbox, outbox
    - pushes go in inbox
    - pop off all nodes and put in outbox to get pop or peek
"""
class MyQueue:

    def __init__(self):
        self.inbox = []
        self.outbox = []
    

    def push(self, x: int) -> None:
        self.inbox.append(x)
        

    def pop(self) -> int:
        while len(self.inbox) > 1:
            self.outbox.append(self.inbox.pop())

        res = self.inbox.pop()

        while self.outbox:
            self.inbox.append(self.outbox.pop())

        return res

        
    def peek(self) -> int:
        while len(self.inbox) > 1:
            self.outbox.append(self.inbox.pop())

        res = self.inbox[-1]

        while self.outbox:
            self.inbox.append(self.outbox.pop())
            
        return res
        

    def empty(self) -> bool:
        return not self.inbox
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()