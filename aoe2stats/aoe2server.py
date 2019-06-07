from flask import Flask
from flask_restful import Api

from aoe2stats.GameResourceDebug import GameResourceDebug
from aoe2stats.GameResource import GameResource
from aoe2stats.ResetResource import ResetResource
from aoe2stats.cheats import findPid
from aoe2stats.memutils import openProc

def startServer(debug = True):
    openProc(findPid())
    app = Flask('')
    api = Api(app)

    @app.route("/")
    def hello():
        return app.send_static_file('index.html')

    @app.after_request
    def add_header(r):
        """
        Add headers to both force latest IE rendering engine or Chrome Frame,
        and also to cache the rendered page for 10 minutes.
        """
        r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        r.headers["Pragma"] = "no-cache"
        r.headers["Expires"] = "0"
        r.headers['Cache-Control'] = 'public, max-age=0'
        return r

    api.add_resource(GameResource, '/game')
    api.add_resource(GameResourceDebug, '/game-dbg')
    api.add_resource(ResetResource, '/reset')
    app.run(debug=debug)