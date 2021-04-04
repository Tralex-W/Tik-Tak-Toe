import pygame, sys, numpy as np

pygame.init()
#VARIABLES
WIDTH = 600
HEIGHT = 600
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
LINE_WIDTH = 15
RED  = (255, 0, 0)
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CIRCLE_COLOR = (239, 231, 231)
CROSS_WDITHD = 25
SPACE = 55
CROSS_COLOR = (66, 66, 66)

#SCREEN
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("TIK TAK TOE") 
screen.fill(BG_COLOR) 

#CONSOL_BOARD
board = np.zeros((3, 3)) 
player = 2 
game_over = False

#FUNCTIONS
def draw_lines(): 
    pygame.draw.line(screen, LINE_COLOR, (0,200), (600,200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0,400), (600,400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200,0), (200,600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400,0), (400,600), LINE_WIDTH)
def draw_figures(): 
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * (WIDTH / 3) + (HEIGHT / 6)),int(row * (WIDTH / 3) + (HEIGHT / 6))), CIRCLE_RADIUS, CIRCLE_WIDTH )
            elif board[row][col] == 2: 
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row*200 +200 -SPACE), (col * 200 +200 -SPACE, row *200 + SPACE), LINE_WIDTH )
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row*200 +SPACE), (col * 200 +200 -SPACE, row *200 + 200 - SPACE), LINE_WIDTH )
def draw_vertical_win_line(col, player):
    posX = col * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT -15), LINE_WIDTH)
def draw_horizontal_win_line(row, player):
    posY = row * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), LINE_WIDTH)
def draw_as_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH -15, 15), LINE_WIDTH)
def draw_ds_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), LINE_WIDTH)
def mark_square(row, col, player):
    board[row][col] = player
def check_square(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False
def check_win(player):
    	# vertical win check
	for col in range(3):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			draw_vertical_win_line(col, player)
			return True

	# horizontal win check
	for row in range(3):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			draw_horizontal_win_line(row, player)
			return True

	# asc diagonal win check
	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		draw_as_diagonal(player)
		return True

	# desc diagonal win chek
	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		draw_ds_diagonal(player)
		return True

	return False
def is_board_full():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return False
def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(3):
        for col in range(3):
            board[row][col] = 0

draw_lines()


#MAIN_LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if check_square( clicked_row, clicked_col) == True:
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player) == True:
                        game_over = True
                    player = 2

                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player) == True:
                        game_over = True
                    player = 1
                print(board)
                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                restart()
                player = 2
                game_over = False

    pygame.display.update()