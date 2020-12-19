from flask import Flask , render_template
from game import Game 


app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/game')
def game(): 
    my_game = Game()
    my_game.run()
    return "Game END"


if __name__ ==  "__main__":





    app.run(debug=True, host='0.0.0.0')