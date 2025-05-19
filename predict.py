import pickle

def predict(modelname, moves):
	with open(modelname, "rb") as modelfile:
		model = pickle.load(modelfile)
		moveslist = []
		for move in moves:
			moveslist.append([move])
		y = model.predict(moveslist)
		return y