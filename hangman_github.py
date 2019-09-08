
import requests
import random

def hangman(): #creates the 2D list for appending the man

	x = []
	for y in range(10):
		height=[]
		for first_digit in range(10):
			height.append(' ')
		x.append(height)
	return x

board = hangman() #creates variable containing the hangman

def drawing(): #print out the drawing of the board 
	
	print("-" * 10)
	x = []
	for y in range(10):
		height=[ ' '.format(elem) for elem in range(10)]
		print('|' +''.join(height))
		x.append(height)

def drawing_man(attempt_counter): #wrong attempt results in drawing the man
	print('-' * 10)
	if attempt_counter == 1: 
		for line in board:
			board[0][5] = "|"
			print('|' + ''.join(line))

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

def user_input(): #gets user input as a letter
	
	while True:
		user_q = (input("Guess a letter?: ").strip()).lower()
		if not user_q:
			print("You have not entered a letter, please try again.")
		# user_qq = input("Your new letter: ")
		elif len(user_q) > 1:
			print("You have entered a word, please enter a letter instead.")
		else:
			break
	return user_q

correct_letters = [] #stores correct letters guessed

def play(): #loop for playing the game
	
	drawing() #prints out drawing for the initial part of the game
	print("Let\'s play Hangman!")
	print("You will have 7 attempts which draws out the hangman before you fail.")
	print("Guess this word: (Picking random word..)")

	#generates random word and print out the underscores here

	word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

	response = requests.get(word_site)
	words = response.content.splitlines()
	word = random.choice(words)
	word = (word.decode('utf-8')).lower()

	guessing_line = ""
	for line in word:
		guessing_line += "_ "
	print(guessing_line)

	board = hangman()
	m = 1
	

	while True:

		user_a = user_input()


		guessing_list = []
		for line in word:
			guessing_list.append("_ ")

		guessing_list1 = []		#creates list to check if == word later  
		for line in word:
			guessing_list1.append("_ ")

		dict_word = { i:j for i,j in enumerate(word)}

		temp = [index for index, value in enumerate(word) if value in correct_letters]
			
		for num in temp:
			guessing_list[num] = dict_word[num] + " "
			guessing_list1[num] = dict_word[num]

		if user_a in word:
			correct_letters.append(user_a)

			temp = [index for index, value in enumerate(word) if value in correct_letters]
			
			for num in temp:
				guessing_list[num] = dict_word[num] + " "
				guessing_list1[num] = dict_word[num]
			
			guess = "".join(guessing_list1)
			print("".join(guessing_list))
			print("\"" + user_a + "\"" + " is in the word.")
			if guess == word:
				print("You win!")
				break
			
		
		elif user_a not in word:
			attempts = [n for n in range(1,8)]
			print("".join(guessing_list))

			if m in attempts:
				
				print("Oops, letter was not in word. Guess again. Extending the hangman...")
				drawing_man(m)
				 
				if m == 7:
					print("You have lost!")
					print("The word was \"" + word + "\".")
					break

				m += 1


if __name__ == "__main__": 
	while True:
		play()
		quit = (input("Would you like to try again? Type 'y' or 'n': ").strip()).lower()
		if quit.lower() == "n":
			print("Thanks for playing!")
			break
