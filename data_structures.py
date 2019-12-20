class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class double_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = -1

    def insert(self, value, location = None):
        node = Node(value)
        #location is none only if we are inserting at the end
        if self.head == None: #Nothing has been inserted
            self.head = self.tail = node
            self.head.prev = self.tail.next = None
            self.size += 1

        elif location == 0: #insert at start of LL
            node.next = self.head
            self.head.prev = node #update nextNodes prev reference
            self.head = node
            self.size += 1

        elif location == None: #insert at end of LL
            node.prev = self.tail
            self.tail.next = self.tail = node #update tail and 2nd to last element
            node.next = None
            self.size += 1

        else: #inserting internally
            temp_node = self.head
            for i in range(location-2): temp_node = temp_node.next
            next = temp_node.next
            node = double_linked_list().createNode(value, next = next, prev = temp_node)
            next.prev = node
            temp_node.next = node
            self.size += 1

    def deleteNode(self, location):
        if self.size == -1: return "Error: LL doesn't exist"

        elif self.size == 0: #delete only node
            self.head = self.tail = None
            self.size -= 1

        elif location == 0: #delete 0th element
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1

        elif location >= self.size: #delete last node
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1

        else:
            temp_node = self.head
            for i in range(location-2):
                temp_node = temp_node.next
            temp_node.next = temp_node.next.next #update prev nodes reference
            if temp_node.next != None:
                temp_node.next.prev = temp_node  #update next nodes prev reference

    def deleteList(self):
        self.head = self.tail = None
        self.size = 0

    def traverse(self):
        temp_node = self.head
        while temp_node != None:
            print temp_node.value
            temp_node = temp_node.next

    def getHead(self): return self.head
    def getTail(self): return self.tail

class Stack():
    """
    Last in first out stack. Used for DFS.
    """
    def __init__(self):
        self.stack = double_linked_list()

    def push(self, value):
        if self.stack.head == None: self.stack.insert(value)
        else: self.stack.insert(value, 0)

    def pop(self):
        if self.stack.size == -1: return "Error: Stack Empty"
        else:
            node = self.stack.head

            if node.next != None: #if snode not only element
                self.stack.head = node.next
                node.next.prev = None

            else: #popping only element
                self.stack.head == None
                self.stack.tail == None

            self.stack.size -= 1
            return node.value

    def isEmpty(self):
        return self.stack.head == None

class Queue():
    """
    first in first out queue. Used for BFS
    """
    def __init__(self):
        self.queue = []
        self.top = 0

    def enQueue(self, value):
        self.top += 1
        if len(self.queue) == 0:
            self.queue.append(value)
        else:
            self.queue.insert(len(self.queue), value)

    def deQueue(self):
        value = self.queue[0]
        self.queue.remove(value)
        return value

    def isEmpty(self):
        return self.top == 0
