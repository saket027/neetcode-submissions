class ListNode:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.next = None



class MyHashMap:

    def __init__(self):
        self.data = [ListNode() for _ in range(1000)]

    def hash(self, key):
        return key % len(self.data)


    def put(self, key: int, value: int) -> None:
        current = self.data[self.hash(key)]
        while current.next is not None:
            if current.next.key == key:
                current.next.val = value
                return
            current = current.next
        current.next = ListNode(key, value)

    def get(self, key: int) -> int:
        current = self.data[self.hash(key)].next
        while current is not None:
            if current.key == key:
                return current.val
            current = current.next

        return -1


    def remove(self, key: int) -> None:
        current = self.data[self.hash(key)]
        while current.next is not None:
            if current.next.key == key:
                current.next = current.next.next
                return 
            current = current.next



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)