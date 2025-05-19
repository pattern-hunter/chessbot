from kfp import compiler, dsl
from parse import parse_data
from random_forest import train_random_forest
from predict import predict


@dsl.component(
	base_image="python3.13.1"
)
def parse_game_data() -> str:
	parse_data()

@dsl.component(
	base_image="python3.13.1",
	packages_to_install = ['sklearn']
)
def train_model(filename: str) -> str:
	return train_random_forest(filename)


@dsl.component(
	base_image="python3.13.1",
	packages_to_install = ['sklearn']
)
def predict_my_move(modelname: str, moves: list) -> str:
	return ", ".join(predict(moves))


@dsl.pipeline
def chessbot_pipeline(msg: str) -> str:
	filename = parse_game_data().output
	modelname = train_model(filename=filename).output
	return predict_my_move(modelname=modelname, moves=[1, 634, 56474]).output

compiler.Compiler().compile(chessbot_pipeline, package_path='pipeline.yaml')