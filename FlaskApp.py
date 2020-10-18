from flask import Flask
from exampleIntegration import cycle
import EmoteModel
app = Flask(__name__)

global logreg
global count_vectors

@app.before_first_request
def torrtle():
    global logreg
    global count_vectors 
    logreg, count_vectors = EmoteModel.init_model()
    


@app.route('/_refresh')
def hello_world():
    global logreg
    global count_vectors 
    return str(cycle(logreg, count_vectors))

if __name__ == "__main__":
    app.run(debug=True) 
