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
        self.p = self.getPrime()
        self.a = np.random.randint(0, self.size - 1)  #random values used for universal hashing
        self.b = np.random.randint(0, self.p-1)

    def search(self, key):
        for i in range(0, len(self.table)):
            j = 0

            if self.probetype == "linear":
                j = (self.hashingfunction(key) + i) % self.size
            elif self.probetype == "quadratic":
                j = self.hashingfunction(key) + (6 * i) + (4 * (i * i)) % self.size
            elif self.probetype == "doublehashing":
                h1 = self.hashingfunction(key)
                h2 = int(np.floor(((key * 0.837) % 1) * self.size))
                j = h1 + (i * h2) % self.size

            if j > len(self.table):
                break
            try:
                if  self.table[j] == None:
                    break
            except:
                return None
            #print(j, self.table[j].key, key)
            if self.table[j].key == key:
                return j

        #print("search failed")
        return None

    def insert(self, key, value):


        n = self.search(key)

        if n is not None: #collision happens
            for i in range(0,len(self.table)):
                j=0

                if self.probetype == "linear":
                    j = (self.hashingfunction(key)+i) % self.size
                elif self.probetype == "quadratic":
                    j = self.hashingfunction(key) + (6*i) + (4*(i*i)) % self.size
                elif self.probetype == "doublehashing":
                    h1 = self.hashingfunction(key)
                    h2 = int(np.floor(((key * 0.837) % 1) * self.size))
                    j = h1+(i* h2) % self.size

                if j > len(self.table):
                    break
                try:
                    if self.table[j] is None:
                        node = Node(j, value)
                        self.table[j]=node
                        return j
                except:
                    h = self.hashingfunction(key)
                    node = Node(h, value)
                    self.table[h] = node
            #print("overflow error")
            return None
        h = self.hashingfunction(key)
        node = Node(h, value)
        self.table[h] = node
        return h

    def deletekey(self, key):
        n = self.search(int(key))
        if n is not None:
            self.table[int(key)] = "Deleted"
            print("Deleted key ", key)
            return True
        print("failed to delete key", key)

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