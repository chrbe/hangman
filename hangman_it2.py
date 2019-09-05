#= [] create an hangman image
#= [] print hangman image
#= [] every time function a is wrong , add to the hangman
#= [] function a that takes wrong input to the hangman
#= [] function that takes a response from user
#= [] function a that decides if the response is right or wrong

import requests
import random



def hangman():

	#print("-" * 10)
	x = []
	for y in range(10):
		height=[]
		for first_digit in range(10):
			height.append(' ')
		x.append(height)
	return x
	#print("|" + "".join(x))

#print(hangman())

board = hangman()

# print(board)

def drawing(): #print out the drawing of the board 
	
	print("-" * 10)
	x = []
	for y in range(5):
		height=[ ' '.format(elem) for elem in range(10)]
		print('|' +''.join(height))
		# for first_digit in range(10):
		# 	height.append(" ")
	# 	x.append(height)
	# print(x)

# drawing()

#Class drawing_head(attempt)
def drawing_man(attempt): #wrong attempt results in drawing the man
	print('-' * 10)
	attempt_counter = attempt
	# while True:
	# 	attempt += 1
	if attempt_counter == 1: #if then else ? conditional statements? nested if?
		for line in board:
			board[0][5] = "|"
			print('|' + ''.join(line))
	# if attempt =2:
	# 	for line
	if attempt_counter == 2:
		for line in board:
			board[0][4] = "|"

			board[0][5] = "_"
			board[1][4] = "|"
			board[1][6] = "|"
			board[1][5] = "_"
			print('|' + ''.join(line))
	
	if attempt_counter == 3:
		for line in board:
			board[0][4] = "|"

			board[0][5] = "_"
			board[1][4] = "|"
			board[1][6] = "|"
			board[1][5] = "_"

			board[2][5] = "|"
			board[3][5] = "|"
			board[4][5] = "|"
			board[5][5] = "|"
			print('|' + ''.join(line))

	if attempt_counter == 4:
		for line in board:
			board[0][4] = "|"

			board[0][5] = "_"
			board[1][4] = "|"
			board[1][6] = "|"
			board[1][5] = "_"

			board[2][5] = "|"
			board[3][5] = "|"
			board[4][5] = "|"
			board[5][5] = "|"

			board[3][3] = "-"
			board[3][4] = "-"
			print('|' + ''.join(line))
			
	if attempt_counter == 5:
		for line in board:
			board[0][4] = "|"

			board[0][5] = "_"
			board[1][4] = "|"
			board[1][6] = "|"
			board[1][5] = "_"

			board[2][5] = "|"
			board[3][5] = "|"
			board[4][5] = "|"
			board[5][5] = "|"

			board[3][3] = "-"
			board[3][4] = "-"

			board[3][6] = "-"
			board[3][7] = "-"
			print('|' + ''.join(line))

	if attempt_counter == 6:
		for line in board:
			board[0][4] = "|"

			board[0][5] = "_"
			board[1][4] = "|"
			board[1][6] = "|"
			board[1][5] = "_"

			board[2][5] = "|"
			board[3][5] = "|"
			board[4][5] = "|"
			board[5][5] = "|"

			board[3][3] = "-"
			board[3][4] = "-"

			board[3][6] = "-"
			board[3][7] = "-"

			board[5][3] = "-"
			board[5][4] = "-"
			print('|' + ''.join(line))		
				
	if attempt_counter == 7:
		for line in board:
			board[0][4] = "|"

			board[0][5] = "_"
			board[1][4] = "|"
			board[1][6] = "|"
			board[1][5] = "_"

			board[2][5] = "|"
			board[3][5] = "|"
			board[4][5] = "|"
			board[5][5] = "|"

			board[3][3] = "-"
			board[3][4] = "-"

			board[3][6] = "-"
			board[3][7] = "-"

			board[5][3] = "-"
			board[5][4] = "-"

			board[5][6] = "-"
			board[5][7] = "-"
			print('|' + ''.join(line))
		# print("You have lost!")	

	# print(board) 


# pic = drawing_man(7)

