import chess

with open("games.txt", "r") as games_file:
    payload = games_file.read().split("\n\n")
    dataset = []
    for i in range(0, len(payload)-1, 2):
        split_payload = payload[i].split("\n")
        white = False
        if split_payload[0] == "":
            white = split_payload[4].split(" ")[1][0:-1] == '"punmaster_general"'
        else:
            white = split_payload[3].split(" ")[1][0:-1] == '"punmaster_general"'

        movelist = payload[i+1].split(".")
        movescount = len(movelist)

        if white:
            dataset.append([-1])
            for i in range(1, movescount, 1):
                moverep = movelist[i].split(" ")
                dataset[-1].append(moverep[1])
                dataset.append([moverep[2]])
            if len(dataset[-1]) == 1:
                dataset = dataset[0:-1]
            
        else:
            for i in range(1, movescount, 1):
                moverep = movelist[i].split(" ")
                dataset.append([moverep[1], moverep[2]])
            if len(dataset[-1]) == 1 or dataset[-1][0][-1] == "#":
                dataset = dataset[0:-1]

        dataset.append(-2)

uci_dataset = []
board = chess.Board()
for row in dataset:
    if row == "done":
        board = chess.Board()
        continue
    uci_row = []
    if row[0] == -1:
        uci_row.append(-1)
    else:
        move = board.parse_san(row[0])
        board.push_san(row[0])
        uci_row.append(move.uci())

    try:
        move = board.parse_san(row[1])
        legalmoves = list(map(lambda x: str(x), board.legal_moves))
        board.push_san(row[1])
        uci_row.append(move.uci())
        uci_row.append(index(legalmoves, row[1]))
        uci_dataset.append(uci_row)
    except chess.InvalidMoveError as e:
        continue

with open("dataset_num.csv", "w") as data_file:
    data_file.write("opponent,mine\n")
    for row in uci_dataset:
        data_file.write(",".join(row)+"\n")