import re
import sys
if len(sys.argv)!=3:
	print "The program needs 3 inputs as programe, filename and number"
	exit(1)
infile=sys.argv[1];
n=int(sys.argv[2])
#infile=raw_input("Enter the file name: ")
fin=file(infile,"r")
fin.seek(0,2)
t=fin.tell()
#n=input()
p=t/n
fin.seek(0,0)
for i in range(n):
	data=fin.read(p)
	pat=str(i)+"."
	filename=re.sub(r"\.",pat,infile)
	fo=file(filename,"w")
	print filename
	fo.write(data)
	fo.close()
fin.close()
