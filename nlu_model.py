from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Interpreter

training_data = load_data('./data/data.md')
trainer = Trainer(config.load('./config_spacy.json'))
trainer.train(training_data)
model_directory = trainer.persist('./model', project_name="commandnlu")


interpreter = Interpreter.load(model_directory)

def run(inp):
    print(interpreter.parse(inp))
