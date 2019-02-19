from rasa_nlu.converters import load_data
from rasa_nlu.model import Trainer
from rasa_nlu.model import RasaNLUConfig
from rasa_nlu.model import Interpreter
import time


training_data = load_data('./data/data.md')
trainer = Trainer(RasaNLUConfig('./config_spacy.json'))
trainer.train(training_data)
model_directory = trainer.persist('./model', project_name="commandnlu")

time.sleep(2)
def run():
    interpreter = Interpreter.load(model_directory)
    print(interpreter.parse("Bye"))

run()
