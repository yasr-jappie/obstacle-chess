import sys
import os
import stdarray

#       a b c d e f g h
#
#  8    r n b q k b n r    8
#  7    p p p p p p p p    7
#  6                       6 
#  5                       5
#------------------------------------
#  4                       4
#  3                       3
#  2    P P P P P P P P    2
#  1    R N B Q K B N R    1  
#
#       a b c d e f g h     

# white pieces
w_king_count = 0
w_queen_count = 0
w_bishop_count = 0
w_knight_count = 0
w_castle_count =0
w_pawn_count = 0

# black pieces
b_king_count = 0
b_queen_count = 0
b_bishop_count = 0
b_knight_count = 0
b_castle_count = 0
b_pawn_count = 0

king_count = 0
queen_count = 0
bihsop_count = 0
knight_count = 0
castle_count =0
pawn_count = 0

#walls
south_wall_count = 0
west_wall_count = 0

# trapdoors

# mines
mine_count = 0
trapdoor_count = 0

x_count = 0


valid_pieces = ['K','k','Q','q','B','b','N','n','R','r','P','p']
valid_char = ['K','k','Q','q','B','b','N','n','R','r','P','p','.','|','_','X','D','O','M']


error_illegal_board = "ERROR: illegal chess_board at "
error_illegal_status_line = "ERROR: illegal chess_board at status line "

def termination(message, position):
    # Terminate the program and display an appropriate message.
    sys.stderr.write(message + position)
    sys.exit(0)

def rank_length_check(rank):
    if len(rank) > 8 or len(rank) < 8:
        return print(error_illegal_board)

def string_to_int(word):
    word = int(word)

# function to get the chess board position
def get_chessboard_position(row, col):
    row_num = 8 - row  # Calculate the row number correctly
    col_letter = chr(ord('a') + col)
    return f"{col_letter}{row_num}"

def find_invalid_piece_positions(chess_board, valid_pieces):

    for row in range(8):
        for col in range(8):
            piece = chess_board[row][col]
            if piece and piece not in valid_pieces:
                position = get_chessboard_position(row, col)
                
    return position

def game_end(status):
    status = False

# input and output files from the command line
input_file = sys.argv[1]
output_file = sys.argv[2]

std_board = []
validity = True


