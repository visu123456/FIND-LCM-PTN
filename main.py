# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))


def printSubSequences(STR, subSTR=""):
	"""
	function:
		To print all subsequences of string
		concept:
			Pick and Don’t Pick
		variables:
			STR = string
			subSTR = to store subsequence
	"""
	if len(STR) == 0:
		print(subSTR, end=" ")
		return

	# we add adding 1st character in string
	printSubSequences(STR[:-1], subSTR + STR[-1])
	"""
	Not adding first character of the string
	because the concept of subsequence either
	character will present or not
	"""
	printSubSequences(STR[:-1], subSTR)
	return


def main():
	"""
	main function to drive code
	"""
	STR = "abc"
	printSubSequences(STR)


if __name__ == "__main__":
	main()

# by itsvinayak
