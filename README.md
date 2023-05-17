# Report Quiz 2

## Design & Analysis of Algorithms G

### Contributors

1. Muhammad Febriansyah - 5025211164
2. Heru Dwi Kurniawan - 5025211055

#### Contribution

- Heru Dwi Kurniawan (Report and create minimax algorithm code) - 50%
- Muhammad Febriansyah (Report and connect minimax algorithm to Tic Tac Toe games) - 50%

## Introduction

In this report, we will discuss the implementation of the Minimax algorithm in the game of Tic Tac Toe. Tic Tac Toe is a simple game commonly played by people of all ages. It is also known as noughts and crosses or Xs and Os. The game is played on a board consisting of nine squares forming three rows and three columns. In Tic Tac Toe, there are two players who compete against each other to place three symbols on the game board, which consists of nine squares. One player plays as X, and the other player plays as O. The objective of the game is to place three of the same symbols in a horizontal, vertical, or diagonal pattern.

Although Tic Tac Toe is relatively simple, it requires the right strategies in choosing the moves to win the game. One way to enhance the ability to play Tic Tac Toe is by utilizing artificial intelligence. In the field of artificial intelligence, there are various techniques and algorithms that can be used to solve problems related to games, and one of them is the Minimax algorithm. The Minimax algorithm is a type of algorithm in artificial intelligence used for decision-making in games with two opposing players, also known as Adversarial Search. In the context of Tic Tac Toe, the Minimax algorithm attempts to predict the opponent's moves and make the best decisions to counter those moves. This algorithm evaluates every possible move for both players and searches for the optimal move to maximize the chances of winning or minimize the chances of losing.

In this report, we will implement the Minimax algorithm, which is an Adversarial Search algorithm, to determine the optimal moves for the computer player in playing the game of Tic Tac Toe. The implementation of the Minimax algorithm aims to provide the computer player with the ability to play Tic Tac Toe effectively and achieve victory or at least secure a draw against a human player.

## Basic Theory

### 1. Minimax Algorithm

The Minimax algorithm is an algorithm used to make choices in order to minimize the possibility of losing the maximum value. This algorithm is applied in games involving two players such as tic tac toe, checkers, go and games that use strategy or other logic. This means that the games can be explained as a set of rules and premises.

### 2. Tic-Tac-Toe

Tic Tac Toe is a paper and pencil game, also known as Noughts and Crosses. The game is played with two players using only X/O symbols on a 3x3 grid. Like other board games, Tic Tac Toe has rules for playing. The rules are as follows:

1. The game involves only two players, one player and one computer.
2. The game starts with an empty grid.
3. The players take turns placing their predetermined X/O symbol onto an empty grid space.
4. The first player is assigned the O symbol, and the computer is assigned the X symbol.
5. Assuming the O symbol goes first, the player with the O symbol has one more or the same number of turns as the X symbol.
6. The game ends when one player successfully places their symbol in a horizontal, vertical, or diagonal line or when all the grid spaces are filled with symbols.
7. Once the game ends, neither player can make any further moves.

![Tic-Tac-Toe Board Image](https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Tic_tac_toe.svg/200px-Tic_tac_toe.svg.png)

## Code Analysis

- State representation: The code uses the State data structure to represent the state of the game at each step. The State object stores information such as state (current game state), parent (previous move), depth (step depth), action (steps taken), and currPlayer (current player).
- Minimax Algorithm: The code above uses the Minimax algorithm to determine the best move in a game of Tic-Tac-Toe. The Minimax algorithm is used to find the game state that produces the maximum score for the player currently playing (in this case 'O') and the minimum score for his opponent (in this case 'X'). This algorithm combines possible moves with an evaluation of state of game to choose best move.
- Evaluate Game State: The code uses evalFunc function to evaluate game state at each step. This function checks if there is win condition (horizontal, vertical or diagonal) for player 'X'. If present function returns score matching condition. If no win condition function checks if game ends in draw.
- Recursion and Backtracking: The Minimax algorithm is implemented recursively with help of minimax function. This function iterates through every possible step and calculates score using game state evaluation function also performs backtracking to return maximum or minimum score obtained from previous steps.
- Best Move: Code uses next_state function find best move that can be taken at current state of game.This function implements Minimax algorithm by iterating through each available step.For each step function calls minimax get score.Then move with best score selected applied to game state.
- Replay: Code uses while loop play games sequentially until game ends.At each iteration best move applied to game state and game state printed screen.This loop ends when end_game function returns True indicating that game over.
- Output Win Message: Code prints game steps and state screen using printState method State object.In addition code also prints win message based evaluating state of game using check_win function.

## Output Program
!image"(
