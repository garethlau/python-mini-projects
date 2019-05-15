import random

list_a = []

def create_binary_list(list_name, length):
    n = random.randint(1, 5)
    for i in range(0, length):
        list_name.append(n)
        n = n + random.randint(1, 5)

def b_search(element, list_name):

    running = True
    while running == True:

        if len(list_name) == 1:
            if element != list_name[0]:
                print("Not found!")
                return False
            else:
                print("Found")
                return True

        elif len(list_name) % 2 == 0:
            test_num = list_name[(int(len(list_name) / 2))]
            if element < test_num:
                del list_name[int(len(list_name) / 2):]
            elif element > test_num:
                del list_name[0: int(len(list_name) / 2)]
            else:
                print("Found!")
                return True
            print(test_num)

        else:
            test_num = list_name[int((len(list_name) - 1) / 2)]
            if element < test_num:
                del list_name[(int((len(list_name) - 1) / 2)):]
            elif element > test_num:
                del list_name[0: int((len(list_name) - 1) / 2)]
            else:
                print("Found!")
                return True
            print(test_num)



if __name__ == "__main__":
    create_binary_list(list_a, 100)
    print(list_a)
    b_search(13, list_a)