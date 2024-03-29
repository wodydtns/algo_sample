# 해시테이블
class HashTableNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        hashsum = 0
        # Simple hash function: sum of characters
        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum

    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]

        if node is None:
            self.buckets[index] = HashTableNode(key, value)
            return

        # Collision: iterate to the end of the linked list and append the node
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = HashTableNode(key, value)

    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value

    def delete(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = None

        # Iterate to find the node to remove
        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return None

        self.size -= 1
        result = node.value

        # Remove node from the chain
        if prev is None:
            self.buckets[index] = node.next
        else:
            prev.next = node.next

        return result


# Example usage
ht = HashTable()
ht.insert("key1", "value1")
ht.insert("key2", "value2")
print(ht.find("key1"))  # Output: value1
print(ht.find("key2"))  # Output: value2
ht.delete("key1")
print(ht.find("key1"))  # Output: None
