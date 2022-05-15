# Dictionaries

filename = "dataset/mbox-short.txt"


handle = open(filename)
lisa=list()
lister=list()
d=dict()


for lines in handle:
    if lines.startswith("From:"):
        continue
    if lines.startswith("From"):
        words=lines.split()
        words=lisa.append(words[1])
    if not lines.startswith("From"):
        continue

for k in lisa:
    if k not in d:
        d[k]=1
    else:
        d[k]=d[k]+1

large=0
for j in d:
    if d[j]>large:
        large=d[j]
        largest=j
    elif d[j]<large:
        continue
print(largest,d[largest])

    

    
        
