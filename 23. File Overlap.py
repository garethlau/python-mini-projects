file1 = open('file1.txt', 'r')
file2 = open('file2.txt', 'r')

if __name__=='__main__':

    overlap = []

    str_list1 = file1.readlines(825)
    num_list1 = []
    for i in range(0, len(str_list1)):
        n = str_list1[i][:-1]
        num_list1.append(n)
        if i == (len(str_list1) - 1):
            n = str_list1[i]
            num_list1.append(n)


    str_list2 = file2.readlines(693)
    num_list2 = []
    for i in range(0, len(str_list2)):
        n = str_list2[i][:-1]
        num_list2.append(n)
        if i == (len(str_list2) - 1):
            n = str_list2[i]
            num_list2.append(n)

    def compare_lists(a_list, b_list, overlap_list):

        if len(a_list) >= len(b_list):
            for i in range(0, len(a_list)):
                element = a_list[i]
                for c in range(0, len(b_list)):
                    test = b_list[c]
                    if element == test and element not in overlap_list:
                        overlap_list.append(element)

        elif len(a_list) < len(b_list):
            for i in range(0, len(b_list)):
                element = b_list[i]
                for c in range(0, len(a_list)):
                    test = a_list[c]
                    if element == test and element not in overlap_list:
                        overlap_list.append(element)

        return overlap_list

    compare_lists(num_list1, num_list2, overlap)
    print(overlap)

