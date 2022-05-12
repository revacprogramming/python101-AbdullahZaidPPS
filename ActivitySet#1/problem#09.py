# Lists

filename = "dataset/romeo.txt"

def lists2():
    
    file=open(filename)
    linesall=list()
    for line in file:
        words=line.split()
        for k in words:
            if k in linesall:
                continue
            else:
                linesall.append(k)
    linesall.sort()
    print(linesall)
lists2()
            