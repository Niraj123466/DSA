'''
    Name : Niraj More
    Assignment : 1
    Roll No : SA49
'''

n = int(input("Enter the number of records : "))
hashTable = [[] for i in range(10)]

def linear_probing(val, name, phone) :
    temp = [(name, phone)]
    while hashTable[val] :
        val = (val + 1) % 10
    hashTable[val] = temp
    display_hashTable()

def separate_chaining(val, name, phone) :
    hashTable[val].append((name, phone))
    display_hashTable()

def insert_value(name, phone) :
    val = hashFunction(phone)
    if not hashTable[val] :
        hashTable[val] = [(name, phone)]
    else :
        print("\n***** Collision Occurured ******")
        choice = int(input('1.Linear Probing\n2.Separate Chaining\n'))
        if choice == 1 :
            linear_probing(val, name, phone)
        else :
            separate_chaining(val, name, phone)
    
def hashFunction(phone) :
    return phone % 10

def display_hashTable() :
    for i in range(10) : 
        print(str(i) + "->" + str(hashTable[i]))

def search_number(phone) :
    for i in range(10) :
        for name, num in hashTable[i] :
            if(num == phone) :
                print(f'Found ! : {name}')
                return
    print("Not found")

for i in range(n) :
    name = input("Enter the name : ")
    phone = int(input("Enter the phone number : "))
    insert_value(name, phone)

print('\nHash Table\n')
display_hashTable()

num = int(input("Enter the number of phone records do you want to search : "))
for i in range(num) :
    phone = int(input("Enter the phone number to be searched : "))
    search_number(phone)

