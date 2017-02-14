Command Line Pente  
======  

**First four hours:** https://github.com/jabrabec/pente/releases/tag/four_hour_mark  

The problem presented in this test – to write a command-line version of the game Pente – posed a unique challenge as I was initially unfamiliar with the game in any context. However, after understanding the basics of how the game is played and doing some whiteboard brainstorming for how to approach the problem, breaking it down into manageable pieces seemed feasible.  

I recently wrote a command line tic-tac-toe game as a challenge for my own edification, and recognized elements from that experience that could be applied to this game, such as creating and manipulating the textual game board and handling player input and basic computer moves for randomly setting pieces. I was able to refactor some of my existing code for this purpose. I entirely redesigned the `make_board()`  function, however, in order to generate it iteratively instead of statically. For the rest of the task I focused on the logic behind determining winning moves.  

I’ve had some previous learning experience with designing a command-lined based Boggle game which used recursion for moving around the game board from any given (x, y) coordinate to find word matches, and decided to use a similar approach for finding winning sequences here. Recursion allowed the program to check for 5 sequential pieces of the same value until the base case of `count == 5` was satisfied, or until the function ultimately exited when no sequential matches were found. A sequence of 5 Xs or Os in a row along any of the axes indicated by the arrows below, if originating at the (1, 1) coordinate and/or the (5, 1) coordinate, would constitute a win:  

![alt text](https://github.com/jabrabec/pente/blob/master/5x5_layout.png?raw=true)  
 
From here, recursion simply needs to look at occupied spaces on the board with an index of `[x][y]` and compare the value in that location to that in the neighboring index: `[x+1][y]`, `[x][y+1]`, `[x+1][y+1]`, or `[x-1][y+1]`, while also incrementing the passed value of `[x]` and/or `[y]` accordingly in the next function call. In order to avoid index errors, the row & column coordinate values passed to the `check_for_five` function initially had a boolean check to limit the coordinates where the check for a sequence of 5 could start (i.e. the 11th column for a left to right horizontal sequence [columns 11, 12, 13, 14, 15]). Then, any time a marker is placed, the function to check winning moves could be called and end the game.  

The files in this repo are in two states; one release tagged `four_hour_mark` represents my first four hours of work. In this state, the game will launch, accept player input, and place computer pieces randomly. It does not stop, however, until all board spaces are occupied.  

Two functions were in progress - `check_for_five` and `check_for_winner` - but were not yet incorporated into the game workflow by the time of this repo tag. The `check_for_five` function will work to correctly identify horizontal, vertical, and diagonal-downward sequences of 5, but not for diagonal-upward ones. If the program is loaded into the Python interpreter, the `check_for_winner` function does not function well but can be tested by manually calling it:  

`python -i pente.py`  

(ctrl+C to stop the automatically invoked `start_game()` script  

```
board = make_board()  
board[1][1] = ' X'  
board[1][2] = ' X'  
board[1][3] = ' X'  
board[1][4] = ' X'  
board[1][5] = ' X'  
print_board(board)  
   1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
 1  X  X  X  X  X  .  .  .  .  .  .  .  .  .  .
 2  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
 3  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
 4  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
 5  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
 6  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
 7  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
 8  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
 9  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
10  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
11  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
12  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
13  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
14  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
15  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .

check_for_five(board)  
    True  
check_for_winner(board)  
    checking row 1  
        checking col 1
True
```
  
`check_for_winner` will succeed quickly if there are matches originating from the (1, 1) coordinate. However, if there are not, the function becomes stuck in an extremely slow for loop (it does not abort from max recursion depth), before aborting from a list index out of range error. The `check_for_five` function can be manually called for other originating coordinates by setting the row & column values passed to the function instead of accepting their defaults. But, since the `check_for_winner` function was originally written as a nested for-loop to examine all possible starting coordinates in the game board, as-is it will not function correctly in most cases.  

Second Release
------  
https://github.com/jabrabec/pente/releases/tag/second_release  

Because I was unsatisfied with these results, I continued to work on this program beyond the 4-hour limit, but I wanted to make that distinction very clear both here and with the tagged releases in the repo. The following changes represent about 2 additional hours of work on this program.  

- `check_for_five` no longer limits the allowable row and/or column values that can serve as the origination coordinates for 5-in-a-row sequence. Instead, all neighboring space equivalency checks are nested in a `try/except` group in order to handle potential index out of range errors. This has solved the failure of `check_for_five` to find diagonal-upward sequences as well as fixed a bug where sequences could not win if they contained markers in the right-most few columns or bottom-most few rows.
- `check_for_five` is also separated into 4 different functions according to the direction being checked, and each function is called separately in the `check_for_winner` function, to fix a bug where sometimes sequences of 5 that were connected but not in a straight line would trigger a win.
- `check_for_winner` is changed to use the set of occupied spaces listed in `played` as the source of row & column indices to pass to the `check_for_five` functions, instead of having to iterate over the entire gameboard with every play. This has significantly improved processing time. This function is also now called after every play a player or the computer makes, and ends the game appropriately.
- Because of these changes, the game can now find winning sequences anywhere on the board and can be launched wholly from the command line.
- Comments and print statements have been cleaned up.  

I was not able to address the ability in Pente for players to capture their opponent’s pieces. Using a horizontal-row example, my plan for that was to be along the lines of the following:  

```
if (
    board[x][y] == ‘ O’ and if board[x][y+1] == ‘ X’ and
    board[x][y+2] == ‘ X’ and board[x][y+3] == ‘ .’
):
    board[x][y+1] == ‘ .’
    board[x][y+2] == ‘ .’
    board[x][y+3] == ‘ O’
    capture_count += 2
```
  

With another as-yet-named function getting called once a player placed a piece in order to check the `capture_count` and end the game if that reached 10 or more. The `computer_play` function would also be modified to check for opportunities to capture the player’s pieces, with a random (or semi-random, weighted?) determination of whether to capture or place another random piece on the board.
