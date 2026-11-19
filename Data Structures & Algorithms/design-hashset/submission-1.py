class ListNode:

    def __init__(self, val:int):
        self.val = val
        self.next = None


class MyHashSet:

    def __init__(self):
        self.data = [ListNode(0) for _ in range(10 ** 4)]

    def add(self, key: int) -> None:
        current = self.data[key % len(self.data)]
        while current.next:
            if current.next.val == key:
                return
            current = current.next
        current.next = ListNode(key)

    def remove(self, key: int) -> None:
        current = self.data[key % len(self.data)]
        while current.next is not None:
            if current.next.val == key:
                current.next = current.next.next
                return
            current = current.next

    def contains(self, key: int) -> bool:
        current = self.data[key % len(self.data)]
        while current.next is not None:
            if current.next.val == key:
                return True
            current = current.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)