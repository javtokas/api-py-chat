from flask import Flask
from flask import request, jsonify
import os
import aiml

app = Flask(__name__)

BRAIN_FILE="brain.dump"

k = aiml.Kernel()

# To increase the startup speed of the bot it is
# possible to save the parsed aiml files as a
# dump. This code checks if a dump exists and
# otherwise loads the aiml from the xml files
# and saves the brain dump.
if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)

# Endless loop which passes the input to the bot and prints
# its response

@app.route('/', methods=['GET'])
def result():
    if 'id' in request.args:
        id = request.args['id']
    else:
        id = "hi"
    input_text = id
    response = k.respond(input_text)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
    
