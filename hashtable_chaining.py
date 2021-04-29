import numpy as np


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.list = [value]


class ChainingHashTable:
    def __init__(self, size, hfunction):
        self.size = size
        self.table = [None]*size
        self.hfunction = hfunction
        self.p = self.getPrime()
        self.a = np.random.randint(0, self.size - 1)  #random values used for universal hashing
        self.b = np.random.randint(0, self.p-1)

    def search(self, key):
        #key=self.hashingfunction(key)
        for i in range(0, len(self.table)):
            node = self.table[i]
            if node is not None:
                if node.key==key:
                    return node
        return None

    def insert(self, key, value):
        h = self.hashingfunction(key)
        n = self.search(h)
        if n is not None:
            n.list.append(value)
            return n.key

        node = Node(h, value)
        self.table[h] = node
        return h

    def deletekey(self, key):
        n = self.search(int(key))
        if n is not None:
            self.table[int(key)] = None
            print("Deleted key ", key)
            return True
        print("failed to delete value", key)

    def print(self):
        print("table is of size: ", len(self.table))
        for i in range(0, len(self.table)):
            n = self.table[i]
            if n is not None:
                print("index:", i, ", key:", n.key, ", value: ", n.list)

    def hashingfunction(self,key):
        if self.hfunction=="division":
            return int(key) % self.size
        elif self.hfunction == "multiplication":
            return int(np.floor(((key * 0.671) % 1) * self.size))
        elif self.hfunction == "universal":
            return ((round(self.a*key + self.b))%self.p)%self.size

    def getPrime(self, p=0):
        if p == 0:
            p = np.random.randint(1000000, 10000000)
        while not self.isprime(p):
            p += 1
        return p

    def isprime(self, n):
        if n <= 2 or n % 2 == 0:
            return False
        return not any((n % i == 0 for i in range(3, n - 1)))