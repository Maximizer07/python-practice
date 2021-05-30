"""
    Реализуйте свою структуру данных, хэш-таблицу, аналог встроенного dict.
    Используйте функцию hash. Примените тестирование на случайных данных.
    1. Реализуйте методы чтения, записи, получения размера хэш-таблицы.
    2. Сделайте вышеупомянутые методы стандартными операторами/функциями,
    по аналогии с dict.
    3. Реализуйте поддержку для цикла for.
"""
INITIAL_CAPACITY = 50


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return "<Node: (%s, %s), next: %s>" % (self.key, self.value, self.next is not None)

    def __repr__(self):
        return str(self)


class HashTable:
    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        hash_sum = 0
        for idx, c in enumerate(key):
            hash_sum += (idx + len(key)) ** ord(c)
            hash_sum = hash_sum % self.capacity
        return hash_sum

    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)

    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                self.buckets[index] = node.next
            else:
                prev.next = prev.next.next
            return result
