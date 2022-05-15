# Tuples

filename = "dataset/mbox-short.txt"
handle = open(filename)

listy=list()
for line in handle:
    if line.startswith("From:"):
        continue
    elif line.startswith("From"):
        words=line.split()
        words=listy.append(words[5])
    elif not line.startswith("From"):
        continue
        
pisty=list()
for letters in listy:
    letter=letters.split(':')
    letter=pisty.append(letter[0])
pisty.sort()

hours=dict()
for hrs in pisty:
    if hrs not in hours:
        hours[hrs]=1
    else:
        hours[hrs]+=1
res=hours.items()

for hr,c in res:
    print(hr,c)

    
