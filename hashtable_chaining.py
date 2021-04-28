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
        self.a = np.random.randint(0, self.size - 1)  #random value used for universal hashing

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
        #for i in range(0, len(self.table)):
        #    if self.table[i] is None:
        #        self.table[i]=node
        #        break
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
            h= int(key) % self.size
            #print(h)
            return int(key) % self.size
        elif self.hfunction == "multiplication":
            #print("got key", key, "calculated hash", np.floor(((key * 0.671) % 1) * self.size))
            return int(np.floor(((key * 0.671) % 1) * self.size))
        elif self.hfunction == "universal":
            print("key", key, "hash", int(key)*self.a)
            return int(key)*self.a
