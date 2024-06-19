from sys import stdin


# Read the sequence of operations to be operated on the hash table
operations = []
for line in stdin:
    line = line.split()
    if len(line) > 2:
        line[2] = int(line[2])
    operations.append(line)


table_size = 10    # set table size here
hash_table = [[] for i in range(table_size)]

def show_hash_table():
    print('-------------------')
    for item_list in hash_table:
        print(item_list)
    print('-------------------')

def hash_func(s):
    # return the hash value

def insert(s, v):
    # return 0 on successful insertion
    # return -1 if s has already been in the hash table

def search(s):
    # return value of the key or
    # return -1 if s does not exists in hash table

def delete(s):
    # return 0 on successful deletion
    # return -1 if s does not exists in hash table


# The main program to execute the sequence of operations
for op in operations:
    # op[0] is "insert" or "search" or "delete"


    

