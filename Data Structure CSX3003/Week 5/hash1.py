from sys import stdin

# Read the sequence of operations to be operated on the hash table
operations = []
for line in stdin:
    line = line.split()
    if len(line) > 2:
        line[2] = int(line[2])
    operations.append(line)


table_size = 10    # set table size here
hash_table = [[] for _ in range(table_size)]


def show_hash_table():
    print('-------------------')
    for item_list in hash_table:
        print(item_list)
    print('-------------------')


def hash_func(s):
    # return the hash value
    hash_value = sum(ord(c) for c in s) % table_size
    return hash_value


def insert(s, v):
    hash_value = hash_func(s)
    item_list = hash_table[hash_value]
    for item in item_list:
        if item[0] == s:
            return -1  # Key already exists, return -1
    item_list.append((s, v))
    return 0  # Successful insertion, return 0


def search(s):
    hash_value = hash_func(s)
    item_list = hash_table[hash_value]
    for item in item_list:
        if item[0] == s:
            return item[1]  # Key found, return value
    return -1  # Key not found, return -1


# def delete(s):
#     hash_value = hash_func(s)
#     item_list = hash_table[hash_value]
#     for i, item in enumerate(item_list):
#         if item[0] == s:
#             del item_list[i]  # Delete the item
#             return 0  # Successful deletion, return 0
#     return -1  # Key not found, return -1

def delete(s):
    hash_value = hash_func(s)
    item_list = hash_table[hash_value]
    for item in range(len(item_list)):
        if item_list[item][0] == s:
            del item_list[item]  # Delete the item
            return 0  # Successful deletion, return 0
    return -1  # Key not found, return -1


# The main program to execute the sequence of operations
for op in operations:
    if op[0] == "insert":
        result = insert(op[1], op[2])
        if result == 0:
            print("Successfully inserted:", op[1])
        else:
            print("Key already exists:", op[1])
    elif op[0] == "search":
        result = search(op[1])
        if result != -1:
            print("Value found:", result)
        else:
            print("Key not found:", op[1])
    elif op[0] == "delete":
        result = delete(op[1])
        if result == 0:
            print("Successfully deleted:", op[1])
        else:
            print("Key not found:", op[1])
