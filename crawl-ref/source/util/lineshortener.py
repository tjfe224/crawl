# myfile.cpp is arbitrary, rename for applicable file
file1 = open('myfile.cpp', 'r')
Lines = file1.readlines()
# readme.cpp is arbitrary output file, rename for whatever
with open('readme.cpp', 'w') as f:
    for line in Lines:
        if len(line) > 80:
        
            for i in range(0, int(len(line) / 80)):
                print(line[i * 80: i * 80 + 80] + '\\')
                f.write(line[i * 80: i * 80 + 80] + '\\')
                f.write('\n')
            print(line[i * 80 + 80: i * 80 + 160])
            f.writelines(line[i * 80 + 80: i * 80 + 160])
        else:
            f.write(line)