class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.val,end="->")
            temp = temp.next
        print("None")


# example usage
l1 = LinkedList()
l1.insert_at_beginning(2)
l1.insert_at_beginning(1)
l1.insert_at_end(4)
l1.display()