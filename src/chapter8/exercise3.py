# Exercise 3

try:
    fhand = open('mbox-short.txt')
    for line in fhand:
        words = line.split()
        if len(words) < 3 or words[0] != 'From':
            continue
        print(words[2])
except:
    print("Unable to open file! File may not exist in the directory")
    quit()
