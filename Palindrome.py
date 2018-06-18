''' Daniel Marquez drm16g '''
#!usr/bin/python3

def main():

	palindromes = {}		#list of palindromes
	counter = 1
	string = input( "Enter the strings:\n")
	back = 0
	while string != 'Done':
		itr = -1
		it = 0
		while it < len(string):
			if string[it].isspace():
				it = it + 1
				continue
				
			elif string[itr].isspace():
				itr = itr - 1
				continue
				
			elif string[itr].lower() != string[it].lower():
				it = 0 
				break
			itr = itr - 1
			it = it + 1
		if it:
			palindromes[counter] = string
			counter = counter + 1
		string = input()

	print('The palindromes are:')
	print(palindromes)
	
if __name__ == '__main__': main()
