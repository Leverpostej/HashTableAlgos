import hashtable_chaining
import hashtable_Openadressing
import numpy as np
import csv
import time
import sys

#table = hashtable_chaining.ChainingHashTable(20000, hfunction="multiplication",)
# hfunction which type of hash function to choose; division, multipliciation, universal

table = hashtable_Openadressing.OpenAddressing(100000, hfunction="multiplication", probetype="doublehashing")
#table1 = hashtable_chaining.ChainingHashTable(20000, hfunction="multiplication")
# probetype which type of probe to use for open addressing; linear, quadratic, doublehashing

with open('imdb.csv', mode='r', encoding="utf8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    counter = 1
    starttime = time.time()
    for row in csv_reader:
        if row is not None:
            #if line_count==10000:
            #    break
            s = table.insert(key=np.random.randint(0,3500), value=row["title"])
            if s is not None:
                counter += 1
            #table2.insert(key=np.random.randint(0, 3500), value=row["Name"])

    print("took", time.time() - starttime, "secs to input", counter, "values")
    #loadfactor = counter/table.size
    #print("loadfactor", loadfactor)
    #print("expected time to search/insert/delete", 1/(1-loadfactor))
    table.insert(50,"Tobias")
    print("table1 takes up", (sys.getsizeof(table.table))/(1024*1024), "megabytes")
   # print("table2 takes up", (sys.getsizeof(table2.table))/(1024*1024), "megabytes")


while True:
    print("Type a command: insert <value> <key> , search <key>, delete <key>, print")
    i = input().split()
    command = i.pop(0)

    if command == "print":
        table1.print()
        continue
    elif command == "insert":
        key = i.pop()
        value = ' '.join([str(elem) for elem in i])

        startime = time.time()
        key2 = table.insert(int(key), value)
        print("took", time.time()-startime, " secs to insert value ", value, "with key ", key, "at hash", key2)
        continue
    elif command == "search":
        i = ' '.join([str(elem) for elem in i])
        h = table.hashingfunction(i)
        startime = time.time()
        node = table.search(int(h))
        if node is not None:
            print("took", time.time()-startime," to search for key ", i, " and found value ", node.list())
            continue
        print("Could not find key ", i)
        continue
    elif command == "deletekey":
        i = ' '.join([str(elem) for elem in i])
        table.deletekey(i)
        continue
    print("Did not understand command. Try again")
