class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        # dummy head và tail
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    # thêm node vào cuối
    def addNode(self, node):
        prev = self.tail.prev

        prev.next = node
        node.prev = prev

        node.next = self.tail
        self.tail.prev = node

    # xóa node
    def removeNode(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    # đưa node mới dùng xuống cuối
    def moveToTail(self, node):
        self.removeNode(node)
        self.addNode(node)

    # xóa node đầu tiên (ít dùng nhất)
    def removeHead(self):
        node = self.head.next
        self.removeNode(node)
        return node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.moveToTail(node)

        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.moveToTail(node)

        else:
            node = Node(key, value)
            self.cache[key] = node
            self.addNode(node)

            if len(self.cache) > self.capacity:
                removed = self.removeHead()
                del self.cache[removed.key]