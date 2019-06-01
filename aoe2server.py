from flask import Flask
from flask_restful import Api

from GameResourceDebug import GameResourceDebug
from GameResource import GameResource
from ResetResource import ResetResource
from cheats import findPid
from memutils import openProc

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello():
    return app.send_static_file('index.html')

api.add_resource(GameResource, '/game')
api.add_resource(GameResourceDebug, '/game-dbg')
api.add_resource(ResetResource, '/reset')

if __name__ == '__main__':
    openProc(findPid())
    app.run(debug=True)

