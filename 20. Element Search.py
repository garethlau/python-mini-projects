binary_list = [1, 3, 6, 7, 12, 16, 18, 20, 29, 30, 34, 35, 40, 42]

def search(element, list):
    if element in list:
        return True
    else:
        return False

def binary_search(element, olist):

    a = olist
    print("the length of the list is: ")
    print(len(olist))
    print(len(a))
    print(int(len(a) / 2))

    running = True
    while running == True:
        if (len(a) % 2) == 0:
            test = a[(int(len(a) / 2))]
            if element < test:
                del a[(int((len(a) / 2) - 1)):(len(a))]

            elif element > test:
                del a[0:int(((len(a) / 2)))]

            else:
                running = False
                print("Found")

        elif (len(a) % 2) == 1:
            test = a[int((len(a) - 1) / 2)]
            if element < test:
                del a[int((len(a) - 1) / 2):(len(a))]

            elif element > test:
                del list[0:int((len(a) + 1) / 2)]

            else:
                running = False
                print("Found")

        elif len(a) == 1:
            if element == a[0]:
                running = False
            else:
                return False
                running = False

print(binary_search(2, binary_list))


#print(search(2, binary_list))
