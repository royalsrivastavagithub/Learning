class _Node:
    __slots__ = 'element', 'next'

    def __init__(self, element, next):
        self.element = element
        self.next = next

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def add_first(self, e):
        new_node = _Node(e, self._head)
        self._head = new_node
        if self._size == 0:
            self._tail = new_node
        self._size += 1

    def add_last(self, e):
        if self._size == 0:
            self.add_first(e)
        else:
            new_node = _Node(e, None)
            self._tail.next = new_node
            self._tail = new_node
            self._size += 1

    def display(self):
        p = self._head
        while p:
            print(p.element, end='-->')
            p = p.next          
        print()

    def search(self,e):
        p = self._head
        while p:
            if p.element == e:
                return True
            p = p.next
        return False
    def addany(self, e, pos):
        p = self._head
        i = 1
        while i < pos-1:
            p = p.next
            i += 1
        new_node = _Node(e, p.next)
        p.next = new_node

    def delete_first(self):
        if self._size == 0:
            return
        self._head = self._head.next
        self._size -= 1

    def delete_last(self):
        if self._size == 0:
            return
        p = self._head
        while p.next.next:
            p = p.next
        p.next = None
        self._size -= 1

    def delete_any(self, pos):
        if self._size == 0:
            return
        p = self._head
        i = 1
        while i < pos-1:
            p = p.next
            i += 1
        p.next = p.next.next
    


ll = LinkedList()
ll.add_last(10)
ll.add_last(20)
ll.add_last(30)
ll.add_last(40)
print('Elements in linked list:', end=' ')
ll.display()
print('Is linked list empty?', ll.is_empty())
print('Length of linked list:', len(ll))
print('Is 20 present in linked list?', ll.search(20))
print('Adding 100 at position 3')
ll.addany(100, 3)
print('After adding 100 at 3rd position:', end=' ')
ll.display()
print('Deleting 4th element')
ll.delete_any(4)
print('After deleting 4th element:', end=' ')
ll.display()
print('Deleting first element')
ll.delete_first()
print('After deleting first element:', end=' ')
ll.display()
print('Deleting last element')
ll.delete_last()
print('After deleting last element:', end=' ')
ll.display()
