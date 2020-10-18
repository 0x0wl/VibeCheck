from flask import Flask
from exampleIntegration import cycle
import EmoteModel
from flask import jsonify
from flask import render_template
from flask import send_file
app = Flask(__name__, static_url_path='', static_folder='static')

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
    return jsonify(ratio=str(cycle(logreg, count_vectors)))

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
