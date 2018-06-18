#--------------Daniel-Marquez----drm16g-----------------

class RSA():
	

	def __init__(self):
		self._e = 0
		self._d = 0
		self._List = []
		self._N = 0

	def inputFunc( self, entries ):
		for entry in range( 0, entries):
			self._List.append( int( input ()) )
		
	def printFunc( self, number ):
		return 'message is ' + str(number) 
		
	
	def encrypted_decorator(self,func):
		def func_wrapper(mode):
			return 'The encrypted ' + func(mode) 
		return func_wrapper	
		
	def decrypted_decorator(self, func):
		def func_wrapper(  mode ):
			return 'The decrypted ' + func(mode)
		return func_wrapper 
	
	def primeGen( self, minimum ):
		possible_prime = minimum
		while 1:
			for divisor in range( 2, possible_prime ):
				if possible_prime % divisor == 0:
					break
			else:
				yield possible_prime
			possible_prime += 1	
	
	def keyGen( self ):
		minimum =  int(input( 'Enter the minimum value for the prime numbers: '))
		prime = self.primeGen( minimum )
		prime1 = next(prime)
		prime2 = next(prime)
		#print( 'prime1: ', prime1)
		#print( 'prime2: ', prime2)
		self._N = prime1 * prime2
		tot = self.Totient( prime1, prime2 )		
		#print( tot)
		for e in range( 2, int(tot) ):
			if self.GCD( e, int(tot) ) == 1:
			 break
		self._e = e
		self._d = 2
		while 1:
			if (e * self._d) % tot == 1:
				break
			self._d += 1
		print ( 'N is ' + str(self._N) )
		print ( 'e is ' + str(self._e) )
		
	def Totient(self, p, q ):
		return self.LCM((p - 1) , (q - 1))
		
	def GCD( self, number1, number2 ):
		while number2:
			number1, number2 = number2, number1%number2
		return number1

	def LCM( self, number1, number2 ):
		return number1 * number2 / self.GCD(number1, number2)

	def encrypt( self, message ):
		return (message **self._e) % self._N 

	def decrypt( self, encryption ):
		return (encryption ** self._d)% self._N
		

	def messages(self):
		message_count = int (input ('Enter the number of messages: '))
		self.inputFunc(message_count)
		self.keyGen()
		encrypted_messages = []
		decrypted_messages = []
		dec_message = self.decrypted_decorator(self.printFunc)
		enc_message = self.encrypted_decorator(self.printFunc)
			
	
		for message in self._List:
			encrypted_messages.append( self.encrypt(message) )
			
		for em in encrypted_messages:
			print( enc_message(em))
			
		for message in encrypted_messages:
			decrypted_messages.append( self.decrypt( message ))

		for em in decrypted_messages:
			print( dec_message(em))
		
def main():

	RSA_list = RSA()
	RSA_list.messages()

if __name__ == '__main__': main()
