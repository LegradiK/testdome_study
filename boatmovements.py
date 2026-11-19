game_matrix = [
    [False, True,  True,  False, False, False],
    [True,  True,  True,  False, False, False],
    [True,  True,  True,  True,  True,  True],
    [False, True,  True,  False, True,  True],
    [False, True,  True,  True,  False, True],
    [False, False, False, False, False, False],
]

def can_travel_to(game_matrix, from_row, from_column, to_row, to_column):
    rows = len(game_matrix)
    columns = len(game_matrix[0])
    # print(rows, columns)

    # boat needs to start from within the range
    if rows > from_row >= 0 and columns > from_column >= 0:
        # boat can only move within the range
        if rows > to_row >=0 and columns > to_column >= 0:

            # boat needs to start from the water
            if game_matrix[from_row][from_column] == False:
                # print("You're on the land.")
                return False

            # Boat can only go to the water - not the land
            if game_matrix[to_row][to_column] == False:
                # print("Boat can't go to the land")
                return False

            row_move = to_row - from_row
            col_move = to_column - from_column

            # allowed moves: up 1, down 1, left 1, right 1, right 2
            if (row_move, col_move) in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
                return True
            if (row_move, col_move) == (0, 2):
                # the square passed over must also be water
                return game_matrix[from_row][from_column + 1]

    return False
  
    
print(can_travel_to(game_matrix, 3, 2, 2, 2)) # True, Valid move
print(can_travel_to(game_matrix, 3, 2, 3, 4)) # False, Can't travel through land
print(can_travel_to(game_matrix, 3, 2, 6, 2)) # False, Out of bounds