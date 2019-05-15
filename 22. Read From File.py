category_count = {}
outfile = open('wfile.txt', 'w')

if __name__ == '__main__':
    with open('test_file.txt', 'r') as file:
        line = file.readline()
        while line:
            line = line[3: -26]
            if line in category_count:
                category_count[line] += 1
            else:
                category_count[line] = 1
            line = file.readline()

            outfile.write(str(line[3:-26]) + '\n')

    print(category_count)

    outfile.close()
