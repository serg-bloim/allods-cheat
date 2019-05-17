from flask import Flask
from flask_restful import Api

from GameResource import GameResource
from cheats import findPid
from memutils import getMemOps, openProc

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello():
    from flask import render_template
    return render_template('index.html')

api.add_resource(GameResource, '/game')

if __name__ == '__main__':
    openProc(findPid())
    app.run(debug=True)

