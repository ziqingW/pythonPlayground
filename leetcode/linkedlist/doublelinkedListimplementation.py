class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None



class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index > self.size-1:
            return -1
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val
    
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        curr = self.head
        self.head = Node(val)
        if curr is not None:
            curr.prev = self.head
            self.head.next = curr
            self.head.prev = None
            self.size += 1
        else:
            self.head.prev = None
            self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        curr = self.head
        if curr is not None:
            for i in range(self.size-1):
                curr = curr.next
            newTail = Node(val)
            curr.next = newTail
            newTail.prev = curr
            newTail.next = None
            self.size += 1
        else:
            self.head = Node(val)
            self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == self.size:
            self.addAtTail(val)
        elif index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        elif 0 < index < self.size:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            newNode = Node(val)
            newNode.next = curr.next
            curr.next.prev = newNode
            curr.next = newNode
            newNode.prev = curr
            self.size += 1
            

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
        elif index == self.size -1:
            curr = self.head
            for i in range(index-1):
                curr = curr.next
            curr.next = None
            self.size -= 1
        elif 0 < index < self.size -1:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
            curr.next.prev = curr
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)