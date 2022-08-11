value = input()
value = value.split(' ')
N = int(value[0])
T = int(value[1])

# Get width for each road segment 
width = []
value = input()			
value = value.split(' ')
for a in value:
	width.append(int(a))

# Determine smallest width for ea test case
for a in range(T):
	value = input()	
	value = value.split(' ')
	x = int(value[0])
	y = int(value[1])
	smallest = 3
	
	for b in range(x,y+1):
		if width[b] < smallest: smallest = width[b]
	print (smallest)