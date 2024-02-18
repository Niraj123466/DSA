n = int(input("Enter Limit of Database: "))
hashTable = [[] for _ in range(10)]

def linear_probing(val, name, phone):
    temp = [(name, phone)]
    while hashTable[val]:
        val = (val + 1) % 10
    hashTable[val] = temp
    display_hashTable()

def separate_chaining(val, name, phone):
    hashTable[val].append((name, phone))
    display_hashTable()

def insert_value(name, phone):
    val = hash_fun(phone)
    if not hashTable[val]:
        hashTable[val] = [(name, phone)]
    else:
        print("\n***Collision Occurred***")
        value = int(input("1. Linear Probing\n2. Separate Chaining\nEnter Choice: "))
        if value == 1:
            linear_probing(val, name, phone)
        elif value == 2:
            separate_chaining(val, name, phone)

def hash_fun(phone):
    return phone % 10

def display_hashTable():
    for k in range(10):
        print(str(k) + "->" + str(hashTable[k]))

def search_number(phone):
    for i in range(10):
        for name, num in hashTable[i]:
            if num == phone:
                print(f"FOUND: {name}")
                return
    print("NOT FOUND")

for i in range(n):
    name = input("Enter name: ")
    phone = int(input("Enter phone number: "))
    insert_value(name, phone)

print("\nHash Table:\n")
display_hashTable()

num = int(input("Enter the number of elements you want to search: "))
for i in range(num):
    phone = int(input("\nEnter phone number to be searched: "))
    search_number(phone)