with open(input_file, 'r') as file:

    # read all content from a file using read()
    content = file.read()

    # splitting the file into separate lines
    lines = content.splitlines()

    r_count = content.count('r')
    n_count = content.count('n')
    b_count = content.count('b')
    q_count = content.count('q')
    k_count = content.count('k')
    p_count = content.count('p')
    R_count = content.count('R')
    N_count = content.count('N')
    B_count = content.count('B')
    Q_count = content.count('Q')
    K_count = content.count('K')
    P_count = content.count('P')
    mine_and_trapdoor_count = content.count('X')
    mine_count = content.count('M')
    westwall_count = content.count('_')
    southwall_count = content.count('|')
    open_trapdoor_count = content.count('O')
    hidden_trapdoor_count = content.count('D')
    dot_count = content.count('.')

    for rank in lines:
        if not rank.startswith('%'):
            row =[]
            for col in rank:
                if col in valid_char:
                    row.append(col)
            std_board.append(row)

    # append each valid row to the 
    file_board = []
    file_board.append(std_board[0])
    file_board.append(std_board[1])
    file_board.append(std_board[2])
    file_board.append(std_board[3])
    file_board.append(std_board[4])
    file_board.append(std_board[5])
    file_board.append(std_board[6])
    file_board.append(std_board[7])

    chess_board = stdarray.create2D(8, 8, '')
    line = 0
    for i in range(8):
        tile = 0
        for j in file_board[i]:
            if j == "|" or j == '_' :
                chess_board[line][tile] += j
            elif j not in valid_char: pass

            else: 
                chess_board[line][tile] += j
                tile += 1
        line += 1
    for row in range(8):
        for col in range(8):
            # king checks
            if chess_board[row][col] == "K":
                if w_king_count < 1:
                    w_king_count += 1
                else:
                    termination(error_illegal_board,get_chessboard_position(row,col))
            if chess_board[row][col] == "k":
                if b_king_count < 1:
                    b_king_count+= 1
                
                else: termination(error_illegal_board,get_chessboard_position(row,col))

            # pawn checks
            elif chess_board[row][col] == "P":
                if w_pawn_count < 8:
                    w_pawn_count+= 1
                else: termination(error_illegal_board,get_chessboard_position(row,col))
            elif chess_board[row][col] == "p":
                if b_pawn_count < 8:
                    b_pawn_count+= 1
                else: termination(error_illegal_board,get_chessboard_position(row,col))

            # queen checks
            elif chess_board[row][col] == "Q":
                if w_queen_count < 1:
                    w_queen_count+= 1
                elif w_queen_count >=2 or w_queen_count <9:
                    if P_count < 8:
                        w_queen_count += 1
                else: termination(error_illegal_board,get_chessboard_position(row,col))
            elif chess_board[row][col] == "q":
                if b_queen_count < 1:
                    b_queen_count+= 1
                elif b_queen_count >=2 or b_queen_count <9:
                    if p_count < 8:
                        b_queen_count += 1
                else: termination(error_illegal_board,get_chessboard_position(row,col))

            # bishop checks
            elif chess_board[row][col] == "B":
                if w_bishop_count < 2:
                    w_bishop_count+= 1
                elif w_bishop_count >=2 or w_bishop_count <10:
                    if p_count < 8:
                        w_bishop_count += 1
                else: termination(error_illegal_board,get_chessboard_position(row,col))
            elif chess_board[row][col] == "b":
                if b_bishop_count < 2:
                    b_bishop_count+= 1
                elif b_bishop_count >=2 or b_bishop_count <10:
                    if p_count < 8:
                        b_bishop_count += 1
                else: termination(error_illegal_board,get_chessboard_position(row,col))

            # knight checks
            elif chess_board[row][col] == "N":
                if w_knight_count < 2:
                    w_knight_count+= 1
                elif w_knight_count >=2 or w_knight_count <10:
                    if p_count < 8:
                        w_knight_count += 1
                else: termination(error_illegal_board,get_chessboard_position(row,col))
            elif chess_board[row][col]  == "n":
                if b_knight_count < 2:
                    b_knight_count+= 1
                elif b_knight_count >=2 or b_knight_count <10:
                    if p_count < 8:
                        b_knight_count += 1
                else: termination(error_illegal_board,get_chessboard_position(row,col))

            # rook or castle checks
            elif chess_board[row][col] == "R":
                if w_castle_count < 2:
                    w_castle_count+= 1
                elif w_castle_count >=2 or w_castle_count <10:
                    if p_count < 8:
                        w_castle_count += 1
                else: termination(error_illegal_board,get_chessboard_position(row,col))
            elif chess_board[row][col] == "r":
                if b_castle_count < 2:
                    b_castle_count+= 1
                elif b_castle_count >=2 or b_castle_count <10:
                    if p_count < 8:
                        b_castle_count += 1
                else: termination(error_illegal_board,get_chessboard_position(row,col))

            # wall count
            elif chess_board[row][col] == "|" :
                if west_wall_count < 3:
                    west_wall_count += 1
                else: termination(error_illegal_board,get_chessboard_position(row,col))
            elif chess_board[row][col] == "_" :
                if south_wall_count < 3:
                    south_wall_count += 1
                else: termination(error_illegal_board,get_chessboard_position(row,col))

            # mine count
            elif chess_board[row][col] == 'M':
                if mine_count <2:
                    mine_count += 1
                else: termination(error_illegal_board,get_chessboard_position(row,col))
            # trapdoor
            elif chess_board[row][col] == 'X':
                if trapdoor_count < 2:
                    trapdoor_count += 1
                else: termination(error_illegal_board,get_chessboard_position(row,col))
    # rank length validation
    for row in chess_board: 
        for col in row : 
            if len(row) > 8: 
                termination(error_illegal_board,get_chessboard_position(row,8))
            elif len(row) < 8:
                termination(error_illegal_board,get_chessboard_position(row),7)

    for row in range(8): 
        for col_index, col in enumerate(chess_board[row]):
            position = get_chessboard_position(row, col_index)  

            position = get_chessboard_position(row, chess_board[row].index(col))
            if (col == 'P' or col == 'p') and (row == 0 or row == 7):
                termination(error_illegal_board, position)
            elif (col =="X" or col =="M") and (row == 0 or row == 1 or row == 2 or row == 5 or row == 6 or row == 7):
                termination(error_illegal_board, position)
            elif (col =='D' ) and (row== 2 or row ==3 or row ==4 or row == 5 ):
                termination(error_illegal_board,position)
    
    # variable containg the status line
    status_line = lines[8]
    status_line = str(status_line)
    status_line = status_line.replace(" ", "")

    # white or black in status line
    # first states who moves next
    # w for white and b for black
    status_line[0]
    if status_line[0] == 'w' or status_line[0] == 'b':
        pass
    else:
        termination(error_illegal_status_line,'')
    
    # number of remaining walls for white
    rem_white_walls = int(status_line[1])
    if rem_white_walls > 3:
        termination(error_illegal_status_line,'')

    # number of remaining walls for black
    rem_black_walls = int(status_line[2])
    if rem_black_walls > 3:     
        termination(error_illegal_status_line,'')
    # castling availability 
    # white kingside, white queenside , black kingside and black queenside
    status_line[3]
    status_line[4]
    status_line[5]
    status_line[6]
    # en passant target square
    status_line[7]

    # Halfmove clock
    if int(status_line[8]) < 0:
        termination(error_illegal_status_line,'')

    status_line_output = lines[8] 
    output_f = open(output_file, "w")
    output_f.writelines(chess_board[0])
    output_f.writelines("\n")
    output_f.writelines(chess_board[1])
    output_f.writelines("\n")
    output_f.writelines(chess_board[2])
    output_f.writelines("\n")
    output_f.writelines(chess_board[3])
    output_f.writelines("\n")
    output_f.writelines(chess_board[4])
    output_f.writelines("\n")
    output_f.writelines(chess_board[5])
    output_f.writelines("\n")
    output_f.writelines(chess_board[6])
    output_f.writelines("\n")
    output_f.writelines(chess_board[7])
    output_f.writelines("\n")
    output_f.writelines(status_line_output)
