''' Name : Niraj More
    Assignment : 2
    Roll No : SA49
'''

set1 = set()
set2 = set()
n = int(input("Enter the no of element in set 1 : "))
print("Enter the elements of set 1 :")
for i in range(n):
    ele = float(input())
    set1.add(i)
print("set 1 : ", set1)

n = int(input("Enter the no of element in set 2 : "))
print("Enter the elements of set 2 :")
for i in range(n):
    ele = float(input())
    set2.add(i)
print("set 2 : ", set2)


flag = True
while (flag):
    print('''Main menu
        1.Add
        2.remove
        3.contain
        4.size
        5.union
        6.intersection
        7.difference
        8.subset''')
    choice = int(input("Enter your choice"))
    if (choice == 1):
        ele = float(input("Enter the element to be added : "))
        print("set before adding element : ", set1)
        set1.add(ele)
        print('new set : ', set1)
        continueOrNot = input("Do you want ot continue : ")
        if(continueOrNot == 'no'):
            flag = False

    elif (choice == 2):
        ele = float(input(("Enter the element to be deleted : ")))
        print("set before adding element : ", set1)
        set1.remove(ele)
        print('new set : ', set1)
        continueOrNot = input("Do you want ot continue : ")
        if(continueOrNot == 'no'):
            flag = False


    elif (choice == 3):
        ele = float(input("Enter the element to be checked in set"))
        print(set1)
        if (ele in set1):
            print(ele, " is present")
        else:
            print(ele, " is absent")
        continueOrNot = input("Do you want ot continue : ")
        if(continueOrNot == 'no'):
            flag = False
    

    elif (choice == 4):
        print('size of ', set1, ' is ', len(set1))
        print('size of ', set2, ' is ', len(set2))
        continueOrNot = input("Do you want ot continue : ")
        if(continueOrNot == 'no'):
            flag = False

    elif (choice == 5):
        print("Union of ", set1, " and ", set2, " is : ", set1.union(set2))
        continueOrNot = input("Do you want ot continue : ")
        if(continueOrNot == 'no'):
            flag = False

    elif (choice == 6):
        print("Intersection of ", set1, " and ",
              set2, " is : ", set1.intersection(set2))
        continueOrNot = input("Do you want ot continue : ")
        if(continueOrNot == 'no'):
            flag = False

    elif (choice == 7):
        print("Difference of ", set1, " and ",
              set2, " is : ", set1 - set2)
        continueOrNot = input("Do you want ot continue : ")
        if(continueOrNot == 'no'):
            flag = False

    elif (choice == 8):
        if (set1.issubset(set2)):
            print(set1, " is subset of ", set2)
        else:
            print(set1, " is not subset of ", set2)
    else:
        print("Wrong choice")
        continueOrNot = input("Do you want ot continue : ")
        if(continueOrNot == 'no'):
            flag = False
    