# Files




fname = input("Enter file name: ")
fh = open(fname)
count=0
add=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    if line.startswith("X-DSPAM-Confidence:"):
        count=count+1
        index=line.find('0')
        num=line[index:]
        num1=float(num)
        add=add+num1
mean=add/count
print("Average spam confidence:",mean)

