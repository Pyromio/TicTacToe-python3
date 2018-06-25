import random

def print_board(board):
	print(board[0], board[1], board[2])
	print(board[3], board[4], board[5])
	print(board[6], board[7], board[8])

def player_move(board):
	player_input = ""
	possible_moves = []
	for position in board:
		if position != "X" and position != "O":
			possible_moves.append(position)
	while player_input not in possible_moves:
		try:
			player_input = int(input("Enter a number: "))
		except Exception as e:
			pass
	board[player_input] = "X"
	return board

def computer_move(board):
	possible_moves = []
	for position in board:
		if position != "X" and position != "O":
			possible_moves.append(position)
	board[random.choice(possible_moves)] = "O"
	return board

def check_for_win(board):
	win = ""
	positions_to_win = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
						[0, 3, 6], [1, 4, 7], [2, 5, 8],
						[0, 4, 8], [2, 4, 6]]
	for win_moves in positions_to_win:
		if board[win_moves[0]] == "X" and board[win_moves[1]] == "X" and board[win_moves[2]] == "X":
			win = "Player"
			break
		if board[win_moves[0]] == "O" and board[win_moves[1]] == "O" and board[win_moves[2]] == "O":
			win = "Computer"
			break
	return win

def main():
	board = []
	for i in range(9):
		board.append(i)
	playing = True
	print_board(board)
	while playing:
		board = player_move(board)
		print_board(board)
		if check_for_win(board) == "Player":
			print("Congratulations you won!")
			break
		board = computer_move(board)
		print_board(board)
		if check_for_win(board) == "Computer":
			print("You lose! Try again.")
			break
	input()

main()
