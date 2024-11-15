import streamlit as st

# Initialize game state
if 'board' not in st.session_state:
    st.session_state.board = [['' for _ in range(3)] for _ in range(3)]
    st.session_state.current_player = 'X'
    st.session_state.winner = None
    st.session_state.tie = False

def check_winner(board):
    # Check rows, columns and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

def check_tie(board):
    for row in board:
        if '' in row:
            return False
    return True

def reset_game():
    st.session_state.board = [['' for _ in range(3)] for _ in range(3)]
    st.session_state.current_player = 'X'
    st.session_state.winner = None
    st.session_state.tie = False

# Create the Tic-Tac-Toe board
st.title("Tic-Tac-Toe")

for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        if cols[j].button(st.session_state.board[i][j] or ' ', key=f'{i}-{j}'):
            if st.session_state.board[i][j] == '' and st.session_state.winner is None:
                st.session_state.board[i][j] = st.session_state.current_player
                st.session_state.winner = check_winner(st.session_state.board)
                st.session_state.tie = check_tie(st.session_state.board)
                if st.session_state.winner is None and not st.session_state.tie:
                    st.session_state.current_player = 'O' if st.session_state.current_player == 'X' else 'X'

# Check for a winner or a tie
if st.session_state.winner:
    st.success(f"Player {st.session_state.winner} wins!")
elif st.session_state.tie:
    st.info("The game is a tie!")

# Reset button
if st.button("Reset Game"):
    reset_game()