def user_input(): #gets user input 
	
	while True:
		user_q = (input("Guess a letter?: ").strip()).lower()
		if not user_q:
			print("You have not entered a letter, please try again.")
		# user_qq = input("Your new letter: ")
		elif len(user_q) > 1:
			print("You have entered a word, please enter a letter instead.")
		else:
			break
	# user_q = user_q.split()
	# if test >= len(word)/2:
	# 	guess = input(print("Guess? Y/N"))
	# 	if guess is "Y":
	# 		guess_word = input(print("What's the word:"))
	#print(user_q)
	return user_q

#def word_generator(): pass function that allows the
correct_letters = []

def guess_word(user_a, word): #determines if input is right or wrong 
	guessing_list = []
	for line in word:
		guessing_list.append("_ ")
	# print(guessing_list)


	# guessing_line = ""
	# for line in word:
	# 	guessing_line += "_ "
	# print(guessing_line)
	
	if user_a in word:
		correct_letters.append(user_a)

	dict_word = { i:j for i,j in enumerate(word) }

	temp = [index for index, value in enumerate(word) if value in correct_letters]
	# print(temp)

	# attempt = 0
	if temp != []:

		for num in temp:
	 		guessing_list[num] = dict_word[num] + " "
		print("".join(guessing_list))
		# print(guessing_list)

#need a function that instantiates every time the user input is created

def restart():
	answer = input("Play again? Y/N: ").upper()
	if restart == "Y":
		print("Restarting game..")
		play()
	elif restart == "N":
		print("Thanks for playing!")


# restart()

def play():
	# game_start = False
	print("Let\'s play Hangman!")
	# print(pic)
	print("Guess this word: (Hang on a few seconds..)")

	#generates random word and print out the underscores here

	word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

	response = requests.get(word_site)
	words = response.content.splitlines()
	word = random.choice(words)
	word = word.decode('utf-8')
	word = word.lower()
	# print(word)

	guessing_line = ""
	for line in word:
		guessing_line += "_ "
	print(guessing_line)

	board = hangman()
	m = 1
	# correct_letters = []
	

	while True:
		# guessing_line = ""
		# for line in word:
		# 	guessing_line += "_ "
		# print(guessing_line)

		user_a = user_input()
		# guess_word(user_a, word)


	#guess_word function 
		guessing_list = []
		for line in word:
			guessing_list.append("_ ")
		# print(guessing_list)

		guessing_list1 = []		#creates list to check if == word later  
		for line in word:
			guessing_list1.append("_ ")

		dict_word = { i:j for i,j in enumerate(word)}

		temp = [index for index, value in enumerate(word) if value in correct_letters]
			# print(temp)
		for num in temp:
			guessing_list[num] = dict_word[num] + " "
			guessing_list1[num] = dict_word[num]
			# print(type(guessing_list))

		if user_a in word:
			correct_letters.append(user_a)

			temp = [index for index, value in enumerate(word) if value in correct_letters]
			# print(temp)
			for num in temp:
				guessing_list[num] = dict_word[num] + " "
				guessing_list1[num] = dict_word[num]
			# print(type(guessing_list))
			shazam = "".join(guessing_list1)
			print("".join(guessing_list))
			if shazam == word:
				print("You win!")
				break
			
		# attempt = 0
		# if temp != []:
			
			# print(shazam)
			

		# elif temp == [] and :
		# 	print(guess_word.counter)
		# 	print("Oops, wrong letter, guess again!")
		# 	drawing_man(guess_word.counter)
		
		elif user_a not in word:
			attempts = [n for n in range(1,8)]
			print("".join(guessing_list))

			if m in attempts:
				
				print("Oops, wrong letter, guess again! Extending the hangman...")
				drawing_man(m)
				 
				if m == 7:
					print("You have lost!")
					print("The word was " + word + ".")
					break

				m += 1


if __name__ == "__main__":
	while True:
		play()
		quit = input("Would you like to try again? Type Y or N: ")
		if quit.lower() == "n":
			print("Thanks for playing!")
			break
