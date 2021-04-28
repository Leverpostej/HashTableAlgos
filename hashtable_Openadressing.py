import numpy as np


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.list = value


class OpenAddressing:
    def __init__(self, size, hfunction, probetype):
        self.size = size
        self.table = [None]*size
        self.hfunction = hfunction
        self.probetype = probetype
        self.a = np.random.randint(0, self.size - 1)  #random value used for universal hashing

    def search(self, key):
        #key=self.hashingfunction(key)
        for i in range(0, len(self.table)):
            node = self.table[i]
            if node is not None:
                if node.key == key:
                    return node
        return None

    def insert(self, key, value):
        h = self.hashingfunction(key)
        n = self.search(h)
        if n is not None:
            if self.probetype == "linear":
                ph = h % self.size
                #print("probehash", probehash, "size", self.size)
                for i in range(ph, len(self.table)):
                    potentialnode = self.table[i]
                    if potentialnode is None:
                        node = Node(i, value)
                        self.table[i] = node
                        return i

                for i in range(0, ph-1):
                    potentialnode = self.table[i]
                    if potentialnode is None:
                        node = Node(i, value)
                        self.table[i] = node
                        return i
                print("Table overflow error")
                return False

            if self.probetype == "quadratic":
                for i in range(0, len(self.table)-1):
                    ph = (h + (i * i)) % self.size #c1 = 0 and c2 = 1
                    if self.table[ph] is None:
                        node = Node(ph, value)
                        self.table[ph] = node
                        return i

                print("Table overflow error")
                return False

            if self.probetype == "doublehashing":
                h1k = int(key % self.size) # m = self.size
                h2k = 1+(key % (self.size - 3))
                for i in range(0, len(self.table)):
                    spot = (h1k+(i*h2k)) % self.size
                    if self.table[spot] is None:
                        node = Node(h, value)
                        self.table[spot] = node
                        return spot

                print("Table overflow error", "h1k", h1k, "h2k", h2k) #happens sometimes
                return False

        node = Node(h, value)
        for i in range(0, len(self.table)):
            if self.table[i] is None:
                self.table[i] = node
                break
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

    def hashingfunction(self, key):
        if self.hfunction == "division":
            return int(key) % self.size
        elif self.hfunction == "multiplication":
            return int(np.floor(((key * 0.837) % 1) * self.size))
        elif self.hfunction == "universal":
            return int(key)*self.a
