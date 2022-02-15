import re

errors = []

pattern = re.compile(r'[A-Z,a-z]')
patt = re.compile(r'[0-9]+')
with open('kh.txt', 'rt') as myfile:   #instead of 'kh.txt' you have to put your file name where attendance are saved
    for line in myfile:
        line.strip('\n')
        if re.match(pattern,line):
            continue
        else :
            if patt.search(line) is not None:  # If pattern search finds a match,
                errors.append(line.replace('\n',''))

#Removing duplicates from the original list and appending in new list
res=[]
for i in errors :
    if i not in res:
      res.append(i)

#Sorting elements in integer order
res.sort(key=int)
print(','.join([err.strip() for err in res]))
print(len(res))
