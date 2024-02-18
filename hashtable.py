n = int(input("Enter Limit of Database: "))
hashTable = [[] for i in range(10)]

def linear_probing(val, phone):
    temp = [phone]
    while hashTable[val]:
        val = (val + 1) % 10
    hashTable[val] = temp
    display_hashTable()

def separate_chaining(val, phone):
    hashTable[val].append(phone)
    display_hashTable()

def insert_value(phone):
    val = hash_fun(phone)
    if not hashTable[val]:
        hashTable[val] = [phone]
    else:
        print("\n***Collision Occurred***")
        value = int(input("1. Linear Probing\n2. Separate Chaining\nEnter Choice: "))
        if value == 1:
            linear_probing(val, phone)
        elif value == 2:
            separate_chaining(val, phone)

def hash_fun(phone):
    return phone % 10

def display_hashTable():
    for k in range(10):
        print(str(k) + "->" + str(hashTable[k]))

def search_number(phone):
    for i in range(10):
        for j in range(len(hashTable[i])):
            if hashTable[i][j] == phone:
                print("FOUND")
                return
    print("NOT FOUND")

for i in range(n):
    nval = input("Enter name: ")
    pval = int(input("Enter phone number: "))
    insert_value(pval)

print("\nHash Table:\n")
display_hashTable()

num = int(input("Enter the number of elements you want to search: "))
for i in range(num):
    phone = int(input("\nEnter phone number to be searched: "))
    search_number(phone)
