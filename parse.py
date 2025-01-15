import chess

board = chess.Board()
print(board)

# print("\n")

# Nf3 = chess.Move.from_uci("g1f3")
# board.push(Nf3)
# print(board)

for m in dir(board):
    print(m)

# with open("games.txt", "r") as games_file:
#     payload = games_file.read().split("\n\n")
#     for i in range(0, len(payload)-1, 2):
#         print(payload[i])
#         print(payload[i+1])
#         print("\n")