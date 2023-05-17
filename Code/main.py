from state import *

# define users game
player, computer = 'O', 'X'
# table tic-tac-toe
table_game = ['-', '-', '-', '-', '-', '-', '-', '-', '-']


def evalFunc(state):
    # check horizontal win
    for i in (0, 3, 6):
        if (state.state[i] == player and state.state[i+1] == player and state.state[i+2] == player):
            return 100 - state.depth

    # check vertical win
    for i in range(3):
        if (state.state[i] == 'X' and state.state[i+3] == 'X' and state.state[i+6] == 'X'):
            return 100 - state.depth

    # check diagonal win
    if ((state.state[0] == 'X' and state.state[4] == 'X' and state.state[8] == 'X') or (state.state[2] == 'X' and state.state[4] == 'X' and state.state[6] == 'X')):
        return 100 - state.depth

    # check for full board
    for i in range(9):
        if state.state[i] == '-':
            break
        if i == 8:
            return 0

    # if this triggers then no one has won yet
    return 0

def minimax(nextState):

    score = evalFunc(nextState)
    if score != 0:
        return score

    # Checks if there are any moves left
    for i in range(9):
        if nextState.state[i] == '-':
            break
        if i == 8:
            return 0

    if nextState.currPlayer == 'X':
        score_val = -100
        for i in range(9):
            if nextState.state[i] == '-':
                nextState.state[i] = 'X'
                score_val = max(score_val, minimax(
                    State(nextState.state, nextState, nextState.depth+1, None, computer)))
                nextState.state[i] = '-'
        return score_val


def next_state(state):
    nextState = State(state.state, state, state.depth+1, None, None)
    if state.currPlayer == 'X':
        score_val = -1000
        nextState.currPlayer = 'X'
    else:
        score_val = 1000
        nextState.currPlayer = 'X'

    bestStateIndex = -1
    for i in range(9):
        if nextState.state[i] == '-':
            nextState.state[i] = state.currPlayer
            newMoveVal = minimax(nextState)
            nextState.state[i] = '-'
            if state.currPlayer == 'X' and newMoveVal > score_val:
                score_val = newMoveVal
                bestStateIndex = i

            elif state.currPlayer == 'O' and newMoveVal < score_val:
                score_val = newMoveVal
                bestStateIndex = i
    if bestStateIndex != -1:
        nextState.state[bestStateIndex] = state.currPlayer

    print("Computer Turn :")
    return (nextState, score_val)


def check_win(state):
    # check horizontal win
    for i in (0, 3, 6):
        if (state.state[i] == player and state.state[i+1] == player and state.state[i+2] == player):
            print("Computer 'X' WIN")
        elif (state.state[i] == computer and state.state[i+1] == computer and state.state[i+2] == computer):
            print("Player 'O' WIN")

    # check vertical win
    for i in range(3):
        if (state.state[i] == 'O' and state.state[i+3] == 'O' and state.state[i+6] == 'O'):
            print("Player 'O' WIN")
        elif (state.state[i] == 'X' and state.state[i+3] == 'X' and state.state[i+6] == 'X'):
            print("Computer 'X' WIN")

    # check diagonal win
    if ((state.state[0] == 'O' and state.state[4] == 'O' and state.state[8] == 'O') or (state.state[2] == 'O' and state.state[4] == 'O' and state.state[6] == 'O')):
        print("Player 'O' WIN")

    elif ((state.state[0] == 'X' and state.state[4] == 'X' and state.state[8] == 'X') or (state.state[2] == 'X' and state.state[4] == 'X' and state.state[6] == 'X')):
        print("Computer 'X' WIN")

    # if this triggers then no one has won yet
    return print("game selesai")


# Will check whether the game is over, returns true if it's over.
def end_game(state):
    for i in range(9):
        if state.state[i] == '-':
            break
        if i == 8:
            return True

    # To check if horizontal win
    for i in (0, 3, 6):
        if (state.state[i] == player and state.state[i+1] == player and state.state[i+2] == player) or (state.state[i] == computer and state.state[i+1] == computer and state.state[i+2] == computer):
            return True

    # To check if vertical win
    for i in range(3):
        if (state.state[i] == 'O' and state.state[i+3] == 'O' and state.state[i+6] == 'O') or (state.state[i] == 'X' and state.state[i+3] == 'X' and state.state[i+6] == 'X'):
            return True

    # To check if diagonal win
    if ((state.state[0] == 'O' and state.state[4] == 'O' and state.state[8] == 'O') or (state.state[2] == 'O' and state.state[4] == 'O' and state.state[6] == 'O') or (state.state[0] == 'X' and state.state[4] == 'X' and state.state[8] == 'X') or (state.state[2] == 'X' and state.state[4] == 'X' and state.state[6] == 'X')):
        return True

    return False


def main():
    print("**** Game Tic Tac Toe ****\n")
    table_case = State(table_game, None, 0, None, computer)
    table_case.printState()

    while not end_game(table_case):
        # Get user input for row and column
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1

        # Make sure the chosen cell is empty
        while table_case.state[row * 3 + col] != '-':
            print("Invalid move! Please try again.")
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1

        # Make the user's move
        table_case.state[row * 3 + col] = player
        table_case.printState()

        # Check if the game is over
        if end_game(table_case):
            break

        # Make the AI's move
        steps = next_state(table_case)
        table_case = steps[0]
        table_case.printState()

    print("Goal State :")
    table_case.printState()
    # Test check_win
    print(check_win(table_case))
    return

if __name__ == "__main__":
    main()
