import sys

if len(sys.argv) == 1:
    print('usage:python modifier.py [inputPath] [outputPath]')
    exit(0)	
else:
    inPath = sys.argv[1] 
    outPath = sys.argv[2]

left1 = True
left2 = True

def modify(str):
    global left1, left2
    
    if str.find('\\\\') is not -1:
        str = str.replace('\\\\', '\\\\\\')

    #Before Start, deal with \$
    if  str.find('\$') is not -1:
        str = str.replace('\$', '\money')

    #Firstly deal with $$...$$
    while str.find('$$') is not -1:
    	if left1:
    		str = str.replace('$$', '\\\[', 1)
    	else:
    		str = str.replace('$$', '\\\]', 1)
    	left1 = not left1

    #Then deal with $...$
    left2 = True

    while str.find('$') is not -1:
    	if left2:
    		str = str.replace('$', '\\\(', 1)
    	else:
    		str = str.replace('$', '\\\)', 1)
    	left2 = not left2
    
    #Finally
    while str.find('\money') is not -1:
    	str = str.replace('\money', '$')

    return str

fp = open(outPath, 'wb')

with open(inPath, 'r') as fpIn:
    while True:
        line = fpIn.readline()
        if not line:
            break;
        #print line,
        line = modify(line)
        #print line,
        print line
        fp.write(line)

fp.close()
