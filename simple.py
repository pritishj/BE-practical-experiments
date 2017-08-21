import math

string = input("Enter string\n")
type(string)
n = math.ceil(math.sqrt(len(string)))
m = math.ceil(len(string)/(n*1.0))
pad = m*n - len(string)
string+="x"*pad;

matrix = []
for i in range(0,m):
    matrix.append([])
    for j in range(0,n):
        matrix[i].append(0)

s=0
        
for i in range(0,m):
	for j in range(0,n):
		matrix[i][j]=string[s]
		s=s+1
		

string2=""
for j in range(0,n):
	for i in range(0,m):
		print(matrix[i][j],end="")
		string2+=matrix[i][j];
print()

#print(matrix)


c = input('''Do you want to decrypt
y or n
''')
			
if c is 'y':
	for i in range(0,m):
		for j in range(0,n):
			print(matrix[i][j],end="")
	print()

s=0        
for i in range(0,m):
	for j in range(0,n):
		matrix[i][j]=string2[s]
		s=s+1	

for j in range(0,n):
	for i in range(0,m):
		print(matrix[i][j],end="")
	
	
		
