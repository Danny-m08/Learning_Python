''' Daniel Marquez drm16g '''

#!/usr/bin/python3


def printTriangle( rows ):
	if rows == 1: 
		print (1)
		return
	elif rows == 2:
		print( '1\n1 1')
		return
	
	last_row = [1,1]
	new_row = []		
	
	print('1\n1 1')			
	for temp in range( 0, rows - 2 ):		#loop through each line
		new_row.append(1)
		for number in range(0,len(last_row)  -1):   #parse through previous row
			new_row.append( last_row[number] + last_row[number + 1] )
		new_row.append( 1 )
		for number in new_row:			#print list
			print( number, end = " ")
		print()		
		last_row = new_row.copy()		
		new_row.clear()			


def main():
	while 1:
		triangle_rows = int(input("Enter the number of rows:"))
		if triangle_rows <= 0:
			print("Number of rows must be greater than or equal to 0")
		else:
			printTriangle( triangle_rows )

if __name__ == '__main__': main()
