# Dictionaries

#filename = "dataset/mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From"):
        continue
    if line.startswith("From:"):
        continue
    if line.startswith("From"):
        words=line.split()
        print(words[1])
        count=count+1
        


