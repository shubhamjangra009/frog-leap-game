# Solution is present in the last line of code as a comment, try if you get stuck solving the puzzle :)

# 'B' is brown frog, 'G' is green frog and '_' is empty stone
initial_positions = ['B', 'B', 'B', '_', 'G', 'G', 'G']

# indexing positons
indexing_positions = [i for i in range(0, 7)]

# game winning condition when all brown frogs reach to right end and green frog to the left
winning_state = ['G', 'G', 'G', '_', 'B', 'B', 'B']

print('***** FROG 🐸 LEAP PUZZLE *****')
print('Instructions: Brown frog can only jump to the right & Green frog can only jump to the left')
print("NOTE: Pressing any other number from range 0 to 6 will instantly end the game, Don't press any alphabet!!!")
game = 'ON'

while game == 'ON':
    print('--------------------------------------------')
    print(f'{indexing_positions}')
    print(initial_positions)
    print('--------------------------------------------')
    if initial_positions == winning_state:
        print('VOILA!!! YOOUUUU WOONNNN 🏆')
        break

    user_input_position = int(
        input("Choose any position from 0 to 6 to make frog jump: "))

    if user_input_position not in indexing_positions:
        print('GAME END, YOU LOSE!')
        break
    else:
        # if user_input_position is not empty stone
        if initial_positions[user_input_position] != '_':
            # if selected frog is brown
            if initial_positions[user_input_position] == 'B':
                # if there's a empty stone on the next step or after the next step then only brown frog can jump

                # jump one step forward
                if initial_positions[user_input_position + 1] == '_':
                    temp1 = initial_positions[user_input_position]
                    initial_positions[user_input_position] = initial_positions[user_input_position + 1]
                    initial_positions[user_input_position + 1] = temp1

                # jump two step forward
                elif initial_positions[user_input_position + 2] == '_':
                    temp2 = initial_positions[user_input_position]
                    initial_positions[user_input_position] = initial_positions[user_input_position + 2]
                    initial_positions[user_input_position + 2] = temp2

                else:
                    print('Invalid move ⚠️⚠️⚠️')

            # if selected frog is green
            elif initial_positions[user_input_position] == 'G':
                # if there's a empty stone on the previous step or before the previous step then only green frog can jump

                # jump one step forward
                if initial_positions[user_input_position - 1] == '_':
                    temp1 = initial_positions[user_input_position]
                    initial_positions[user_input_position] = initial_positions[user_input_position - 1]
                    initial_positions[user_input_position - 1] = temp1

                # jump two step backward
                elif initial_positions[user_input_position - 2] == '_':
                    temp2 = initial_positions[user_input_position]
                    initial_positions[user_input_position] = initial_positions[user_input_position - 2]
                    initial_positions[user_input_position - 2] = temp2
                    # print('--------------------------------------------\n')
                    # print(initial_positions)

                else:
                    print('Invalid move ⚠️⚠️⚠️')

        # user selected empty stone
        elif initial_positions[user_input_position] == '_':
            print(
                'WARNING ⚠️ You can only select the frog 🐸 not the empty positioned stone!!!\n')


# SOLUTION : 4 2 1 3 5 6 4 2 0 1 3 5 4 2 3
# Press these numbers one by one in series
