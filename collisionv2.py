#finding hash collisions in SHA256
#Usage: python3 <scriptname> <sample size> <hash size> <seed>
#by lightflix

import hashlib
import sys
import time

#a list that will be populated with hashes.
hash_list = []

#hash generator
def generator(seed,hash_list):

	print("\nGenerating hashes...\n")

	i=0

	#input seed is the starting point
	start = seed

	hash_list.append(start)

	#loop until the nth iteration
	while (i<int(sys.argv[1])):

		#hashlib shit, encode string to bytes.
		m = hashlib.sha256(bytes(start,'utf-8'))

		#store hash
		end = m.digest()

		#first five chars of the hash in hex is input for the next iteration
		start = end.hex()[0:int(sys.argv[2])]

		hash_list.append(start)
		print(start)

		#increment counter
		i+=1

	print("\nPopulated with "+str(i)+" hashes")

def floyds(hash_list):

	#count number of lines in file
	# line_count = len([line for line in f])
	line_count = int(sys.argv[1])

	#turtle and hare point to the beginning of the hash list
	turtle = hare = hash_list[0]

	#initialise turtle and hare pointers
	turtle_ptr = 0
	hare_ptr = 0

	#flag if a cycle is found.
	cycle_find = 0

	print("Cycle detection begins...\n")

	#detecc cycle, goes until hare runs out of track length in the race
	while hare_ptr < line_count:

		#intialise turtle and hare values, they point to the beginning of the hash list.
		turtle = hash_list[turtle_ptr]
		hare = hash_list[hare_ptr]

		#if at any point, an element (hash subset) the turtle points to is equal to that of the hare, cycle has been found 
		if turtle == hare and turtle!=sys.argv[3]:
			print("Cycle found\n")
			cycle_find = 1
			break

		#if cycle hasn't been found, carry on and increment turtle by one step and hare by two.
		if cycle_find == 0:
			turtle_ptr+=1
			hare_ptr+=2

	#detecc start and end of cycle
	if cycle_find == 1:

		#move turtle pointer to the start
		turtle_ptr = 0

		#hare keeps going until the end of list
		while hare_ptr < line_count:

			turtle = hash_list[turtle_ptr]
			hare = hash_list[hare_ptr]

			#if turle equals hare, then you've met again, but at the first element of the cycle. Go one step back on both to find out strings that cause the collision
			if turtle == hare:
				print("\n",sys.argv[2],"-char collision: ",hash_list[turtle_ptr-1]+" and "+hash_list[hare_ptr-1])
				return

			#increment one step at a time
			turtle_ptr+=1
			hare_ptr+=1

	else:
		print("No cycle found, try increasing sample size.")
		return

start_time = time.time()

#function(seed, filename)
generator(sys.argv[3],hash_list)

#function(filename)
floyds(hash_list)

print("\nExecution time: %s seconds " % (time.time() - start_time),"\n")
sys.stdout.write('\a')





