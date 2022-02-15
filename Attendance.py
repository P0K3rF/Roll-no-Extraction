import re

errors = []

pattern = re.compile(r'[A-Z,a-z]')
patt = re.compile(r'[0-9]+')
with open('kh.txt', 'rt') as myfile:
    for line in myfile:
        line.strip('\n')
        if re.match(pattern,line):
            continue
        else :
            if patt.search(line) is not None:  # If pattern search finds a match,
                errors.append(line.replace('\n',''))
print(','.join([err.strip() for err in errors]))
