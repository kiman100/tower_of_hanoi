#!/usr/bin/python
def Hanoi():
	moveCount = 0
	length = 'abc'
	while(length.isdigit()==False):
		length = raw_input('How many numbers do you want? ')
	length = int(length)
	post_list = [[],[],[]]
	length_plus_1 = length+1
	for x in range(1,length_plus_1):
		post_list[0].append(x)
	post_list[0].append(length_plus_1)
	post_list[1].append(length_plus_1)
	post_list[2].append(length_plus_1)
	while(len(post_list[2])<length_plus_1):
		humor_mom(post_list,length)
		userinput = raw_input(str())
		if(len(userinput)!=2):
			print 'Oops!'
			print 'Looks like you diddent enter in the right input format'
			print 'The format to use is, first the number of what list you are trying to take something from'
			print 'The second number is were you are trying to move it.'
			print 'you can only put 2 numbers, no more no less'
			print'(and no letters)'
		else:
			takefrom = userinput[0]
			goto = userinput[1]
			if(takefrom.isdigit() and goto.isdigit()):
				takefrom = int(takefrom)-1
				goto = int(goto)-1
				if(takefrom>2 or takefrom<0):
					print'Oops'
					print'looks like you did not put in a valid input'
					print'it has to be 2 numbers that are from 1 to 3'
				elif(goto>2 or goto<0):
					print'Oops'
					print'looks like you did not put in a valid input'
					print'it has to be 2 numbers that are from 1 to 3'
				else:
					if(post_list[goto][0]>post_list[takefrom][0]):
						moveCount += 1
						post_list[goto].insert(0,post_list[takefrom][0])
						post_list[takefrom].pop(0)
					else:
						print 'Oops!'
						print 'looks like you are trying to move a bigger number onto a smaller number.'
						print 'You can only move a number to another number if the number you are trying to move is less than the number you are trying to move it onto.'
			else:
				print'Oops'
				print'looks like you did not put in a valid input'
				print'it has to be 2 numbers that are from 1 to 3'

	humor_mom(post_list,length)
	minMoves = 1
	for x in range(1,length):
		minMoves = minMoves*2 + 1
	print 'Congratulations you won in '+str(moveCount)+' moves!!!'
	print ' minimum amount of moves is '+str(minMoves)
def humor_mom(list_of_posts,numRings):
	list_0_dif =numRings- len(list_of_posts[0])+1
	list_1_dif =numRings- len(list_of_posts[1])+1
	list_2_dif =numRings- len(list_of_posts[2])+1
	for x in range(0,numRings):
		toprint = ''
		if(x>=list_0_dif):
			toprint=toprint+'%2d   '%(list_of_posts[0][x-list_0_dif])
		else:
			toprint=toprint+'     '
		if(x>=list_1_dif):
			toprint=toprint+'%2d   '%(list_of_posts[1][x-list_1_dif])
		else:
			toprint=toprint+'     '
		if(x>=list_2_dif):
			toprint=toprint+'%2d   '%(list_of_posts[2][x-list_2_dif])
		else:
			toprint=toprint+'     '
		print toprint
	print'____________________'
Hanoi()
